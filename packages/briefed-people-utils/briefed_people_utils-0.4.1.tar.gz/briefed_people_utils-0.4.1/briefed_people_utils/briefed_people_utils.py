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


def update_or_create_model_instance(host,token,username,password,payload,model_name=None):
    
    if model_name:
        url = '{0}api/{1}/update/'.format(host,model_name)
    else:
        url = '{0}api/update/_bulk'.format(host)
    
    headers = {
        'Authorization': 'Token {0}'.format(token),
        'user': username,
        'password': password,
        'Content-Type': 'application/json',
    }
    response = requests.put(url,headers=headers,json=payload)
    
    return response
