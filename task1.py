import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
data = requests.get(url)
dict_for_three_heros = {}
intelligences = []
for superhero in data.json():
    if superhero['name'] == 'Hulk':
        dict_for_three_heros['Hulk'] = superhero['powerstats']['intelligence']
        intelligences.append(superhero['powerstats']['intelligence'])
    elif superhero['name'] == 'Captain America':
        dict_for_three_heros['Captain America'] = superhero['powerstats']['intelligence']
        intelligences.append(superhero['powerstats']['intelligence'])
    elif superhero['name'] == 'Thanos':
        dict_for_three_heros['Thanos'] = superhero['powerstats']['intelligence']
        intelligences.append(superhero['powerstats']['intelligence'])
    if len(dict_for_three_heros.keys()) == 3:
        break

max_intelligence = max(intelligences)
for name, intelligence in dict_for_three_heros.items():
    if intelligence == max_intelligence:
        print(f'Самый сильный супергерой - {name}, intelligence = {intelligence}')
        break