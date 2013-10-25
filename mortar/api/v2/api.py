#
# Copyright 2013 Mortar Data Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import requests
from requests.auth import HTTPBasicAuth

class API(object):
    
    HEADERS = {'Accept': 'application/json',
               'Accept-Encoding': 'gzip',
               'Content-Type': 'application/json',
               # TODO add version
               'User-Agent': 'mortar-api-python'}
    
    def __init__(self, email, api_key, scheme='https', host='api.mortardata.com'):
        self.auth = HTTPBasicAuth(email, api_key)
        self.scheme = scheme
        self.host = host
    
    def url(self, path):
        return '%s://%s/v2/%s' % (self.scheme, self.host, path)
    
    def post(self, path, payload):
        # prep
        post_url = self.url(path)
        json_payload = json.dumps(payload)
        
        # request
        response = requests.post(post_url, data=json_payload, auth=self.auth, headers=API.HEADERS)
        
        # test and return
        response.raise_for_status()
        return response.json()
    
    def get(self, path, params=None):
        # prep
        get_url = self.url(path)
        
        # request
        response = requests.get(get_url, params=params, auth=self.auth, headers=API.HEADERS)

        # test and return
        response.raise_for_status()
        return response.json()
    
    def put(self, path, payload):
        # prep
        put_url = self.url(path)
        json_payload = json.dumps(payload)

        # request
        response = requests.put(put_url, data=json_payload, auth=self.auth, headers=API.HEADERS)

        # test and return
        response.raise_for_status()
        return response.json()

    def delete(self, path):
        # prep
        delete_url = self.url(path)

        # request
        response = requests.delete(delete_url, auth=self.auth, headers=API.HEADERS)

        # test and return
        response.raise_for_status()
    

