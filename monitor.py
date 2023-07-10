import calendar
import time
import json
import sys

import requests
import toml


config = toml.load(open('config.toml'))

http_session = requests.Session()
http_session.auth = (config['username'], config['password'])
orbi_url = '{}?ts={}'.format(
    config['orbi_url'],
    calendar.timegm(time.gmtime())
)

resp = http_session.get(orbi_url, verify=False)

devices = None
for line in resp.text.split('\n'):
    if line.startswith('device='):
        devices = json.loads(line.lstrip('device='))
        break


active_devices = [dev['name']
                  for dev in devices
                  if 'backhaul_sta' in dev
                  and dev['backhaul_sta'] == 'Good']
if sys.argv[1] in active_devices:
    sys.exit(0)
else:
    raise Exception("Device '{}' not found or is inactive".format(sys.argv[1]))
    sys.exit(1)