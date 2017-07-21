import base64
import json
import re
import requests

def getShortUrl(analysisId):
    target_url = 'http://mchen.cbapac.net:3000/matches/{0}'.format(analysisId)

    endpoint = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAl-y9zwhEdTm9sK41NlJ1j0OjybGI8o58'
    payload = { 'longUrl': target_url }

    res = requests.post(endpoint, json=payload)
    res_json = json.loads(res.text)

    short_url = res_json['id']
    short_url_no_protocol = re.sub(r'^https?://', '', short_url)
    return short_url_no_protocol
