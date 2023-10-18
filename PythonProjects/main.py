import requests 

token = "6d8f1a44d89b4928fa502a1c613ecdd1"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', 
                        
json = {
    "name": "DOVVJ",
    "photo": "https://dolnikov.ru/pokemons/albums/040.png"}, 
headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (response.text)


response = requests.patch('https://api.pokemonbattle.me:9104/pokemons',
json = { 
    "pokemon_id": "12637",
    "name": "ALISA"
},
headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (response.text)

response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
json = { 
    "pokemon_id": "12637"
},
headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (response.text)







