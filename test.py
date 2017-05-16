myInventory = {
'rope'		:	1,
'torch'		:	6,
'gold coin'	:	42,
'dagger'	:	1,
'arrow'		:	12,
'potion'	:	19
}

dragonLoot = [
'gold coin',
'dagger',
'gold coin',
'gold coin',
'ruby'
]


for k,v in myInventory.items():
	itemCount = 0
	for loot in dragonLoot:
		if loot == k:
			v = v + dragonLoot.count(loot)
		else:
			itemCount = itemCount + v.get(str(loot, 1))
	print k,v