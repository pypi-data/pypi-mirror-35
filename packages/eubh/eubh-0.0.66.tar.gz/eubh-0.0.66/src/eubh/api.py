import json
from requests import *
from .config import Config


class Api:
    def __init__(self, key=None):
        config = Config()
        self.key = key
        self.base_url = config.get('HTTP_ADDRESS')
        self.headers = {'Content-Type': 'application/json'}

    def get_url(self, url):
        return "%s/%s" % (self.base_url, url)

    def upload_machine_and_get_task(self, data={}):
        return post(self.get_url('project/machine/%s' % (data.get('mac'))), data=json.dumps(data),
                    headers=self.headers).json()

    def project_machine_update_cmd(self, data={}):
        return post(self.get_url('project/machine/%s/update-cmd' % data.get('id')), data=data)

    def store_project_container_log(self, data={}):
        return post(self.get_url('project/container-log'), data=data)

    def get_project_info_by_key(self):
        return get(self.get_url('project/project/%s' % self.key), headers=self.headers).json()

    def get_project_container_lists(self, key):
        return get(self.get_url('project/container/lists/%s' % key), headers=self.headers).json()

    def get_project_container_logs_by_container_id(self, container_id):
        return get(self.get_url('project/container-log/%s/logs-by-container-id' % container_id)).json()

    def post_project_container_logs(self, data={}):
        return post(self.get_url('project/container-log/%s/set' % data.get('container_id')), data=data)

    def get_config_by_key(self):
        return self.get_project_info_by_key()
