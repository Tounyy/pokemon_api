from dotenv import load_dotenv
import os
import requests

load_dotenv()

class PokeAPI:
    def __init__(self):
        self.base_url = os.getenv('POKEAPI_BASE_URL')

    def get_pokemon_list(self, limit=100):
        response = requests.get(f"{self.base_url}?limit={limit}")
        print(f"response in get_pokemon_list")
        if response.status_code == 200:
            return response.json()['results']
        else:
            return []

    def get_total_pokemon_count(self):
        response = requests.get(f"{self.base_url}?limit=1")
        print(f"response in get_total_pokemon_count")
        if response.status_code == 200:
            total_count = response.json()["count"]
            return total_count
        else:
            return 0

    def get_pokemon_details(self, name_or_id):
        response = requests.get(f"{self.base_url}/{name_or_id}")
        print(f"response in get_pokemon_details")
        if response.status_code == 200:
            return response.json()
        else:
            return None