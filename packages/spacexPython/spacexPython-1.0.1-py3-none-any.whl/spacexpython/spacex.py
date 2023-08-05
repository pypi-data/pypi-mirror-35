import requests
import urldata



def launches():
    requestUrl = url.Domain.main + url.Domain.main_launches
    url_response = requests.get(url=str(requestUrl))
    response = url_response.json()
    return response

