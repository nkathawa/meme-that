import requests

resp = requests.get('https://api.imgflip.com/get_memes')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /get_memes/ {}'.format(resp.status_code))

for todo_item in resp.json()["data"]["memes"]:
	if todo_item['box_count'] == 2:
		print('{},{}'.format(todo_item['name'], todo_item['url']))
		#myfile = requests.get(todo_item['url'])
		#open(todo_item['name'].replace(" ", "")+'.png', 'wb').write(myfile.content)
