import requests

resp = requests.get('https://covercovid-19.com/reports/counties/king/washington')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    counties = resp.json()
    if counties is None:
        print("Uh-Oh, it looks like you might have mistyped the county name. Click [here](https://covercovid-19.com/#map-anchor) to view the whole interactive map of US Covid-19 statistics.")
    else:
        lat = counties["latitude"]
        lon = counties["longitude"]
        print("Click [here](https://covercovid-19.com/?lat={}&lon={})".format(lat, lon))