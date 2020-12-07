import requests
from urllib.parse import quote, urljoin

COUNTRIES_URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'


class CountriesList:
    def __init__(self):
        response = requests.get(COUNTRIES_URL)
        self.response_lines = iter(response.json())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response_lines)['name']['common']


def wiki_url_exist(url):  # все ссылки я проверил, но это очень медленно
    response = requests.get(url)
    return response.status_code == 200


if __name__ == '__main__':
    countries_list = CountriesList()
    with open('countries.txt', mode='w', encoding='utf-8') as f:
        for country_name in countries_list:
            country_url = urljoin('https://en.wikipedia.org/wiki/', quote(country_name.replace(' ', '_')))
            # if not wiki_url_exist(country_url):
            #     print(f'{country_name} - WRONG URL')
            #     country_url = 'NOT FOUND'
            f.write(f'{country_name} - {country_url}\n')
