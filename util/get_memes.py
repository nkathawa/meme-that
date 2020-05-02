import requests
import json

resp = requests.get('https://api.imgflip.com/get_memes')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /get_memes/ {}'.format(resp.status_code))

# memes = resp.json()["data"]["memes"]
# print memes

my_data = {}
for meme in resp.json()["data"]["memes"]:
	if meme['box_count'] == 2:
		data = {'name': meme['name'], 'url': meme['url']}
		my_data[meme['id']] = data
		# myfile = requests.get(meme['url'])
		# open(meme['name'].replace(" ", "").replace("?", "") +'.png', 'wb').write(myfile.content)
json_data = json.dumps(my_data)
sample = open('samplefile.txt', 'w') 
sample.write(json_data) 
sample.close()