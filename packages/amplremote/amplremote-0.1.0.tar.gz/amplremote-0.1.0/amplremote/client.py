#!/usr/bin/env python
from __future__ import print_function, absolute_import, division
from base64 import b64encode, b64decode
from time import sleep
import sys
import os
import re
import json
import requests

"""
model diet.mod;
data diet.dat;
option solver remote;
option remote_options '  solver="gurobi"';
option gurobi_options 'outlev=1';
solve;

option remote_options "solver='gurobi' user='admin' pass='secret' url='http://0.0.0.0:5001/api/'";

"""

BASE_URL = "http://0.0.0.0:5001/api/"
USERNAME='admin'
PASSWORD='secret'

class Client:
    def __init__(self, base_url, username, password):
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url
        self.username = username
        self.password = password

    def post(self, url, data):
        if not url.startswith('http'):
            url = self.base_url + url
        return requests.post(
            url, auth=(self.username, self.password),
            verify=True, json=data
        )

    def get(self, url):
        if not url.startswith('http'):
            url = self.base_url + url
        return requests.get(
            url, auth=(self.username, self.password),
            verify=True
        )


def main():
    assert len(sys.argv) == 3 and sys.argv[2] == '-AMPL'

    nlfile = sys.argv[1] + '.nl'

    # Handle options
    options = dict(
      re.findall(r'''([^\s]+)\s*=\s*("[^"]*"|'[^']*'|[^\s]+)''',
      os.getenv('remote_options'))
    )
    for opt in options:
        options[opt] = options[opt].strip('\'"')
    solver = options.get('solver', None)
    if solver is None:
        raise Exception('Must specify the solver name')
    solver_options = os.getenv('{}_options'.format(solver))
    if solver_options is None:
        solver_options = ''
    # print(solver, solver_options, options)

    client = Client(
        options.get('url', BASE_URL),
        options.get('user', USERNAME),
        options.get('pass', PASSWORD)
    )

    res = client.post('jobs', {'user': USERNAME,
            'model': b64encode(open(nlfile, 'rb').read()),
            'options': options,
            'solver': solver,
            'solver_options': solver_options
        }
    )
    # print('CODE:', res.status_code)
    if not res.ok:
        res.raise_for_status()

    if res.ok:
        data = json.loads(res.content)
        job_id = data['id']

    while True:
        sleep(1)
        res = client.get('jobs/{job_id}'.format(job_id=job_id))
        # print('CODE:', res.status_code)
        if not res.ok:
            res.raise_for_status()

        if res.ok:
            data = json.loads(res.content)
            if data['alive'] is False:
                print(data['output'])
                solution = data['solution']
                open(sys.argv[1]  + '.sol', 'wb').write(b64decode(solution))
                break


if __name__ == '__main__':
    main()
