# Rancher-based deployment functions

import os
import requests
import json
import base64
import time
import subprocess
import logging
_logger = logging.getLogger(__name__)

from wordpress_cd.drivers import driver
from wordpress_cd.drivers.base import BaseDriver, randomword


@driver('rancher')
class RancherDriver(BaseDriver):
    def __str__(self):
        return "Rancher"

    def __init__(self, args, test_dataset = None):
        super(RancherDriver, self).__init__(args, test_dataset = test_dataset)

        _logger.debug("Initialising Rancher Deployment Driver")

        try:
            self.image_uri = os.environ['WPCD_DOCKER_IMAGE']
            self.rancher_secret_key = os.environ['RANCHER_SECRET_KEY']
            self.rancher_access_key = os.environ['RANCHER_ACCESS_KEY']
        except KeyError as e:
            raise Exception("Missing '{0}' environment variable.".format(e))

        self.mysql_root_pass = randomword(10)

    def _get_docker_compose_yml(self, docker_image):
        with open("config/rancher/docker-compose.yml") as f:
            docker_compose_yml = f.read()
        docker_compose_yml = docker_compose_yml.replace("{{ docker_image }}", docker_image)
        docker_compose_yml = docker_compose_yml.replace("{{ mysql_root_pass }}", self.mysql_root_pass)
        docker_compose_yml = docker_compose_yml.replace("{{ mysql_user }}", self.test_dataset.mysql_user)
        docker_compose_yml = docker_compose_yml.replace("{{ mysql_pass }}", self.test_dataset.mysql_pass)
        docker_compose_yml = docker_compose_yml.replace("{{ mysql_db }}", self.test_dataset.mysql_db)
        return docker_compose_yml

    def _get_rancher_compose_yml(self):
        with open("config/rancher/rancher-compose.yml") as f:
            rancher_compose_yml = f.read()
        rancher_compose_yml = rancher_compose_yml.replace("{{ hostname }}", self.test_site_fqdn)
        return rancher_compose_yml

    def _setup_host(self):
        # Use Rancher API call to create a new stack:
        # https://rancher.com/docs/rancher/v1.2/en/api/v2-beta/api-resources/stack/#create

        # Prepare the 'docker-compose.yml' file
        docker_image = "rossigee/wordpress:latest" # just for a moment...
        docker_compose_yml = self._get_docker_compose_yml(docker_image)

        # Prepare the 'rancher-compose.yml' file
        rancher_compose_yml = self._get_rancher_compose_yml()

        # Service endpoint (v2-beta)
        projectId = os.environ['RANCHER_ENVIRONMENT']
        endpoint_url = os.environ['RANCHER_URL'] + '/v2-beta/projects/' + projectId + '/stack'
        auth = (self.rancher_access_key, self.rancher_secret_key)

        # Construct payload for stack creation
        payload = {
            "name": "wp-citest-" + self.test_site_uid,
            "description": "WordPress CI test ({})".format(self.test_site_uid),
            "dockerCompose": docker_compose_yml,
            "rancherCompose": rancher_compose_yml,
            "startOnCreate": True
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(endpoint_url,
                          data=json.dumps(payload), headers=headers,
                          auth=auth)
        if r.status_code != 201:
            raise Exception("Unexpected HTTP status code: {}".format(r.status_code))
        res = r.json()
        self.stack_id = res['id']
        _logger.info("Stack creation started, stack id: {}".format(self.stack_id))

        # Wait for it to become active
        endpoint_url = os.environ['RANCHER_URL'] + '/v2-beta/projects/' + projectId + '/stack/' + self.stack_id
        state = res['state']
        sleep = 10
        retry = 30
        while (state != 'active'):
            _logger.debug("stack: " + self.stack_id + " [" + state + "]")
            time.sleep(sleep)
            r = requests.get(endpoint_url, auth=auth)
            res = r.json()
            state = res['state']
            retry -= 1
            if retry <= 0:
                _logger.error("Maximum retries exceeded")
                return 1

        _logger.info("Stack creation complete, stack id: {}".format(self.stack_id))

    def _teardown_host(self):
        # Use Rancher API call to delete a stack:
        # https://rancher.com/docs/rancher/v1.2/en/api/v2-beta/api-resources/stack/#delete

        # Service endpoint (v2-beta)
        projectId = os.environ['RANCHER_ENVIRONMENT']
        endpoint_url = os.environ['RANCHER_URL'] + '/v2-beta/projects/' + projectId + '/stack/' + self.stack_id
        auth = (self.rancher_access_key, self.rancher_secret_key)

        # Upgrade the service with payload
        r = requests.delete(endpoint_url,
                          auth=auth)
        if r.status_code != 200:
            raise Exception("Unexpected HTTP status code: {}".format(r.status_code))
        _logger.info("Stack deleted, stack id: {}".format(self.stack_id))

    def _docker_build(self):
        buildargs = ['docker', 'build', '-t', self.image_uri, '.']
        buildenv = os.environ.copy()
        buildproc = subprocess.Popen(buildargs, stderr=subprocess.PIPE, env=buildenv)
        buildproc.wait()
        exitcode = buildproc.returncode
        errmsg = buildproc.stderr.read()
        if exitcode != 0:
            raise Exception("Error while building image: %s" % errmsg)

    def _docker_push(self):
        pushargs = ['docker', 'push', self.image_uri]
        pushenv = os.environ.copy()
        pushproc = subprocess.Popen(pushargs, stderr=subprocess.PIPE, env=pushenv)
        pushproc.wait()
        exitcode = pushproc.returncode
        errmsg = pushproc.stderr.read()
        if exitcode != 0:
            raise Exception("Error while pushing image: %s" % errmsg)

    def _upgrade_rancher_service(self, projectId, serviceId):
        # Use Rancher API call to upgrade a service's stack:
        # https://rancher.com/docs/rancher/v1.2/en/api/v2-beta/api-resources/service/#upgrade

        # Service endpoint (v2-beta)
        endpoint_url = os.environ['RANCHER_URL'] + '/v2-beta/projects/' + projectId + '/services/' + serviceId
        auth = (self.rancher_access_key, self.rancher_secret_key)

        # Find service based on the ids provided
        _logger.info("Fetch current status of service ({})... ".format(endpoint_url))
        r = requests.get(endpoint_url, auth=auth)
        if r.status_code != 200:
            raise Exception("Unexpected HTTP status code: {}".format(r.status_code))
        service = r.json()
        launchConfig = service['launchConfig']
        secondaryLaunchConfigs = service['secondaryLaunchConfigs']

        # Update launchConfig with new image
        launchConfig['imageUuid'] = "docker:" + self.image_uri

        # Construct payload for upgrade
        payload = {
            'inServiceStrategy': {
                'batchSize': 1,
                'intervalMillis': 2000,
                'startFirst': False,
                'launchConfig': launchConfig,
                'secondaryLaunchConfigs': secondaryLaunchConfigs,
            }
        }
        headers = {'content-type': 'application/json'}

        # Upgrade the service with payload
        _logger.info("Requesting upgrade of service to use image '{}'... ".format(self.image_uri))
        r = requests.post(endpoint_url + '?action=upgrade',
                          data=json.dumps(payload), headers=headers,
                          auth=auth)
        if r.status_code != 200:
            raise Exception("Unexpected HTTP status code: {}".format(r.status_code))
        res = r.json()

        # Poll service upgrade status
        sleep = 10
        retry = 30
        state = 'checking'
        while (state != 'upgraded'):
            r = requests.get(endpoint_url, auth=auth)
            state = r.json()['state']
            _logger.debug("service: " + service['name'] + " [" + state + "]")
            if retry <= 0:
                _logger.error("Maximum retries exceeded")
                return 1
            time.sleep(sleep)
            retry -= 1
        _logger.debug("service: " + service['name'] + " [upgraded]")

        # Finish Upgrade
        _logger.info("Finishing upgrade of service...")
        r = requests.post(endpoint_url + '/?action=finishupgrade',
                          headers=headers, auth=auth)
        if r.status_code != 200:
            raise Exception("Unexpected HTTP status code: {}".format(r.status_code))

    def deploy_site(self):
        _logger.info("Deploying site to Rancher environment (job id: {0})...".format(self.job_id))

        _logger.info("Building new docker image...")
        self._docker_build()

        _logger.info("Pushing new docker image...")
        self._docker_push()

        _logger.info("Deploying new docker image to rancher service...")
        projectId = os.environ['RANCHER_ENVIRONMENT']
        serviceId = os.environ['RANCHER_SERVICE']
        self._upgrade_rancher_service(projectId, serviceId)

        # Done
        _logger.info("Deployment successful.")
        return 0

    def _setup_ssl(self):
        # Already covered by wildcard cert on LB
        pass

    def _teardown_ssl(self):
        pass
