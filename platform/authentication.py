from random import randint

class Player():
	def __init__(self, uuid, name):
		self.uuid = ""
		self.name = ""

class Authentication():
	def __init__(self, games):
		self.games = {}

	def generate_random_code(self):
		return randint(100000000, 999999999)

	def start_game(self, username):
		code = self.generate_random_code()
		self.games[code] = [username]
		return code

	def join_game(self, code, username):
		self.games[code].append(username)

def main():
	games = {}
	authentication = Authentication(games)
	code = authentication.start_game("navin")
	authentication.join_game(code, "john")
	code = authentication.start_game("javier")
	authentication.join_game(code, "anthony")
	code = authentication.start_game("josiah")
	authentication.join_game(code, "andrew")
	print(authentication.games)

if __name__ == "__main__":
    main()