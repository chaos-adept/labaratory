from mvc.model import Player
from mvc.controller import updatePlayerName
from mvc.controller import killPlayer
from mvc.view import renderPlayer
player = Player();

if __name__ == "__main__" :
	renderPlayer(player)
	updatePlayerName(player, "Mario")
	renderPlayer(player)
	killPlayer(player)
	renderPlayer(player)