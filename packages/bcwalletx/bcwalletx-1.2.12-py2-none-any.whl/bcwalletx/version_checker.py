import requests
import re


GITHUB_URL = 'https://github.com/dalijolijo/bcwalletx'
VERSION_URL = 'https://raw.githubusercontent.com/dalijolijo/bcwalletx/master/setup.py'


def get_latest_bcwallet_version():
    r = requests.get(VERSION_URL)
    assert r.status_code == 200, 'Could Not Connect to GitHub (status code %s)' % r.status_code
    matches = re.findall("version='(.*?)\'", r.content)
    assert matches, 'bcwalletx version not found on github'
    return matches[0]
