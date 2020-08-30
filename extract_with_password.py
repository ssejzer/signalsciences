import sys, requests, os, calendar, json
from datetime import datetime, timedelta

# Initial setup
api_host = 'https://dashboard.signalsciences.net'
email = os.environ.get('SIGSCI_EMAIL')
password = os.environ.get('SIGSCI_PASSWORD')
corp_name = 'testcorp'
site_name = 'www.mysite.com'

# Calculate UTC timestamps for the previous full hour
# E.g. if now is 9:05 AM UTC, the timestamps will be 8:00 AM and 9:00 AM
until_time = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
from_time = until_time - timedelta(hours=1)
until_time = calendar.timegm(until_time.utctimetuple())
from_time = calendar.timegm(from_time.utctimetuple())

# Authenticate
auth = requests.post(
    api_host + '/api/v0/auth',
    data = {"email": email, "password": password}
)

if auth.status_code == 401:
    print 'Invalid login.'
    sys.exit()
elif auth.status_code != 200:
    print 'Unexpected status: %s response: %s' % (auth.status_code, auth.text)
    sys.exit()

parsed_response = auth.json()
token = parsed_response['token']

# Loop across all the data and output it in one big JSON object
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer %s' % token
}
url = api_host + ('/api/v0/corps/%s/sites/%s/feed/requests?from=%s&until=%s' % (corp_name, site_name, from_time, until_time))
first = True

print '{ "data": ['

while True:
    response_raw = requests.get(url, headers=headers)
    response = json.loads(response_raw.text)

    for request in response['data']:
        data = json.dumps(request)
        if first:
            first = False
        else:
            data = ',\n' + data
        sys.stdout.write(data)

    next_url = response['next']['uri']
    if next_url == '':
        break
    url = api_host + next_url

print '\n] }'
