from random import randint

class Player():
	def __init__(self, name):
		self.uuid = randint(100000000, 999999999)
		self.name = name

class Authentication():
	def __init__(self, games):
		self.games = games

	def generate_random_code(self):
		return randint(100000000, 999999999)

	def start_game(self, player):
		code = self.generate_random_code()
		self.games[code] = [player]
		return code

	def join_game(self, code, player):
		self.games[code].append(player)

def main():
	navin = Player("navin")
	john = Player("john")
	javier = Player("javier")
	anthony = Player("anthony")
	josiah = Player("josiah")
	andrew = Player("andrew")

	games = {}
	authentication = Authentication(games)
	code = authentication.start_game(navin)
	authentication.join_game(code, john)
	code = authentication.start_game(javier)
	authentication.join_game(code, anthony)
	code = authentication.start_game(josiah)
	authentication.join_game(code, andrew)
	print(authentication.games)

if __name__ == "__main__":
    main()