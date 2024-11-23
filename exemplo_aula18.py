import requests
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True


def pegar_pokemon(id: int) -> Pokemon:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    #print(data)
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    #print(data['name'], types)
    return Pokemon(name=data['name'], type=types)  

pokemon = pegar_pokemon(1)
print(pokemon)
pokemon = pegar_pokemon(25)
print(pokemon)
pokemon = pegar_pokemon(4)
print(pokemon)
