import requests

resp = requests.get('https://covercovid-19.com/reports/self')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    print(resp.json())
