import requests

resp = requests.get('https://covercovid-19.com/reports/counties/top')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    counties = resp.json()
    body = ""
    for i, county in enumerate(counties, start =1):
        body +=  "\n" + str(i) + ". " + (county['name'] + ", " + county['state'] + ": " + str(county['2wd']))
    print(body)