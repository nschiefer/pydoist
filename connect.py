import httplib
import json
import urllib

# connects and makes a request to the appropriate Todoist API URL with the given params
# does not use HTTPS
# handles errors
# returns the Python-data structure (lists and dictionaries) representation of the JSON response
def connect(method="GET", url='', params={}):
    connection = httplib.HTTPConnection("todoist.com")

    return send_request(connection, method, url, params)

# secure version of connect
def connect_secure(url, params):
    connection = httplib.HTTPSConnection("todoist.com")

    return send_request(connection, method, url, params)

# sends the request using the given connection object
def send_request(connection, method, url, params):
    dest = "/API/" + url + "?" + urllib.urlencode(params)
    print dest

    connection.request(method, dest)

    response = connection.getresponse()

    return json.loads(response.read())

