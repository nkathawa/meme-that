import requests
import json

resp = requests.get('https://api.imgflip.com/get_memes')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /get_memes/ {}'.format(resp.status_code))

output_data = {}
for meme in resp.json()["data"]["memes"]:
	if meme['box_count'] == 2:
		data = {'name': meme['name'], 'url': meme['url']}
		output_data[meme['id']] = data
		# myfile = requests.get(meme['url'])
		# open(meme['name'].replace(" ", "").replace("?", "") +'.png', 'wb').write(myfile.content)
json_data = json.dumps(output_data)
output = open('output.txt', 'w') 
output.write(json_data) 
output.close()