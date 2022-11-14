import requests
from random import randint
from bs4 import BeautifulSoup
import re

user_agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]


def search(target):
    response = requests.get(f"http://{target}/contact", headers = {"User-agent" : "{}".format(user_agent[randint(0,4)])})
    
    if response.status_code != 200:
        if retry(target) == None:
            print(f"{target} : Erreur {response.status_code}")
        else:
            response = retry(target)

    return get_email(response, target)


def retry(target):

    response = requests.get(f"http://{target}", headers = {"User-agent" : "{}".format(user_agent[randint(0,4)])})

    if response.status_code != 200:
        target = target.split('.', 1)[0]
        response = requests.get(f"http://{target}.com", headers = {"User-agent" : "{}".format(user_agent[randint(0,4)])})

    # Ici pour ajouter une autre alternative à la requête

    if response.status_code != 200:
        return None
    else:
        return response


def get_email(response, target):
    soup = BeautifulSoup(response.text, "html.parser")

    text_soup = soup.get_text(" ")



    str_index = text_soup.find("@"+f"{target.split('.',1)[0]}")

    index_end = ""
    i = 0
    first_part = []
    while index_end != " ":
        i -= 1
        index_end = text_soup[str_index+i]
        first_part.append(text_soup[str_index+i])


    last_part = []
    index_start = ""
    i = 0
    while index_start != " ":
        index_start = text_soup[str_index-i]
        last_part.append(text_soup[str_index-i])
        i -= 1

    res = "".join(first_part)[::-1]+"".join(last_part)

    if not "@" in res or not "." in res:
        res = " Aucun mail"


    print(f"{target} :{res}")
    
    return res

    # email.append(soup.body.text[str_index+i])
    