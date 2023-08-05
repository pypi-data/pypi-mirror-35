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


def update_or_create_model_instance(model_name,token,username,password,data):
    url = 'https://briefed.eu/api/{0}/update'.format(model_name)
    headers = {
        'Authorization': 'Token {0}'.format(token),
        'user': username,
        'password': password,
    }
    response = requests.put(url,headers=headers,data=data)
    return response
    