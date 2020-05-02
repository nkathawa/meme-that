import requests
import json

with open('json_memes.json') as f:
  json_data = json.load(f)

for meme in json_data:
	myfile = requests.get(json_data[meme]['url'])
	open('pictures/' + json_data[meme]['name'].replace(" ", "").replace("?", "") + '.png', 'wb').write(myfile.content)