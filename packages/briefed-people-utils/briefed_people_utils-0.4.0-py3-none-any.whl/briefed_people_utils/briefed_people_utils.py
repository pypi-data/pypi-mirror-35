import requests
from bs4 import BeautifulSoup


def get_soup(link):

    try:

        link = link.replace('\n','').strip()
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(link,headers=headers)

        if response.status_code == requests.codes.ok:
            page = response.content
            soup = BeautifulSoup(page, "lxml")

        else:
            soup = None
            print("Requests returned status_code: {0}. {1}".format(response.status_code,link))

        return soup

    except Exception as e:
        print(str(e))
        print(link)


def prepare_url(host,model_name):
    if model_name:
        url = '{0}api/{1}/update/'.format(host,model_name)
    else:
        url = '{0}api/update/_bulk'.format(host)
    return url


def prepare_headers(token,username,password):
    headers = {
        'Authorization': 'Token {0}'.format(token),
        'user': username,
        'password': password,
    }
    return headers


def update_or_create_model_instance(host,token,username,password,data,files=None,model_name=None):

    url = prepare_url(host,model_name)
    headers = prepare_headers(token,username,password)
    response = requests.put(url,headers=headers,data=data)

    return response
