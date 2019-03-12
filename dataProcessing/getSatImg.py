import os
import json
import requests
import time
from requests.auth import HTTPBasicAuth


geometry = {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -119.13574218749999,
              36.36822190085111
            ],
            [
              -117.42187500000001,
              36.36822190085111
            ],
            [
              -117.42187500000001,
              37.112145754751516
            ],
            [
              -119.13574218749999,
              37.112145754751516
            ],
            [
              -119.13574218749999,
              36.36822190085111
            ]
          ]
        ]
      }

      # get images that overlap with our AOI 
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geometry
}

# get images acquired within a date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2016-08-31T00:00:00.000Z",
    "lte": "2016-09-01T00:00:00.000Z"
  }
}

# only get images which have <50% cloud coverage
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.5
  }
}

# combine our geo, date, cloud filters
combined_filter = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}

PLANET_API_KEY  = "6d91b0682f8e4887b240cf16c301ab8d"

item_type = "PSScene4Band"

# API request object
search_request = {
  "interval": "day",
  "item_types": [item_type], 
  "filter": combined_filter
}

# fire off the POST request
search_result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(PLANET_API_KEY, ''),
    json=search_request)

print(json.dumps(search_result.json(), indent=1))

image_ids = [feature['id'] for feature in search_result.json()['features']]
id0 = image_ids[0]
print("Image_ID0: ")
print(id0)

id0_url='https://api.planet.com/data/v1/item-types/{}/items/{}/assets'.format(item_type,id0)

result = \
  requests.get(
    id0_url,
    auth=HTTPBasicAuth(PLANET_API_KEY, '')
  )

print(result.json().keys())

links = result.json()["analytic"]["_links"]
self_link = links["_self"]
activation_link = links["activate"]

# Request activation of the 'analytic' asset:
activate_result = \
  requests.get(
    activation_link,
    auth=HTTPBasicAuth(PLANET_API_KEY, '')
  )
  
activation_status_result = \
  requests.get(
    self_link,
    auth=HTTPBasicAuth(PLANET_API_KEY, '')
  )
    
for x in range (10):
    print(activation_status_result.json()["status"])
    time.sleep(2)
    if activation_status_result.json()["status"]=="active":
        download_link = activation_status_result.json()["location"]
        print(download_link)
        break