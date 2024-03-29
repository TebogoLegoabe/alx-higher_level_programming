#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == '__main__':
    cut = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(cut) as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))
