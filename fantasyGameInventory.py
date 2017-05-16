################################
#Fantasy Game Inventory: Part 1#
################################

myInventory = {
'rope'		:	1,
'torch'		:	6,
'gold coin'	:	42,
'dagger'	:	1,
'arrow'		:	12,
'potion'	:	19
}

def displayInventory(inventory):
	print '' #Because terminal prints stuff hella crowded.
	print 'INVENTORY'
	print("-" * (len('INVENTORY')))
	item_total = 0
	for k,v in sorted(inventory.items()):
		print k.capitalize() + ' : ' + str(v)
		item_total = item_total + v
	print 'Total number of items: ', item_total
	print '' #Because terminal prints stuff hella crowded.

#displayInventory(myInventory)



################################
#Fantasy Game Inventory: Part 2#
################################

dragonLoot = [
'gold coin',
'dagger',
'gold coin'
'gold coin',
'ruby'
]

def addToInventory(inventory, addedItems):
	#Check test.py