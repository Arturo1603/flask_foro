import requests
from bs4 import BeautifulSoup


class WebScrapController:
    def __init__(self):
        self.url = f'https://www.impacto.com.pe/catalogo?qsearch='

    def scrap(self, searcher):
        try:
            page = requests.get(f'{self.url}{searcher}')
            soup = BeautifulSoup(page.content, 'html.parser')

            data = soup.find_all('img', class_='first-image')

            for info in data:
                print(info.get('src'))
            

            return {
                'message': 'OK'
            }

        except Exception as e:
            return {
                "message": "Ocurrio algo",
                'error': str(e),
            }, 500
