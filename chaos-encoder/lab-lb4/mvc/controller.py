import view
def updatePlayerName(player, newName):
	oldName = player.name
	player.name = newName
	view.showAction("player '%s' was changed to '%s'" % (oldName, newName))
	
def killPlayer(player):
	player.isAlive = False
	view.showAction("player '%s' was killed" % player.name);