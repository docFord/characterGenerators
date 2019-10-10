#!/usr/bin/python

# Random Character Generator v1.9

# Program requires termcolor to be installed
# you can download this via pip install termcolor
# because I am not making a requirements.txt for 1 package

from os import urandom
from time import sleep
import random
from termcolor import colored,cprint

# race array
races = ['Tortle',
		 'Dragonborn', #PHB
		 'Dwarf', #PHB
		 'Elf', #PHB 
		 'Gnome', #PHB 
		 'Half-Elf', #PHB 
		 'Half-Orc', #PHB 
		 'Halfling', #PHB 
		 'Human', #PHB 
		 'Tiefling', #PHB 
		 'Aarakocra', #VGM
		 'Aasimar', #VGM
		 'Bugbear', #VGM
		 'Firbolg',
		 'Goblin', #VGM
		 'Grung',
		 'Hobgoblin', #VGM
		 'Kenku', #VGM
		 'Kobold', #VGM
		 'Lizardfolk', #VGM
		 'Orc', #VGM
		 'Tabaxi', #VGM
		 'Triton',
		 'Yuan-Ti Pureblood', #VGM
		 'Goliath',
		 'Genasi',
		 'Minotaur', #Ravnica
		 'Centaur', #Ravnica
		 'Gith', #MTOF
		 'Awakened Undead', #dndBeyond homebrew
		 'Verdan', #AcqInc
		 'Loxodon', #Ravnica
		 'Vedalken', #Ravnica
		 'Warforged', #Wayfinders Eberron (DMs Guild)
		 'Changeling', #Wayfinders Eberron (DMs Guild)
		 'Shifter', #Wayfinders Eberron (DMs Guild)
		 'Kalashtar', #Wayfinders Eberron (DMs Guild)
]

# subrace dictionaries
elf_subraces = {0: 'High Elf', 1: 'Wood Elf', 2: 'Drow', 3: 'Eladrin', 4: 'Shadar-Kai', 5: 'Sea Elf'}
dwarf_subraces = {0:'Hill Dwarf', 1: 'Mountain Dwarf', 2: 'Duergar'}
aasimar_subraces = {0: 'Fallen Aasimar', 1: 'Protector Aasimar', 2: 'Scourge Aasimar'}
genasi_subraces = {0: 'Earth Genasi', 1: 'Water Genasi', 2: 'Air Genasi', 3: 'Fire Genasi'}
gith_subraces = {0: 'Githyanki', 1: 'Githzerai'}
gnome_subraces = {0: 'Forest Gnome', 1: 'Rock Gnome', 2: 'Deep Gnome'}
halfelf_subraces = {0: 'Half-Elf of Drow descent', 1: 'Half-Elf of High descent', 2: 'Half-Elf of Wood descent', 3: 'Half-Elf of Aquatic descent'}
halfling_subraces = {0: 'Lightfoot Halfling', 1: 'Stout Halfling', 2: 'Ghostwise Halfling', 3: 'Other', 4: 'Other', 5: 'Other'}
shifter_subraces = {0: 'Beasthide Shifter', 1: 'Longtooth Shifter', 2: 'Swiftstride Shifter', 3: 'Wildhunt Shifter'}
warforged_subraces = {0: 'Envoy Warforged', 1: 'Juggernaut Warforged', 2: 'Skirmisher Warforged'}

otherhalfling_subraces = { 0: 'Half-Halfling / Half-Orc',
						   1: 'Half-Halfling / Half-Dragonborn',
						   2: 'Half-Halfling / Quarter-Elf',
						   3: 'Half-Halfling / Quarter-Orc',
						   4: 'Half-Halfling / Half-Tiefling',
						   5: 'Half-Halfling / Half-Tortle',
						   6: 'Half-Halfling / Half-Kobold',
						   7: 'Half-Halfling / Half-Kenku',
						   8: 'Half-Halfling / Half-Goblin',
						   9: 'Half-Halfling / Half-Tabaxi',
						   10: 'Half-Halfling / Half-Dwarf',
						   11: 'Half-Halfling / Half-Bugbear',
						   12: 'Half-Halfling / Half-Aasimar',
}

human_subraces = { 0: 'Arkaiun',
				   1: 'Bedine',
				   2: 'Ffolk',
				   3: 'Gur',
				   4: 'Halruaan',
				   5: 'Imaskari',
				   6: 'Nar',
				   7: 'Shaaran',
				   8: 'Tuigan',
				   9: 'Ulutiun',
				   10: 'Calishite',
				   11: 'Chondathan',
				   12: 'Damaran',
				   13: 'Illuskan',
				   14: 'Mulan',
				   15: 'Rashemi',
				   16: 'Shou',
				   17: 'Tethyrian',
				   18: 'Turumi',
				   19: 'Chultan',
}
	# human subraces found in SCAG pp. 110-112

dragonborn_subraces = { 0: 'Black',
						1: 'Blue',
						2: 'Brass',
						3: 'Bronze',
						4: 'Copper',
						5: 'Gold',
						6: 'Green',
						7: 'Red',
						8: 'Silver',
						9: 'White',
}

# class dictionary (14 classes)
dndclass = ['Barbarian',
			'Bard',
			'Cleric',
			'Druid',
			'Fighter',
			'Monk',
			'Paladin',
			'Ranger',
			'Rogue',
			'Sorcerer',
			'Warlock',
			'Wizard',
			'Blood Hunter', #Matt Mercer
			'Artificer', #UA
			'Illrigger', #Strongholds and Followers Add-on Supplement
]

# class specialty/archetype/school/college etc. dictionaries
barbarian_subclass = { 0: 'Path of the Ancestral Guardian',
					   1: 'Path of the Battlerager',
					   2: 'Path of the Berserker',
					   3: 'Path of the Storm Herald',
					   4: 'Path of the Totem Warrior',
					   5: 'Path of the Zealot',
					   6: 'Path of the Wild Soul',
}

bard_subclass = { 0: 'College of Glamour',
				  1: 'College of Swords',
				  2: 'College of Lore',
				  3: 'College of Valor',
				  4: 'College of Whispers',
}


cleric_subclass = { 0: 'Forge Domain',
					1: 'Life Domain',
					2: 'Grave Domain',
					3: 'Tempest Domain',
					4: 'Trickery Domain',
					5: 'Death Domain',	#DMG p.96
					6: 'Arcana Domain',
					7: 'Knowledge Domain',
					8: 'Light Domain',
					9: 'Nature Domain',
					10: 'War Domain',
					11: 'Order Domain',	#Ravnica p.25
					12: 'Blood Domain'
}


druid_subclass = { 0: 'Circle of Dreams',
				   1: 'Circle of the Land',
				   2: 'Circle of the Moon',
				   3: 'Circle of the Shepherd',
				   4: 'Circle of Spores'	#Ravnica p.26
}

druid_land = ['Arctic',
			  'Coast',
			  'Desert',
			  'Forest',
			  'Grassland',
			  'Mountain',
			  'Swamp',
			  'Underdark'
]


fighter_subclass = { 0: 'Arcane Archer',
					 1: 'Battle Master',
					 2: 'Brute',
					 3: 'Cavalier',
					 4: 'Champion',
					 5: 'Eldritch Knight',
					 6: 'Purple Dragon Knight',
					 7: 'Samurai',
					 8: 'Scout',
}


fighter_style = { 0: 'Archery',
				  1: 'Defense',
				  2: 'Dueling',
				  3: 'Great Weapon Fighting',
				  4: 'Protection',
				  5: 'Two-Weapon Fighting',
}


monk_subclass = { 0: 'Way of the Drunken Master',
				  1: 'Way of the Four Elements',
				  2: 'Way of the Kensei',
				  3: 'Way of the Long Death',
				  4: 'Way of the Open Hand',
				  5: 'Way of Shadow',
				  6: 'Way of the Sun Soul',
				  7: 'Way of Tranquility',
				  8: 'Way of the Cobalt Soul', #Taldorei
}


paladin_subclass = { 0: 'Oath of Conquest',
					 1: 'Oath of Vengeance',
					 2: 'Oath of Redemption',
					 3: 'Oath of the Ancients',
					 4: 'Oath of the Crown',
					 5: 'Oath of Devotion',
					 6: 'Oathbreaker',
					 7: 'Oath of Secrets', #Ebonclad p.72
}

paladin_style = { 0: 'Defense',
				  1: 'Dueling',
				  2: 'Great Weapon Fighting',
				  3: 'Protection',
}

ranger_subclass = { 0: 'Beast Master',
					1: 'Hunter',
					2: 'Monster Slayer',
					3: 'Gloom Stalker',
					4: 'Horizon Walker',
					5: 'UA'
}

ranger_style = { 0: 'Archery',
				 1: 'Defense',
				 2: 'Dueling',
				 3: 'Two-Weapon Fighting',
}


rogue_subclass = { 0: 'Arcane Trickster',
				   1: 'Thief',
				   2: 'Assassin',
				   3: 'Mastermind',
				   4: 'Scout',
				   5: 'Inquisitive',
				   6: 'Swashbuckler',
}


sorcerer_subclass = { 0: 'Divine Soul',
					  1: 'Draconic Bloodline',
					  2: 'Shadow Magic',
					  3: 'Storm Sorcery',
					  4: 'Wild Magic',
					  5: 'Phoenix Sorcery',
}


warlock_subclass = { 0: 'The Archfey',
					 1: 'The Celestial',
					 2: 'The Fiend',
					 3: 'The Great Old One',
					 4: 'The Hexblade',
					 5: 'The Undying',
					 6: 'The Noble Genie', #XGTEE
					 7: 'The Chaos Walker', #XGTEE
}

warlock_pact = { 0: 'Pact of the Chain',
				 1: 'Pact of the Blade',
				 2: 'Pact of the Tome',
}


wizard_subclass = { 0: 'Artificer',
					1: 'Bladesinger',
					2: 'School of Abjuration',
					3: 'School of Conjuration',
					4: 'School of Divination',
					5: 'School of Enchantment',
					6: 'School of Evocation',
					7: 'School of Illusion',
					8: 'School of Necromancy',
					8: 'School of Transmutation',
					9: 'War Magic',
}


bloodhunter_subclass = { 0: 'Order of the Mutant',
						 1: 'Order of the Ghostslayer',
						 2: 'Order of the Profane Soul',
}

bloodhunter_rites = { 0: 'Rite of the Flame',
					  1: 'Rite of the Frozen',
					  2: 'Rite of the Storm',
}

artificer_subclass = {0: 'Alchemist', 1: 'Artillerist'} #Update with the new artificer changes when Eberron is released!

illrigger_subclass = {0: 'Shadowmaster', 1: 'Painkiller', 2: 'Architect of Ruin'}

illrigger_style = { 0: 'Treachery',
					1: 'Bravado',
					2: 'Schemes',
					3: 'Lies',
}

# random dictionaries

gender = { 0: 'Male',
		   1: 'Female'
}

alignment = { 0: 'Lawful Good',
			  1: 'Neutral Good',
			  2: 'Chaotic Good',
			  3: 'Lawful Neutral',
			  4: 'Neutral',
			  5: 'Chaotic Neutral',
			  6: 'Lawful Evil',
			  7: 'Neutral Evil',
			  8: 'Chaotic Evil',
}
#Need to list where these are from in the comments
background = { 0: 'Acolyte', #PHB
			   1: 'Anthropologist', #ToA
			   2: 'Archaeologist', #ToA
			   3: 'Caravan Specialist', #EE-AL
			   4: 'Charlatan', #PHB
			   5: 'City Watch', #SCAG
			   6: 'Clan Crafter', #SCAG
			   7: 'Cloistered Scholar', #SCAG
			   8: 'Courtier', #SCAG
			   9: 'Criminal', #PHB
			   10: 'Earthspur Miner', #EE-AL
			   11: 'Entertainer', #PHB
			   12: 'Faction Agent', #SCAG
			   13: 'Far Traveler', #SCAG
			   14: 'Folk Hero', #PHB
			   15: 'Gladiator', #PHB
			   16: 'Guild Artisan', #PHB
			   17: 'Guild Merchant', #PHB
			   18: 'Harborfolk', #EE-AL
			   19: 'Hermit', #PHB
			   20: 'Inheritor', #SCAG
			   21: 'Investigator', #SCAG
			   22: 'Knight', #PHB
			   23: 'Knight of the Order', #SCAG
			   24: 'Mercenary Veteran', #SCAG
			   25: 'Mulmaster Aristocrat', #EE-AL
			   26: 'Noble', #PHB
			   27: 'Outlander', #PHB
			   28: 'Pirate', #PHB
			   29: 'Sage', #PHB
			   30: 'Sailor', #PHB
			   31: 'Secret Identity', #RoD-AL
			   32: 'Shade Fanatic', #RoD-AL
			   33: 'Soldier', #PHB
			   34: 'Spy', #PHB
			   35: 'Trade Sheriff', #RoD-AL
			   36: 'Urban Bounty Hunter', #SCAG
			   37: 'Urchin', #PHB
			   38: 'Uthgardt Tribe Member', #SCAG
			   39: 'Waterdhavian Noble', #SCAG
			   40: 'Cormanthor Refugee', #RoD-AL
			   41: 'Gate Urchin', #RoD-AL
			   42: 'Hillsfar Merchant', #RoD-AL
			   43: 'Hillsfar Smuggler', #RoD-AL
			   44: 'Celebrity Adventurer\'s Scion', #AcqInc
			   45: 'Failed Merchant', #AcqInc
			   46: 'Plaintiff', #AcqInc
			   47: 'Rival Intern', #AcqInc
			   48: 'Haunted One', #CoS
			   49: 'Black Fist Double Agent', #CoS-AL
			   50: 'Dragon Casualty', #CoS-AL
			   51: 'Iron Route Bandit', #CoS-AL
			   52: 'Phlan Insurgent', #CoS-AL
			   53: 'Stojanow Prisoner', #CoS-AL
			   54: 'Ticklebelly Nomad', #CoS-AL
			   55: 'Phlan Refugee', #EE-AL
			   56: 'Clasp Member', #Taldorei
			   57: 'Lyceum Student', #Taldorei
			   58: 'Ashari', #Taldorei
			   59: 'Recovered Cultist', #Taldorei
			   60: 'Fate-Touched', #Taldorei
}

bgFeature = [ 'Cult of the Dragon Infiltrator', #HoTDQ
			  'Dragon Scholar', #HoTDQ
			  'Deep Delver', #OoTA
			  'Underdark Experience', #OoTA
]

factions = { 0: 'The Lords\' Alliance',
			 1: 'The Emerald Enclave',
			 2: 'The Order of the Gauntlet',
			 3: 'The Zhentarim',
			 4: 'The Harpers',
			 5: 'Ytepka Society',
			 6: 'Flaming Fist',
			 7: 'Company of the Yellow Banner',
			 8: 'Red Wizards of Thay',
			 9: 'Arcane Brotherhood',
}


racialScores = { 'Mountain Dwarf': 'Str + 2, Con +2',
				 'Hill Dwarf': 'Wis + 1, Con +2',
				 'Duergar': 'Str +1, Con + 2',
				 'High Elf': 'Int +1, Dex +2',
				 'Wood Elf': 'Wis + 1, Dex +2',
				 'Drow': 'Cha +1, Dex +2',
				 'Eladrin': 'Cha +1, Dex +2',
				 'Shadar-Kai': 'Con +1, Dex +2',
				 'Sea Elf': 'Con +1, Dex +2',
				 'Lightfoot Halfling': 'Cha +1, Dex +2',
				 'Stout Halfling': 'Con +1, Dex +2',
				 'Ghostwise Halfling': 'Wis +1, Dex +2',
				 'Human': '2 different ability scores of your choice get +1',
				 'Black Dragonborn': 'Str +2, Cha +1',
				 'Blue Dragonborn': 'Str +2, Cha +1',
				 'Brass Dragonborn': 'Str +2, Cha +1',
				 'Bronze Dragonborn': 'Str +2, Cha +1',
				 'Copper Dragonborn': 'Str +2, Cha +1',
				 'Gold Dragonborn': 'Str +2, Cha +1',
				 'Green Dragonborn': 'Str +2, Cha +1',
				 'Red Dragonborn': 'Str +2, Cha +1',
				 'Silver Dragonborn': 'Str +2, Cha +1',
				 'White Dragonborn': 'Str +2, Cha +1',
				 'Forest Gnome': 'Dex +1, Int +2',
				 'Rock Gnome': 'Con +1, Int +2',
				 'Deep Gnome': 'Dex +1, Int +2',
				 'Half-Elf of Drow descent': 'Cha +2, 2 other ability scores of your choice get +1',
				 'Half-Elf of High descent': 'Cha +2, 2 other ability scores of your choice get +1',
				 'Half-Elf of Wood descent': 'Cha +2, 2 other ability scores of your choice get +1',
				 'Half-Elf of Aquatic descent': 'Cha +2, 2 other ability scores of your choice get +1',
				 'Half-Orc': 'Str +2, Con +1',
				 'Tiefling': 'Int +1, Cha +2',
				 'Earth Genasi': 'Str +1, Con +2',
				 'Water Genasi': 'Wis +1, Con +2',
				 'Air Genasi': 'Dex +1, Con +2',
				 'Fire Genasi': 'Int +1, Con +2',
				 'Githzerai': 'Wis +2, Int +1',
				 'Githyanki': 'Str +2, Int +1',
				 'Aarakocra': 'Wis +1, Dex +2',
				 'Goliath': 'Str +2, Con +1',
				 'Tortle': 'Wis +1, Str +2',
				 'Protector Aasimar': 'Wis +1, Cha +2',
				 'Scourge Aasimar': 'Con +1, Cha +2',
				 'Fallen Aasimar': 'Str +1, Cha +2',
				 'Firbolg': 'Wis +2, Str +1',
				 'Kenku': 'Wis +1, Dex +2',
				 'Lizardfolk': 'Wis +1, Con +2',
				 'Tabaxi': 'Cha +1, Dex +2',
				 'Triton': 'Str +1, Con +1, Cha +1',
				 'Bugbear': 'Str +2, Dex +1',
				 'Goblin': 'Dex +2, Con +1',
				 'Hobgoblin': 'Con +2, Int +1',
				 'Kobold': 'Dex +2, Str -2',
				 'Orc': 'Str +2, Con +1, Int -2',
				 'Yuan-Ti Pureblood': 'Cha +2, Int +1',
				 'Grung': 'Con +1, Dex +2',
				 'Minotaur': 'Str +2, Con +1',
				 'Centaur': 'Str +2, Wis +1',
				 'Half-Halfling / Quarter-Orc': 'Str +1, Dex +1',
				 'Half-Halfling / Quarter-Elf': 'Dex +1, +1 to any other ability score',
				 'Half-Halfling / Half-Tiefling': 'Cha +1, Dex+1',
				 'Half-Halfling / Half-Orc': 'Str +1, Dex +1',
				 'Half-Halfling / Half-Dragonborn': 'Dex +1, Con +1',
				 'Half-Halfling / Half-Tortle': 'Con +1, Dex +1',
				 'Half-Halfling / Half-Kobold': 'Str -2, Dex +2, Wis +1',
				 'Half-Halfling / Half-Kenku': 'Wis +1, Dex +1',
				 'Half-Halfling / Half-Dwarf': 'Con +1, Dex +1',
				 'Half-Halfling / Half-Goblin': 'Dex +1, Con +1',
				 'Half-Halfling / Half-Tabaxi': 'Dex +1, Cha +1',
				 'Half-Halfling / Half-Bugbear': 'Str +1, Dex +1',
				 'Half-Halfling / Half-Aasimar': 'Cha +1, Dex +1',
				 'Awakened Undead': 'Con +2, Dex +1',
				 'Verdan': 'Cha +2, Con +1',
				 'Loxodon': 'Con +2, Wis +1',
				 'Vedalken': 'Int +2, Wis +1',
				 'Envoy Warforged': 'Con +1, 2 other ability scores of your choice get +1',
				 'Juggernaut Warforged': 'Str +2, Con +1',
				 'Skirmisher Warforged': 'Dex +2, Con +1',
				 'Changeling': 'Cha +2, either +1 Dex or +1 Int',
				 'Longtooth Shifter': 'Str +2, Dex +1',
				 'Beasthide Shifter': 'Con +2, Dex +1',
				 'Swiftstride Shifter': 'Dex +2, Cha +1',
				 'Wildhunt Shifter': 'Wis +2, Dex +1',
				 'Kalashtar': 'Wis +1, Cha +1, +1 to any other ability score',
}

racials = { 'Mountain Dwarf': '\n\t- Darkvision (60ft), \n\t- Dwarven Resilience, \n\t- Dwarven Combat Training, \n\t- 1 Tool Proficiency from: (smith\'s tools, brewer\'s tools, mason\'s tools), \n\t- Stonecunning, \n\t- Dwarven Armor Training, \n\t- Languages: Dwarven, Common',
			'Hill Dwarf': '\n\t- Darkvision (60ft), \n\t- Dwarven Resilience, \n\t- Dwarven Combat Training, \n\t- 1 Tool Proficiency from: (smith\'s tools, brewer\'s tools, mason\'s tools), \n\t- Stonecunning, \n\t- Dwarven Toughness, \n\t- Languages: Dwarven, Common',
			'Duergar': '\n\t- Superior Darkvision (120ft), \n\t- Duergar Resilience, \n\t- Sunlight Sensitivity, \n\t- Duergar Magic (INT): Enlarge/Reduce (@ 3rd level), Invisibility (@ 5th level), \n\t  these recharge after a long rest, \n\t- Languages: Undercommon, Dwarven, Common',
			'High Elf': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Elf Weapon Training, Cantrip (INT) Wizard Spell List), \n\t- Languages: Elven, Common, +1 Additional',
			'Wood Elf': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Elf Weapon Training, \n\t- Fleet of Foot (35 ft movement), \n\t- Mark of the Wild, \n\t- Languages: Elven, Common',
			'Drow': '\n\t- Superior Darkvision (120ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Drow Weapon Training, \n\t- Sunlight Sensitivity, \n\t- Drow Magic (CHA): Dancing Lights (@ 3rd level), Darkness (@ 5th level), these recharge after a long rest, \n\t- Languages: Elven, Common, Undercommon',
			'Eladrin': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Fey Step, \n\t- Languages: Elven, Common',
			'Shadar-Kai': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Necrotic Resistance, \n\t- Blessing of the Raven Queen, \n\t- Languages: Elven, Common',
			'Sea Elf': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Fey Ancestry, \n\t- Trance, \n\t- Sea Elf Training, \n\t- Child of the Sea, \n\t- Friend of the Sea, \n\t- Languages: Elven, Common, Aquan',
			'Lightfoot Halfling': '\n\t- Lucky, \n\t- Brave, \n\t- Halfling Nimbleness, \n\t- Naturally Stealthy, \n\t- Languages: Halfling, Common',
			'Stout Halfling': '\n\t- Lucky, \n\t- Brave, \n\t- Halfling Nimbleness, \n\t- Stout Resilience, \n\t- Languages: Halfling, Common',
			'Ghostwise Halfling': '\n\t- Lucky, \n\t- Brave, \n\t- Halfling Nimbleness, \n\t- Silent Speech, \n\t- Languages: Halfling, Common',
			'Human': '\n\t- One feat of your choice, \n\t- One skill proficiency of your choice, \n\t- Languages: Common, +1 Additional',
			'Black Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Acid), \n\t- Damage Resistance (Acid), \n\t- Languages: Draconic, Common',
			'Blue Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Lightning), \n\t- Damage Resistance (Lightning), \n\t- Languages: Draconic, Common',
			'Brass Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Fire), \n\t- Damage Resistance (Fire), \n\t- Languages: Draconic, Common',
			'Bronze Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Lightning), \n\t- Damage Resistance (Lightning), \n\t- Languages: Draconic, Common',
			'Copper Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Acid), \n\t- Damage Resistance (Acid), \n\t- Languages: Draconic, Common',
			'Gold Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Fire), \n\t- Damage Resistance (Fire), \n\t- Languages: Draconic, Common',
			'Green Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Poison), \n\t- Damage Resistance (Poison), \n\t- Languages: Draconic, Common',
			'Red Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Fire), \n\t- Damage Resistance (Fire), \n\t- Languages: Draconic, Common',
			'Silver Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Cold), \n\t- Damage Resistance (Cold), \n\t- Languages: Draconic, Common',
			'White Dragonborn': '\n\t- Draconic Ancestry, \n\t- Breath Weapon (Cold), \n\t- Damage Resistance (Cold), \n\t- Languages: Draconic, Common',
			'Forest Gnome': '\n\t- Darkvision (60ft), \n\t- Gnome Cunning, \n\t- Natural Illusionist, \n\t- Speak with Small Beasts, \n\t- Languages: Gnomish, Common',
			'Rock Gnome': '\n\t- Darkvision (60ft), \n\t- Gnome Cunning, \n\t- Artificer\'s Lore, \n\t- Tinker, \n\t- Languages: Gnomish, Common',
			'Deep Gnome': '\n\t- Superior Darkvision (120ft), \n\t- Gnome Cunning, \n\t- Stone Camoflague, \n\t- Languages: Gnomish, Common, Undercommon',
			'Half-Elf of Drow descent': '\n\t- Darkvision (60ft), \n\t- Fey Ancestry, \n\t- Skill Versatility or Drow Magic, \n\t- Languages: Common, Elven, +1 Additional',
			'Half-Elf of High descent': '\n\t- Darkvision (60ft), \n\t- Fey Ancestry, \n\t- Skill Versatility or either Elf Weapon Training or Cantrip, \n\t- Languages: Common, Elven, +1 Additional',
			'Half-Elf of Wood descent': '\n\t- Darkvision (60ft), \n\t- Fey Ancestry, \n\t- Skill Versatility or either Elf Weapon Training, Fleet of Foot, or Mask of the Wild, \n\t- Languages: Common, Elven, +1 Additional',
			'Half-Elf of Aquatic descent': '\n\t- Darkvision (60ft), \n\t- Fey Ancestry, \n\t- Skill Versatility or a swimming speed of 30ft, \n\t- Languages: Common, Elven, +1 Additional',
			'Half-Orc': '\n\t- Darkvision (60ft), \n\t- Menacing, \n\t- Relentless Endurance, \n\t- Savage Attacks, \n\t- Languages: Common, Orc',
			'Tiefling': '\n\t- Darkvision (60ft), \n\t- Hellish Resistance, \n\t- Infernal Legacy, \n\t- Languages: Infernal, Common',
			'Earth Genasi': '\n\t- Earth Walk, \n\t- Merge with Stone, \n\t- Languages: Primordial, Common',
			'Water Genasi': '\n\t- Acid Resistance, \n\t- Amphibious, \n\t- Swim Speed (30ft),\n\t- Call to the Wave, \n\t- Languages: Primordial, Common',
			'Air Genasi': '\n\t- Unending Breath, \n\t- Mingle with the Wind, \n\t- Languages: Primordial, Common',
			'Fire Genasi': '\n\t- Darkvision (60ft), \n\t- Fire Resistance, \n\t- Reach to the Blaze, \n\t- Languages: Primordial, Common',
			'Githyanki': '\n\t- Decadent Mastery, \n\t- Martial Prodigy, \n\t- Githyanki Psionics (INT): Jump (@ 3rd level), Misty Step (@ 5th level), \n\t these recharge after a long rest, \n\t- Languages: Gith, Common, +1 Additional',
			'Githzerai': '\n\t- Mental Discipline, \n\t- Githzerai Psionics (WIS): Shield (@ 3rd level), Detect Thoughts (@ 5th level), \n\t these recharge after a long rest, \n\t- Languages: Gith, Common',
			'Aarakocra': '\n\t- Flight (50ft), \n\t- Talons (1d4), \n\t- Languages: Auran, Aarakocra, Common',
			'Goliath': '\n\t- Natural Athlete, \n\t- Stone\'s Endurance, \n\t- Powerful Build, \n\t- Mountain Born, \n\t- Languages: Common, Giant',
			'Tortle': '\n\t- Claws (1d4), \n\t- Hold Breath, \n\t- Natural Armor, \n\t- Shell Defense, \n\t- Survival Instinct, \n\t- Languages: Aquan, Common',
			'Protector Aasimar': '\n\t- Darkvision (60ft), \n\t- Celestial Resistance, \n\t- Healing Hands, \n\t- Light Bearer, \n\t- Radiant Soul, \n\t- Languages: Common, Celestial',
			'Scourge Aasimar': '\n\t- Darkvision (60ft), \n\t- Celestial Resistance, \n\t- Healing Hands, \n\t- Light Bearer, \n\t- Radiant Consumption, \n\t- Languages: Common, Celestial',
			'Fallen Aasimar': '\n\t- Darkvision (60ft), \n\t- Celestial Resistance, \n\t- Healing Hands, \n\t- Light Bearer, \n\t- Necrotic Shroud, \n\t- Languages: Common, Celestial',
			'Firbolg': '\n\t- Firbolg Magic (WIS): detect magic, disguise self, these recharge after a short or long rest, \n\t- Hidden Step, \n\t- Powerful Build, \n\t- Speech of Beast and Leaf, \n\t- Languages: Common, Elvish, Giant',
			'Kenku': '\n\t- Expert Forgery, \n\t- Kenku Training, \n\t- Mimicry, \n\t- Languages: Common, Auran (can only speak using mimicry)',
			'Lizardfolk': '\n\t- Bite (1d6), \n\t- Cunning Artisan, \n\t- Hold Breath, \n\t- Hunter\'s Lore, \n\t- Natural Armor, \n\t- Hungry Jaws, \n\t- Languages: Draconic, Common',
			'Tabaxi': '\n\t- Darkvision (60ft), \n\t- Feline Agility, \n\t- Cat\'s Claws (1d4 & climb (20ft) ), \n\t- Cat\'s Talent, \n\t- Languages: Common, +1 Additional',
			'Triton': '\n\t- Amphibious, \n\t- Control Air and Water, \n\t- Emissary of the Sea, \n\t- Guardians of the Depths, \n\t- Languages: Common, Primordial',
			'Bugbear': '\n\t- Darkvision (60ft), \n\t- Long-Limbed, \n\t- Powerful Build, \n\t- Sneaky, \n\t- Surprise Attack, \n\t- Languages: Common, Goblin',
			'Goblin': '\n\t- Darkvision (60ft), \n\t- Fury of the Small, \n\t- Nimble Escape, \n\t- Languages: Common, Goblin',
			'Hobgoblin': '\n\t- Darkvision (60ft), \n\t- Martial Training, \n\t- Saving Face, \n\t- Languages: Common, Goblin',
			'Kobold': '\n\t- Darkvision (60ft), \n\t- Grovel, Cower, and Beg, \n\t- Pack Tactics, \n\t- Sunlight Sensitivity, \n\t- Languages: Common, Draconic',
			'Orc': '\n\t- Darkvision (60ft), \n\t- Aggressive, \n\t- Menacing, \n\t- Powerful Build, \n\t- Languages: Common, Orc',
			'Yuan-Ti Pureblood': '\n\t- Darkvision (60ft), \n\t- Innate Spellcasting (CHA): Poison Spray, Animal Friendship (snakes), \n\tSuggestion (@ 3rd level), suggestion recharges after a long rest, \n\t- Magic Resistance (ADV on saves against spells and other magical effects), \n\t- Poison Immunity, \n\t- Languages: Common, Abyssal, Draconic',
			'Grung': '\n\t- Arboreal Alertness, \n\t- Amphibious, \n\t- Poison Immunity, \n\t- Poisonous Skin, \n\t- Standing Leap, \n\t- Water Dependency, \n\t- Languages: Grung',
			'Minotaur': '\n\t- Horns (1d6), \n\t- Goring Rush, \n\t- Hammering Horns, \n\t- Imposing Presence, \n\t- Languages: Common, Minotaur',
			'Centaur': '\n\t- Speed: 40ft, \n\t- Fey, \n\t- Charge, \n\t- Hooves (1d4), \n\t- Equine Build, \n\t- Survivor, \n\t- Languages: Common, Sylvan',
			'Awakened Undead': '\n\t- Darkvision (60ft), \n\t- Deadman\'s Respite, \n\t- Grim Fortitude, \n\t- Grave Touched, \n\t- Languages: Common \n\t- Located at: \n\t\thttps://www.dndbeyond.com/characters/races/88796-awakened-undead-v-4 \n\t\thttps://www.dndbeyond.com/characters/races/XXX',
			'Half-Halfling / Half-Dragonborn': '\n\t- Stout Resilience, \n\t- Brave, \n\t- Breath Weapon, \n\t- Damage Resistance, \n\t- Languages: Common, Halfling, Draconic',
			'Half-Halfling / Half-Kobold': '\n\t- Halfling Nimbleness, \n\t- Darkvision (30ft), \n\t- Pack Tactics, \n\t- Languages: Common, Halfling, Draconic',
			'Half-Halfling / Half-Tortle': '\n\t- Brave, \n\t- Hold Breath, \n\t- Claws (1d4 slashing), \n\t- Survival Instinct, \n\t- Languages: Common, Halfling, Aquan',
			'Half-Halfling / Half-Tiefling': '\n\t- Brave, \n\t- Hellish Resistance, \n\t- Infernal Legacy (Thurmaturgy, @ 3rd level you get Hellish Rebuke), \n\t- Languages: Common, Halfling, Infernal',
			'Half-Halfling / Half-Orc': '\n\t- Brave, \n\t- Aggressive, \n\t- Powerful Build, \n\t- Speed (30 ft), \n\t- Languages: Common, Halfling, Orc',
			'Half-Halfling / Quarter-Orc': '\n\t- Halfling Nimbleness, \n\t- Darkvision (30 ft), \n\t- Relentless Endurance, \n\t- Languages: Common, Halfling, Orc',
			'Half-Halfling / Quarter-Elf': '\n\t- Lucky, \n\t- Darkvision (30ft), \n\t- Fey Ancestry, \n\t- Languages: Common, Halfling, Elven, +1 Additional',
			'Half-Halfling / Half-Kenku': '\n\t- Halfling Nimbleness, \n\t- Kenku Training, \n\t- Expert Forgery, \n\t- Languages: Common, Halfling, Auran',
			'Half-Halfling / Half-Dwarf': '\n\t- Brave, \n\t- Halfling Nimbleness, \n\t- Darkvision (30ft), \n\t- Dwarven Resilience, \n\t- Dwarven Combat Training, \n\t- Languages: Common, Halfling, Dwarven',
			'Half-Halfling / Half-Goblin': '\n\t- Halfling Nimbleness, \n\t- Fury of the Small, \n\t- Darkvision (30 ft), \n\t- Languages: Common, Halfling, Goblin',
			'Half-Halfling / Half-Tabaxi': '\n\t- Halfling Nimbleness, \n\t- Feline Agility, \n\t- Darkvision (30ft), \n\t- Cat\'s Claws (1d4 & 20ft Climbing speed), \n\t- Languages: Common, Halfling, +1 Additional',
			'Half-Halfling / Half-Bugbear': '\n\t- Naturally Stealthy, \n\t- Sneaky, \n\t- Surprise Attack, \n\t- Languages: Common, Halfling, Goblin',
			'Half-Halfling / Half-Aasimar': '\n\t- Brave, \n\t- Darkvision (30 ft), \n\t- Celestial Resistance, \n\t- Healing Hands, \n\t- Languages: Common, Halfling, Celestial',
			'Verdan': '\n\t- Black Blood Healing, \n\t- Limited Telepathy, \n\t- Persuasive, \n\t- Telepathic Insight\n\t- Languages: Common, Goblin, +1 Additional', #Acq Inc p.74
			'Vedalken': '\n\t- Vedalken Dispassion, \n\t- Tireless Precision, \n\t- Partially Amphibious, \n\t- Languages:  Common, Vedalken, +1 Additional',
			'Loxodon': '\n\t- Powerful Build, \n\t- Loxodon Serentiy, \n\t- Natural Armor, \n\t- Trunk, \n\t- Keen Smell, \n\t- Languages: Common, Loxodon',
			'Changeling': '\n\t- Change Appearance, \n\t- Changeling Instincts, \n\t- Unsettling Visage, \n\t- Divergent Persona, \n\t- Languages: Common, +2 Additional',
			'Kalashtar': '\n\t- Dual Mind, \n\t- Mental Discipline, \n\t- Mind Link, \n\t- Psychic Glamour, \n\t- Severed from Dreams, \n\t- Languages: Common, Quori, +1 Additional',
			'Beasthide Shifter': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Shifting, \n\t- Tough, \n\t- Shifting Feature (+1d6 temp HP, +1 AC), \n\t- Languages: Common',
			'Longtooth Shifter': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Shifting, \n\t- Fierce, \n\t- Shifting Feature (use fangs for unarmed strike (1d6 + str piercing dmg)), \n\t- Languages: Common',
			'Swiftstride Shifter': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Shifting, \n\t- Graceful, \n\t- Swift Stride (+5 ft speed), \n\t- Shifting Feature (walk speed +5 ft, move 10 ft as reaction if enemy w/in 5ft), \n\t- Languages: Common',
			'Wildhunt Shifter': '\n\t- Darkvision (60ft), \n\t- Keen Senses, \n\t- Shifting, \n\t- Natural Tracker, \n\t- Mark the Scent, \n\t- Shifting Feature (ADV on WIS saves), \n\t- Languages: Common',
			'Envoy Warforged': '\n\t- Warforged Resilience, \n\t- Sentry\'s Rest, \n\t- Integrated Protection, \n\t- Specialized Design, \n\t- Integrated Tool, \n\t- Languages: Common',
			'Juggernaut Warforged': '\n\t- Warforged Resilience, \n\t- Sentry\'s Rest, \n\t- Integrated Protection, \n\t- Iron Fists (1d4 + Str), \n\t- Powerful Build, \n\t- Languages: Common',
			'Skirmisher Warforged': '\n\t- Warforged Resilience, \n\t- Sentry\'s Rest, \n\t- Integrated Protection, \n\t- Swift (+10 ft speed), \n\t- Light Step, \n\t- Languages: Common',
}

classAbilities = { 'Barbarian - Ancestral Guardian': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Ancestral Protectors',
				   'Barbarian - Battlerager': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Battlerager Armor',
				   'Barbarian - Berserker': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Frenzy',
				   'Barbarian - Storm Herald': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Storm Aura (Desert, Sea, Tundra)',
				   'Barbarian - Totem Warrior': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Spirit Seeker, \n\t- Totem Spirit (Bear, Eagle, Wolf, Elk, Tiger)',
				   'Barbarian - Zealot': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Divine Fury, \n\t- Warrior of the Gods',
				   'Barbarian - Wild Soul': '\n\t- Rage (3 / +2), \n\t- Unarmored Defense, \n\t- Reckless Attack, \n\t- Danger Sense, \n\t- Lingering Magic, \n\t- Wild Surge',
				   'Bard - Glamour': '\n\t- Spellcasting (CHA), \n\t- Bardic Inspiration (d6), \n\t- Jack of All Trades, \n\t- Song of Rest (d6), \n\t- Expertise, \n\t- Mantle of Inspiration, \n\t- Entralling Performance',
				   'Bard - Swords': '\n\t- Spellcasting (CHA), \n\t- Bardic Inspiration (d6), \n\t- Jack of All Trades, \n\t- Song of Rest (d6), \n\t- Expertise, \n\t- Bonus Proficiencies (Med Armor, Scimitar), \n\t- Fighting Style (Dueling, Two Weapon Fighting), \n\t- Blade Flourish (Defensive Flourish, Slashing Flourish, Mobile Flourish)',
				   'Bard - Lore': '\n\t- Spellcasting (CHA), \n\t- Bardic Inspiration (d6), \n\t- Jack of All Trades, \n\t- Song of Rest (d6), \n\t- Expertise, \n\t- Bonus Proficiencies (+3 Skills), \n\t- Cutting Words',
				   'Bard - Valor': '\n\t- Spellcasting (CHA), \n\t- Bardic Inspiration (d6), \n\t- Jack of All Trades, \n\t- Song of Rest (d6), \n\t- Expertise, \n\t- Bonus Proficiencies (Med Armor, shields, & martial weapons), \n\t- Combat Inspiration',
				   'Bard - Whispers': '\n\t- Spellcasting (CHA), \n\t- Bardic Inspiration (d6), \n\t- Jack of All Trades, \n\t- Song of Rest (d6), \n\t- Expertise, \n\t- Psychic Blades, \n\t- Words of Terror',
				   'Cleric - Forge Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiencies (Heavy Armor, Smith\'s Tools), \n\t- Blessing of the Forge, \n\t- Channel Divinity (Artisan\'s Blessing)',
				   'Cleric - Life Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiency (Heavy Armor), \n\t- Disciple of Life, \n\t- Channel Divinity (Preserve Life)',
				   'Cleric - Grave Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Circle of Mortality, \n\t- Eyes of the Grave, \n\t- Channel Divinity (Path to the Grave)',
				   'Cleric - Tempest Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiencies (Martial Weapons & Heavy Armor), \n\t- Wrath of the Storm, \n\t- Channel Divinity (Destructive Wrath)',
				   'Cleric - Trickery Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Blessing of the Trickster, \n\t- Channel Divinity (Invoke Duplicity)',
				   'Cleric - Death Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiency (Martial Weapons), \n\t- Reaper, \n\t- Channel Divinity (Touch of Death)',
				   'Cleric - Arcana Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Arcane Initiate (Prof. in Arcana, +2 cantrips), \n\t- Channel Divinity (Arcane Abjuration)',
				   'Cleric - Knowledge Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Blessings of Knowledge, \n\t- Channel Divinity (Knowledge Through the Ages)',
				   'Cleric - Light Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Cantrip, \n\t- Warding Flame, \n\t- Channel Divinity (Radiance of the Dawn)',
				   'Cleric - Nature Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Acolyte of Nature, \n\t- Bonus Proficiency (Heavy Armor), \n\t- Channel Divinity (Charm Animals and Plants)',
				   'Cleric - War Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiencies (Martial Weapons & Heavy Armor), \n\t- War Priest, \n\t- Channel Divinity (Guided Strike)',
				   'Cleric - Order Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiencies (Heavy Armor & either Intimidation or Persuasion Skill), \n\t- Voice of Authority, \n\t- Channel Divinity (Order\'s Demand)',
				   'Cleric - Blood Domain': '\n\t- Spellcasting (WIS), \n\t- Channel Divinity (Turn Undead), \n\t- Bonus Proficiencies (Martial Weapons), \n\t- Bloodletting Focus, \n\t- Channel Divinity (Blood Puppet)',
				   'Druid - Dreams': '\n\t- Druidic (Language: Druidic), \n\t- Spellcasting (WIS), \n\t- Wild Shape (1/4 CR, No Flying or Swimming), \n\t- Balm of the Summer Court',
				   'Druid - Land': '\n\t- Druidic (Language: Druidic), \n\t- Spellcasting (WIS), \n\t- Wild Shape (1/4 CR, No Flying or Swimming), \n\t- Bonus Cantrip, \n\t- Natural Recovery, \n\t- Circle Spells (Arctic, Coast, Desert, Forest, Grassland, Mountain, Swamp, Underdark)',
				   'Druid - Moon': '\n\t- Druidic (Language: Druidic), \n\t- Spellcasting (WIS), \n\t- Wild Shape (1/4 CR, No Flying or Swimming), \n\t- Combat Wild Shape, \n\t- Circle Forms (Wild Shape 1 CR)',
				   'Druid - Shepherd': '\n\t- Druidic (Language: Druidic), \n\t- Spellcasting (WIS), \n\t- Wild Shape (1/4 CR, No Flying or Swimming), \n\t- Speech of the Woods, \n\t- Spirit Totem (Bear Spirit, Hawk Spirit, Unicorn Spirit)',
				   'Druid - Spores': '\n\t- Druidic (Language: Druidic), \n\t- Spellcasting (WIS), \n\t- Wild Shape (1/4 CR, No Flying or Swimming), \n\t- Halo of Spores, \n\t- Symbiotic Entity',
				   'Fighter - Arcane Archer': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Arcane Archer Lore, \n\t- Arcane Shot (2 options)',
				   'Fighter - Battle Master': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Combat Superiority (3 Manuevers, 4 Superiority Dice), \n\t- Student of War',
				   'Fighter - Brute': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Brute Force',
				   'Fighter - Cavalier': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Bonus Proficiency (Animal Handling, History, Insight, Performance, or Persuasion. Or learn 1 Language), \n\t- Born to the Saddle, \n\t- Unwavering Mark',
				   'Fighter - Champion': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Improved Critical',
				   'Fighter - Eldritch Knight': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Spellcasting (INT), \n\t- Weapon Bond',
				   'Fighter - Purple Dragon Knight': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Rallying Cry',
				   'Fighter - Samurai': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Bonus Proficiency (History, Insight, Performance, or Persuasion), \n\t- Fighting Spirit',
				   'Fighter - Scout': '\n\t- Second Wind, \n\t- Action Surge, \n\t- Bonus Proficiency (3 skills from: below) \n\t\t~ Acrobatics, Athletics, Investigation, Medicine, Nature, Perception, Stealth, or Survival), \n\t- Combat Superiority (4 superiority dice), \n\t- Natural Explorer',
				   'Monk - Drunken Master': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Bonus Proficiencies (Performance, Brewer\'s Tools), \n\t- Drunken Technique',
				   'Monk - Four Elements': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Disciple of the Elements',
				   'Monk - Kensei': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Path of the Kensei',
				   'Monk - Long Death': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Touch of Death',
				   'Monk - Open Hand': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Way of the Open Hand',
				   'Monk - Shadow': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Shadow Arts',
				   'Monk - Sun Soul': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Radiant Sun Bolt',
				   'Monk - Tranquility': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Healing Hands',
				   'Monk - Cobalt Soul': '\n\t- Unarmored Defense, \n\t- Martial Arts (d4), \n\t- Ki (3 points), \n\t- Unarmored Movement (10 ft), \n\t- Deflect Missiles, \n\t- Mystical Erudition, \n\t- Extract Aspects',
				   'Paladin - Conquest': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Conquering Presence), \n\t- Channel Divinity (Guided Strike)',
				   'Paladin - Vengeance': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Abjure Enemy), \n\t- Channel Divinity (Vow of Enmity)',
				   'Paladin - Redemption': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Emissary of Peace), \n\t- Channel Divinity (Rebuke the Violent)',
				   'Paladin - Ancients': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Nature\'s Wrath), \n\t- Channel Divinity (Turn the Faithless)',
				   'Paladin - Crown': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Champion Challenge), \n\t- Channel Divinity (Turn the Tide)',
				   'Paladin - Devotion': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Sacred Weapon), \n\t- Channel Divinity (Turn the Unholy)',
				   'Paladin - Oathbreaker': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Control Undead), \n\t- Channel Divinity (Dreadful Aspect)',
				   'Paladin - Secrets': '\n\t- Divine Sense, \n\t- Lay on Hands, \n\t- Spellcasting (CHA), \n\t- Divine Smite, \n\t- Divine Health, \n\t- Channel Divinity (Keep Secrets), \n\t- Channel Divinity (Learn Secrets)',
				   'Ranger - Beast Master': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, \n\t- Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Ranger\'s Companion',
				   'Ranger - Hunter': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, \n\t- Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Hunter\'s Prey',
				   'Ranger - Monster Slayer': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, \n\t- Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Monster Slayer Magic, \n\t- Hunter\'s Sense, \n\t- Slayer\'s Prey',
				   'Ranger - Gloom Stalker': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, \n\t- Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Gloom Stalker Magic, \n\t- Dread Ambusher, \n\t- Umbral Sight',
				   'Ranger - Horizon Walker': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, \n\t- Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Horizon Walker Magic, \n\t- Detect Portal, \n\t- Planar Warrior (1d8)',
				   'Ranger - UA': '\n\t- Favored Enemy (beasts, fey, humanoids, monstrosities, or undead), \n\t- Natural Explorer, \n\t- Fighting Style, Spellcasting (WIS), \n\t- Primeval Awareness, \n\t- Ranger Conclave (Beast, Hunter, or Stalker), \n\t- Ranger Conclave ability',
				   'Rogue - Arcane Trickster': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Spellcasting (INT), \n\t- Mage Hand Legerdemain',
				   'Rogue - Thief': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Fast Hands, \n\t- Second-Story Work',
				   'Rogue - Assassin': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Bonus Proficiencies (Disguise Kit & Poisoner\'s Kit), \n\t- Assassinate',
				   'Rogue - Mastermind': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Master of Intrigue, \n\t- Master of tactics',
				   'Rogue - Scout': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Skirmisher, \n\t- Survivalist',
				   'Rogue - Inquisitive': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Ear for Deceit, \n\t- Eye for Detail, \n\t- Insightful Fighting',
				   'Rogue - Swashbuckler': '\n\t- Expertise, \n\t- Sneak Attack (2d6), \n\t- Thieves\' Cant, \n\t- Cunning Action, \n\t- Fancy Footwork, \n\t- Rakish Audacity',
				   'Sorcerer - Divine Soul': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Divine Magic, \n\t- Favored by the Gods',
				   'Sorcerer - Draconic Bloodline': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Dragon Ancestor, \n\t- Draconic Resilience',
				   'Sorcerer - Shadow Magic': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Eyes of the Dark (Darkvision 120ft), \n\t- Strength of the Grave',
				   'Sorcerer - Storm Sorcery': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Wind Speaker (Language: Primordial), \n\t- Tempestuous Magic',
				   'Sorcerer - Wild Magic': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Wild Magic Surge, \n\t- Tides of Chaos',
				   'Sorcerer - Phoenix Sorcery': '\n\t- Spellcasting (WIS), \n\t- Font of Magic (3 Sorcery points, Flexible Casting), \n\t- Metamagic (2 choices), \n\t- Ignite, \n\t- Mantle of Flame',
				   'Warlock - The Archfey': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Fey Presence',
				   'Warlock - The Celestial': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Bonus Cantrips (Light & Sacred Flame), \n\t- Healing Light',
				   'Warlock - The Fiend': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Dark One\'s Blessing',
				   'Warlock - The Great Old One': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Awakened Mind',
				   'Warlock - The Hexblade': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Hexblade\'s Curse, \n\t- Hex Warrior',
				   'Warlock - The Undying': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Among the Dead',
				   'Warlock - The Noble Genie': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Noble Patronage (Language: Primordial), \n\t- Gen Vizier (Spell Fetching - 1d12)',
				   'Warlock - The Chaos Walker': '\n\t- Pact Magic (CHA), \n\t- Eldritch Invocations (2), \n\t- Pact Boon (Pact of the Chain, Blade, or Tome), \n\t- Strings Attached',
				   'Wizard - Artificer': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Infuse Potions, \n\t- Infuse Scrolls',#Eberron UA / might be in the dms guild
				   'Wizard - Bladesinger': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Training in War and Song (Proficiency in Light Armor, a 1H weapon of choice, and Performance skill), \n\t- Bladesong',
				   'Wizard - Abjuration': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Abjuration Savant, \n\t- Arcane Ward',
				   'Wizard - Conjuration': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Conjuration Savant, \n\t- Minor Conjuration',
				   'Wizard - Divination': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Divination Savant, \n\t- Portent',
				   'Wizard - Enchantment': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Enchantment Savant, \n\t- Hypnotic Gaze',
				   'Wizard - Evocation': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Evocation Savant, \n\t- Sculpt Spells',
				   'Wizard - Illusion': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Illusion Savant, \n\t- Improved Minor Illusion',
				   'Wizard - Necromancy': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Necromancy Savant, \n\t- Grim Harvest',
				   'Wizard - Transmutation': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Transmutation Savant, \n\t- Minor Alchemy',
				   'Wizard - War Magic': '\n\t- Spellcasting (INT): Spellbook, Ritual Casting, Spellcasting Focus, \n\t- Arcane Recovery, \n\t- Arcane Deflection, \n\t- Tactical Wit',
				   'Blood Hunter - Mutant': '\n\t- Hunter\'s Bane, \n\t- Crimson Rite (Flame, Frozen, Storm), \n\t- Fighting Style, \n\t- Blood Maledict, \n\t- Formulas (3 Mutagen Formulas), \n\t- Mutagen Craft',
				   'Blood Hunter - Ghostslayer': '\n\t- Hunter\'s Bane, \n\t- Crimson Rite (Flame, Frozen, Storm), \n\t- Fighting Style, \n\t- Blood Maledict, \n\t- Rite of the Dawn',
				   'Blood Hunter - Profane Soul': '\n\t- Hunter\'s Bane, \n\t- Crimson Rite (Flame, Frozen, Storm), \n\t- Fighting Style, \n\t- Blood Maledict, \n\t- Otherworldly Patron, \n\t- Pact Magic, \n\t- Rite Focus',
				   'Artificer - Alchemist': '\n\t- Magical Tinkering, \n\t- Spellcasting (INT) - Tools Required, \n\t- Infuse Item (3 infusions), \n\t- Tool Proficiency, \n\t- Tool Expertise, \n\t- Tools of the Trade, \n\t\t+ Proficiency w/ Alchemist Supplies & Herbalism Kit, \n\t\t+ Crafting potions takes a 1/4 of the time and 1/2 the gold, \n\t- Alchemist Spells (don\'t count against prepared limit), \n\t- Alchemical Homunculus',
				   'Artificer - Artillerist': '\n\t- Magical Tinkering, \n\t- Spellcasting (INT) - Tools Required, \n\t- Infuse Item (3 infusions), \n\t- Tool Proficiency, \n\t- Tool Expertise, \n\t- Tools of the Trade, \n\t\t+ Proficiency w/ Smith\'s Tools & Woodcarver\'s Tools, \n\t\t+ Crafting wands takes 1/4 of the time and 1/2 the gold, \n\t- Artillerist Spells (don\'t count against prepared limit), \n\t- Arcane Turret',
				   'Illrigger - Shadowmaster': '\n\t- Forked Tongue, \n\t- Infernal Conduit, \n\t- Spellcasting (CHA), \n\t- Baleful Interdict, \n\t- Hellsight, \n\t- Knight of Hell (Moloch), \n\t- Invoke Authority (Cloud of Brimstone), \n\t- Invoke Authority (Compel the Graceless)',
				   'Illrigger - Painkiller': '\n\t- Forked Tongue, \n\t- Infernal Conduit, \n\t- Spellcasting (CHA), \n\t- Baleful Interdict, \n\t- Hellsight, \n\t- Knight of Hell (Dispater), \n\t- Invoke Authority (Devastator), \n\t- Invoke Authority (Compel the Weak)',
				   'Illrigger - Architect of Ruin': '\n\t- Forked Tongue, \n\t- Infernal Conduit, \n\t- Spellcasting (CHA), \n\t- Baleful Interdict, \n\t- Hellsight, \n\t- Knight of Hell (Asmodeus), \n\t- Invoke Authority (Infernal Arcanist), \n\t- Invoke Authority (Compel the Cedulous)',
}

acquisitionsJob = [ 'Cartographer',
					'Decisionist',
					'Documancer',
					'Hoardsperson',
					'Loremonger',
					'Obviator',
					'Occultant',
					'Secretarian',
]

acqAbilities = { 'Cartographer': '\n\t- Proficiency with Cartographer\'s Tools and either vehicles (land) or vehicles (water), \n\t- It\'s a Rental',
				 'Decisionist': '\n\t- Proficiency with Musical Instrument (Horn), \n\t- Tiebreaker',
				 'Documancer': '\n\t- Proficiency with Calligrapher\'s Supplies, \n\t- Gift of Words',
				 'Hoardsperson': '\n\t- Proficiency with Jeweler\'s Tools, \n\t- What a Deal',
				 'Loremonger': '\n\t- Proficiency with one of the following: Artisan\'s Tools (choose type), Navigator\'s Tools, vehicles (land), vehicles (water), \n\t- Whisper Jar',
				 'Obviator': '\n\t- Proficiency with Alchemist\'s Supplies, \n\t- Read the Opposition',
				 'Occultant': '\n\t- Proficiency with one of the following: Cook\'s Utensils, Leatherworker\'s Tools, or Weaver\'s Tools, \n\t- Read the Kill',
				 'Secretarian': '\n\t- Proficiency with one of the following: Gaming Set, Musical Instrument, or Disguise Kit, \n\t- Sending Stone',	
}

namePiece = { 0: '',
			  1: '',
			  2: '',
			  3: '',
			  4: '',
			  5: 'a',
			  6: 'be',
			  7: 'de',
			  8: 'el',
			  9: 'fa',
			  10: 'jo',
			  11: 'ki',
			  12: 'la',
			  13: 'ma',
			  14: 'na',
			  15: 'o',
			  16: 'pa',
			  17: 're',
			  18: 'si',
			  19: 'ta',
			  20: 'va',
			  21: 'bar',
			  22: 'ched',
			  23: 'dell',
			  24: 'far',
			  25: 'gran',
			  26: 'hal',
			  27: 'jen',
			  28: 'kel',
			  29: 'lim',
			  30: 'mor',
			  31: 'net',
			  32: 'penn',
			  33: 'quil',
			  34: 'rond',
			  35: 'sark',
			  36: 'shen',
			  37: 'tur',
			  38: 'vash',
			  39: 'yor',
			  40: 'zen',
			  41: 'roy',
			  42: 'oo',
			  43: 'ike',
			  44: 'eve',
			  45: '',
			  46: 'a',
			  47: 'ac',
			  48: 'ai',
			  49: 'al',
			  50: 'am',
			  51: 'an',
			  52: 'ar',
			  53: 'ea',
			  54: 'el',
			  55: 'er',
			  56: 'ess',
			  57: 'ett',
			  58: 'ic',
			  59: 'id',
			  60: 'il',
			  61: 'in',
			  62: 'is',
			  63: 'or',
			  64: 'us',
			  65: 'itt',
			  66: 'go',
			  67: 'gr',
			  68: 'cou',
}

namePiece0 = { 0: 'kah',
			  1: 'jah',
			  2: 'li',
			  3: 'eon',
			  4: 'rah',
			  5: 'wey',
			  6: 'wah',
			  7: 'tar',
			  8: 'an',
			  9: 'ste',
			  10: 'mik',
			  11: 'gi',
			  12: 'jo',
			  13: 'cou',
			  14: 'ro',
			  15: 'i',
			  16: 'rog',
			  17: 'tay',
			  18: 'ire',
			  19: 'oo',
			  20: 'et',
			  21: 'ch',
			  22: 'nat',
			  23: 'din',
}

namePiece1 = { 0: '',
			   1: '',
			   2: '',
			   3: '',
			   4: 'a',
			   5: 'be',
			   6: 'de',
			   7: 'el',
			   8: 'fa',
			   9: 'jo',
			   10: 'ki',
			   11: 'la',
			   12: 'ma',
			   13: 'na',
			   14: 'o',
			   15: 'pa',
			   16: 're',
			   17: 'si',
			   18: 'ta',
			   19: 'va',
}

namePiece2 = { 0: 'bar',
			   1: 'ched',
			   2: 'dell',
			   3: 'far',
			   4: 'gran',
			   5: 'hal',
			   6: 'jen',
			   7: 'kel',
			   8: 'lim',
			   9: 'mor',
			   10: 'net',
			   11: 'penn',
			   12: 'quil',
			   13: 'rond',
			   14: 'sark',
			   15: 'shen',
			   16: 'tur',
			   17: 'vash',
			   18: 'yor',
			   19: 'zen',
}

namePiece3 = { 0: '',
			   1: 'a',
			   2: 'ac',
			   3: 'ai',
			   4: 'al',
			   5: 'am',
			   6: 'an',
			   7: 'ar',
			   8: 'ea',
			   9: 'el',
			   10: 'er',
			   11: 'ess',
			   12: 'ett',
			   13: 'ic',
			   14: 'id',
			   15: 'il',
			   16: 'in',
			   17: 'is',
			   18: 'or',
			   19: 'us',
}

humanFemaleName = [ 'Jayna',
			  		'Ezrie',
			  		'Sabetha',
			  		'Zamira',
			  		'Quinn',
]

humanMaleName = [ 'Caleb',
				  'Caden',
				  'Carlo',
]

humanSurname = [ 'Proudmoore',
				 'Duckett',
				 'Selmy',
				 'Lamora',
				 'Voss',
				 '',
]

uncommonItems = ['Alchemy Jug',
				 'Ammunition +1',
				 'Amulet of Proof Against Detection and Location',
				 'Bag of Holding',
				 'Bag of Tricks',
				 'Boots of Elvenkind',
				 'Boots of Striding and Springing',
				 'Boots of the Winterlands',
				 'Bracers of Archery',
				 'Brooch of Shielding',
				 'Broom of Flying',
				 'Cap of Water Breathing',
				 'Circlet of Blasting',
				 'Cloak of Elvenkind',
				 'Cloak of Protection',
				 'Cloak of the Manta Ray',
				 'Decanter of Endless Water',
				 'Deck of Illusions',
				 'Driftglobe',
				 'Dust of Disappearance',
				 'Dust of Dryness',
				 'Dust of Sneezing and Choking',
				 'Elemental Gem',
				 'Eversmoking Bottle',
				 'Eyes of Charming',
				 'Eyes of Minute Seeing',
				 'Eyes of the Eagle',
				 'Figurine of Wonderous Power, Silver Raven',
				 'Gauntlets of Ogre Power',
				 'Gem of Brightness',
				 'Gloves of Missile Snaring',
				 'Gloves of Swimming and Climbing',
				 'Gloves of Thievery',
				 'Goggles of Night',
				 'Hat of Disguise',
				 'Headband of Intellect',
				 'Helm of Comprehending Languages',
				 'Helm of Telepathy',
				 'Immovable Rod',
				 'Instrument of the Bards, Doss Lute',
				 'Instrument of the Bards, Fochlucan Bandore',
				 'Instrument of the Bards, Mac-Fuirmidh Cittem',
				 'Javelin of Lightning',
				 'Keoghtom\'s Ointment',
				 'Lantern of Revealing',
				 'Mariner\'s Armor',
				 'Medallion of Thoughts',
				 'Mithral Armor',
				 'Necklace of Adaptation',
				 'Oil of Slipperiness',
				 'Pearl of Power',
				 'Periapt of Health',
				 'Periapt of Wound Closure',
				 'Philter of Love',
				 'Pipes of Haunting',
				 'Pipes of the Sewers',
				 'Potion of Animal Friendship',
				 'Potion of Fire Breath',
				 'Potion of Greater Healing',
				 'Potion of Growth',
				 'Potion of Hill Giant Strength',
				 'Potion of Poison',
				 'Potion of Resistance',
				 'Potion of Water Breathing',
				 'Quiver of Ehlonna',
				 'Ring of Jumping',
				 'Ring of Mind Shielding',
				 'Ring of Swimming',
				 'Ring of Warmth',
				 'Ring of Water Walking',
				 'Robe of Useful Items',
				 'Rod of the Pact Keeper +1',
				 'Rope of Climbing',
				 'Saddle of the Cavalier',
				 'Sending Stones',
				 'Sentinel Shield',
				 'Shield +1',
				 'Slippers of Spider Climbing',
				 'Spell Scroll, 2nd Level',
				 'Spell Scroll, 3rd Level',
				 'Staff of the Adder',
				 'Staff of the Python',
				 'Stone of Good Luck',
				 'Sword of Vengeance',
				 'Trident of Fish Command',
				 'Wand of Magic Detection',
				 'Wand of Magic Missile',
				 'Wand of Secrets',
				 'Wand of the War Mage +1',
				 'Wand of Web',
				 'Weapon of Warming',
				 'Weapon +1',
				 'Wind Fan',
				 'Winged Boots',
]

rareItems = ['Armor of Resistance',
			 'Armor of Vulnerability',
			 'Armor +1',
			 'Arrow-catching Shield',
			 'Elven Chain',
			 'Glamoured Studded Leather',
			 'Shield of Missile Attraction',
			 'Shield +2',
			 'Elixir of Health',
			 'Oil of Etherealness',
			 'Potion of Clairvoyance',
			 'Potion of Diminution',
			 'Potion of Fire Giant Strength',
			 'Potion of Frost Giant Strength',
			 'Potion of Gaseous Form',
			 'Potion of Heroism',
			 'Potion of Invulnerability',
			 'Potion of Mind Reading',
			 'Potion of Stone Giant Strength',
			 'Potion of Superior Healing',
			 'Ring of Animal Influence',
			 'Ring of Evasion',
			 'Ring of Feather Falling',
			 'Ring of Free Action',
			 'Ring of Protection',
			 'Ring of Resistance',
			 'Ring of Spell Storing',
			 'Ring of X-ray Vision',
			 'Ring of the Ram',
			 'Rod of Rulership',
			 'Rod of the Pact Keeper +2',
			 'Tentacle Rod',
			 'Scroll of Protection',
			 'Spell Scroll, 4th Level',
			 'Spell Scroll, 5th Level',
			 'Staff of Charming',
			 'Staff of Healing',
			 'Staff of Swarming Insects',
			 'Staff of Withering',
			 'Staff of the Woodlands',
			 'Wand of Binding',
			 'Wand of Enemy Detection',
			 'Wand of Fear',
			 'Wand of Fireballs',
			 'Wand of Lightning Bolts',
			 'Wand of Paralysis',
			 'Wand of Wonder',
			 'Wand of the War Mage +2',
			 'Ammunition +2',
			 'Berserker Axe',
			 'Dagger of Venom',
			 'Dragon Slayer',
			 'Flame Tongue',
			 'Giant Slayer',
			 'Mace of Disruption',
			 'Mace of Smiting',
			 'Mace of Terror',
			 'Sun Blade',
			 'Sword of Life Stealing',
			 'Sword of Wounding',
			 'Vicious Weapon',
			 'Weapon +2',
			 'Amulet of Health',
			 'Bag of Beans',
			 'Bead of Force',
			 'Belt of Dwarvenkind',
			 'Belt of Hill Giant Strength',
			 'Boots of Levitation',
			 'Boots of Speed',
			 'Bowl of Commanding Water Elementals',
			 'Bracers of Defense',
			 'Brazier of Commanding Fire Elementals',
			 'Cape of the Mountebank',
			 'Censer of Controlling Air Elementals',
			 'Chime of Opening',
			 'Cloak of Displacement',
			 'Cloak of the Bat',
			 'Cube of Force',
			 'Daern\'s Instant Fortress (broken)',
			 'Dimensional Shackles',
			 'Figurine of Wondrous Power, Bronze Griffon',
			 'Figurine of Wondrous Power, Ebony Fly',
			 'Figurine of Wondrous Power, Golden Lions',
			 'Figurine of Wondrous Power, Ivory Goats',
			 'Figurine of Wondrous Power, Marble Elephant',
			 'Figurine of Wondrous Power, Onyx Dog',
			 'Figurine of Wondrous Power, Serpentine Owl',
			 'Folding Boat',
			 'Gem of Seeing',
			 'Helm of Teleportation',
			 'Heward\'s Handy Haversack',
			 'Horn of Blasting',
			 'Horn of Valhalla, Brass',
			 'Horn of Valhalla, Silver',
			 'Horseshoes of Speed',
			 'Instrument of the Bards, Canaith Mandolin',
			 'Instrument of the Bards, Cli Lyre',
			 'Ioun Stone, Awareness',
			 'Ioun Stone, Protection',
			 'Ioun Stone, Reserve',
			 'Ioun Stone, Sustenance',
			 'Iron Bands of Bilarro',
			 'Mantle of Spell Resistance',
			 'Necklace of Fireballs',
			 'Necklace of Prayer Beads',
			 'Periapt of Proof Against Poison',
			 'Portable Hole',
			 'Quaal\'s Feather Token',
			 'Robe of Eyes',
			 'Rope of Entanglement',
			 'Stone of Controlling Earth Elementals',
			 'Wings of Flying',
]

weapons = ['Club',
		   'Dagger',
		   'Greatclub',
		   'Handaxe',
		   'Javelin',
		   'Light Hammer',
		   'Mace',
		   'Quarterstaff',
		   'Sickle',
		   'Spear',
		   'Crossbow, light',
		   'Dart',
		   'Shortbow',
		   'Sling',
		   'Battleaxe',
		   'Flail',
		   'Glaive',
		   'Greataxe',
		   'Greatsword',
		   'Halberd',
		   'Lance',
		   'Longsword',
		   'Maul',
		   'Morningstar',
		   'Pike',
		   'Rapier',
		   'Scimitar',
		   'Shortsword',
		   'Trident',
		   'War pick',
		   'Warhammer',
		   'Whip',
		   'Blowgun',
		   'Crossbow, hand',
		   'Crossbow, heavy',
		   'Longbow',
]

armor = ['Padded Armor',
		 'Leather Armor',
		 'Studded Leather Armor',
		 'Hide Armor',
		 'Chain Shirt',
		 'Scale Mail',
		 'Breastplate',
		 'Half Plate',
		 'Ring Mail',
		 'Chain Mail',
		 'Splint Armor',
		 'Plate Armor',
]

spells2 = ['Aganazzar\'s Scorcher',
		   'Aid',
		   'Alter Self',
		   'Animal Messenger',
		   'Arcane Lock',
		   'Augury',
		   'Barkskin',
		   'Beast Sense',
		   'Blindness / Deafness',
		   'Blur',
		   'Branding Smite',
		   'Calm Emotions',
		   'Cloud of Daggers',
		   'Continual Flame',
		   'Cordon of Arrows',
		   'Crown of Madness',
		   'Darkness',
		   'Darkvision',
		   'Detect Thoughts',
		   'Dragon\'s Breath',
		   'Dust Devil',
		   'Earthbind',
		   'Enhance Ability',
		   'Enlarge / Reduce',
		   'Enthrall',
		   'Find Steed',
		   'Find Traps',
		   'Flame Blade',
		   'Flaming Sphere',
		   'Gentle Repose',
		   'Gust of Wind',
		   'Healing Spirit',
		   'Heat Metal',
		   'Hold Person',
		   'Invisibility',
		   'Knock',
		   'Lesser Restoration',
		   'Levitate',
		   'Locate Animals or Plants',
		   'Locate Objects',
		   'Magic Mouth',
		   'Magic Weapon',
		   'Maximilian\'s Earthen Grasp',
		   'Melf\'s Acid Arrow',
		   'Mind Spike',
		   'Mirror Image',
		   'Misty Step',
		   'Moonbeam',
		   'Nystul\'s Magic Aura',
		   'Pass without Trace',
		   'Phantasmal Force',
		   'Prayer of Healing',
		   'Protection from Poison',
		   'Pyrotechnics',
		   'Ray of Enfeeblement',
		   'Rope Trick',
		   'Scorching Ray',
		   'See Invisibility',
		   'Shadow Blade',
		   'Shatter',
		   'Silence',
		   'Skywrite',
		   'Snilloc\'s Snowball Storm',
		   'Spider CLimb',
		   'Spike Growth',
		   'Spiritual Weapon',
		   'Suggestion',
		   'Warding Bond',
		   'Warding Wind',
		   'Web',
		   'Zone of Truth',
]

spells3 = ['Animate Dead',
		   'Aura of Vitality',
		   'Beacon of Hope',
		   'Bestow Curse',
		   'Blinding Smite',
		   'Blink',
		   'Call Lightning',
		   'Catnap',
		   'Clairvoyance',
		   'Conjure Animals',
		   'Conjure Barrage',
		   'Counterspell',
		   'Create Food and Water',
		   'Crusader\'s Mantle',
		   'Daylight',
		   'Dispel Magic',
		   'Elemental Weapon',
		   'Enemies Abound',
		   'Erupting Earth',
		   'Fear',
		   'Feign Death',
		   'Fireball',
		   'Flame Arrows',
		   'Fly',
		   'Gaseous Form',
		   'Glyph of Warding',
		   'Haste',
		   'Hunger of Hadar',
		   'Hypnotic Pattern',
		   'Leomund\'s Tiny Hut',
		   'Life Transference',
		   'Lightning Arrow',
		   'Lightning Bolt',
		   'Magic Circle',
		   'Major Image',
		   'Mass Healing Word',
		   'Meld into Stone',
		   'Melf\'s Minute Meteors',
		   'Nondetection',
		   'Phantom Steed',
		   'Plant Growth',
		   'Protection from Energy',
		   'Remove Curse',
		   'Revivify',
		   'Sending',
		   'Sleet Storm',
		   'Slow',
		   'Speak with Dead',
		   'Speak with Plants',
		   'Spirit Guardians',
		   'Stinking Cloud',
		   'Summon Lesser Demons',
		   'Thunder Step',
		   'Tidal Wave',
		   'Tiny Servant',
		   'Tongues',
		   'Vampiric Touch',
		   'Wall of Sand',
		   'Wall of Water',
		   'Water Breathing',
		   'Water Walk',
		   'Wind Wall',
]

spells4 = ['Arcane Eye',
		   'Aura of Life',
		   'Aura of Purity',
		   'Banishment',
		   'Blight',
		   'Charm Monster',
		   'Compulsion',
		   'Confusion',
		   'Conjure Minor Elementals',
		   'Conjure Woodland Beings',
		   'Control Water',
		   'Death Ward',
		   'Dimension Door',
		   'Divination',
		   'Dominate Beast',
		   'Elemental Bane',
		   'Evard\'s Black Tentacles',
		   'Fabricate',
		   'Find Greater Steed',
		   'Fire Shield',
		   'Freedom of Movement',
		   'Giant Insect',
		   'Grasping Vine',
		   'Greater Invisibility',
		   'Guardian of Faith',
		   'Guardian of Nature',
		   'Hallucinatory Terrain',
		   'Ice Storm',
		   'Leomund\'s Secret Chest',
		   'Locate Creature',
		   'Mordenkainen\'s Faithful Hound',
		   'Mordenkainen\'s Private Sanctum',
		   'Otiluke\'s Resilient Sphere',
		   'Phantasmal Killer',
		   'Polymorph',
		   'Shadow of Moil',
		   'Sickening Radiance',
		   'Staggering Smite',
		   'Stone Shape',
		   'Stoneskin',
		   'Storm Sphere',
		   'Summon Greater Demon',
		   'Vitriolic Sphere',
		   'Wall of Fire',
		   'Watery Sphere',
]

spells5 = ['Animate Objects',
		   'Antilife Shell',
		   'Awaken',
		   'Banishing Smite',
		   'Bigby\'s Hand',
		   'Circle of Power',
		   'Cloudkill',
		   'Commune',
		   'Commune with Nature',
		   'Cone of Cold',
		   'Conjure Elemental',
		   'Conjure Volley',
		   'Contact Other Plane',
		   'Contagion',
		   'Control Winds',
		   'Creation',
		   'Danse Macabre',
		   'Dawn',
		   'Destructive Wave',
		   'Dispel Evil and Good',
		   'Dominate Person',
		   'Dream',
		   'Enervation',
		   'Far Step',
		   'Flame Strike',
		   'Geas',
		   'Greater Restoration',
		   'Hallow',
		   'Hold Monster',
		   'Holy Weapon',
		   'Immolation',
		   'Infernal Calling',
		   'Insect Plague',
		   'Legend Lore',
		   'Maelstrom',
		   'Mass Cure Wounds',
		   'Mislead',
		   'Modify Memory',
		   'Negative Energy Flood',
		   'Passwall',
		   'Planar Binding',
		   'Raise Dead',
		   'Rary\'s Telepathic Bond',
		   'Reincarnate',
		   'Scrying',
		   'Seeming',
		   'Skill Empowerment',
		   'Steel Wind Strike',
		   'Swift Quiver',
		   'Synaptic Static',
		   'Telekinesis',
		   'Teleportation Circle',
		   'Transmute Rock',
		   'Tree Stride',
		   'Wall of Force',
		   'Wall of Light',
		   'Wall of Stone',
		   'Wrath of Nature',
]


################
#  GLOBAL VARS #
################

dndRace = ""
dndClass = ""
dndBackground = ""
dndGender = ""
dndAlignment = ""
dndName = ""
igotclass = ""
acqJob = ""
end = None
printColor = ""

#################

def raceSel():
	global dndRace
	shuffler()
	#d31 = random.randrange(0,31)
	#dndRace = races[d31]
	dndRace = random.choice(races)
	#dndRace = races[18] #test a specific race

	if dndRace == 'Elf':
		d6 = random.randrange(0,6)
		dndRace = elf_subraces[d6] #should be d6

	elif 'Dwarf' in dndRace:
		d3 = random.randrange(0,3)
		dndRace = dwarf_subraces[d3]

	elif 'Goblin' in dndRace:
		subRace = " BADASS"

	elif dndRace == 'Half-Elf':
		d4 = random.randrange(0,4)
		dndRace = halfelf_subraces[d4]

	elif 'Human' in dndRace:
		d18 = random.randrange(0,19) #humans
		dndRace = dndRace + ", ethnicity: " + human_subraces[d18]

	elif 'Aasimar' in dndRace:
		d3 = random.randrange(0,3)
		dndRace = aasimar_subraces[d3]

	elif 'Genasi' in dndRace:
		d3 = random.randrange(0,3)
		dndRace = genasi_subraces[d3]

	elif 'Gith' in dndRace:
		d2 = random.randrange(0,2)
		dndRace = gith_subraces[d2]

	elif 'Gnome' in dndRace:
		d3 = random.randrange(0,3)
		dndRace = gnome_subraces[d3]

	elif 'Halfling' in dndRace:
		d6 = random.randrange(0,6) #formerly a d4
		dndRace = halfling_subraces[d6]
		if 'Other' in dndRace:
			d13 = random.randrange(0,13)
			dndRace = otherhalfling_subraces[d13]

	elif 'Dragonborn' in dndRace:
		d10 = random.randrange(0,10)
		dndRace = dragonborn_subraces[d10] + " " + dndRace

	elif 'Shifter' in dndRace:
		for i in range(10):
			random.shuffle(shifter_subraces)
		dndRace = random.choice(shifter_subraces)

	elif 'Warforged' in dndRace:
		for i in range(10):
			random.shuffle(warforged_subraces)
		dndRace = random.choice(warforged_subraces)

	print("Race: " + colored(dndRace, 'cyan'))

#################

def shuffler():
	for i in range(100):
		random.shuffle(dndclass)
		random.shuffle(races)

#################

def classSel():
	global dndClass,igotclass,end,druid_land
	shuffler()
	d15 = random.randrange(0,15)
	dndClass = dndclass[d15] 
	#dndClass = dndclass[14] #test value to verify specific classes function
	#print(dndClass)

	if 'Barbarian' in dndClass:
		d7 = random.randrange(0,7)
		dndClass = barbarian_subclass[d7] + " " + dndClass
		igotclass = "Barbarian - " + barbarian_subclass[d7][12:end] 

	elif 'Bard' in dndClass:
		d5 = random.randrange(0,5)
		dndClass = dndClass + " who studied at the " + bard_subclass[d5]
		igotclass = "Bard - " + bard_subclass[d5][11:end]

	elif 'Cleric' in dndClass:
		d12 = random.randrange(0,12)
		dndClass = cleric_subclass[d12] + " " + dndClass
		igotclass = "Cleric - " + cleric_subclass[d12]

	elif 'Druid' in dndClass:
		d5 = random.randrange(0,5)
		dndClass = dndClass + " brought up in the " + druid_subclass[d5]
		igotclass = "Druid - " + druid_subclass[d5][14:end]
		if igotclass == 'Druid - ms':
			igotclass = 'Druid - Dreams'
		elif igotclass == 'Druid - es':
			igotclass = 'Druid - Spores'

		if 'Circle of the Land' in dndClass:
			d8 = random.randrange(0,8)
			for i in range(5):
				random.shuffle(druid_land)
			dLand = druid_land[d8]
			dndClass = dndClass + " (" + dLand + ")"

	elif 'Fighter' in dndClass:
		d9 = random.randrange(0,9)
		d6 = random.randrange(0,6)
		dndClass = fighter_subclass[d9] + " " + dndClass + " trained in the ways of " + fighter_style[d6]
		igotclass = "Fighter - " + fighter_subclass[d9]

	elif 'Monk' in dndClass:
		d9 = random.randrange(0,9)
		dndClass = monk_subclass[d9] + " " + dndClass
		if ' the ' in monk_subclass[d9]:
			igotclass = 'Monk - ' + monk_subclass[d9][11:end]
		else:
			igotclass = 'Monk - ' + monk_subclass[d9][7:end]

	elif 'Paladin' in dndClass:
		d8 = random.randrange(0,8)
		d4 = random.randrange(0,4)
		dndClass = paladin_subclass[d8] + " " + dndClass + " trained in the art of " + paladin_style[d4]
		if 'Oathbreaker' in paladin_subclass[d8]:
			igotclass = 'Paladin - Oathbreaker'
		elif ' the ' in paladin_subclass[d8]:
			igotclass = 'Paladin - ' + paladin_subclass[d8][12:end]
		else:
			igotclass = 'Paladin - ' + paladin_subclass[d8][8:end]

	elif 'Ranger' in dndClass:
		d6 = random.randrange(0,6)
		d4 = random.randrange(0,4)
		dndClass = ranger_subclass[d6] + " " + dndClass + " whose specialty lies in " + ranger_style[d4]
		igotclass = "Ranger - " + ranger_subclass[d6]

	elif 'Rogue' in dndClass:
		d7 = random.randrange(0,7)
		dndClass = dndClass + " that specializes as a " + rogue_subclass[d7]
		igotclass = "Rogue - " + rogue_subclass[d7]

	elif 'Sorcerer' in dndClass:
		d6 = random.randrange(0,6)
		dndClass = sorcerer_subclass[d6] + " " + dndClass
		igotclass = "Sorcerer - " + sorcerer_subclass[d6]

	elif 'Warlock' in dndClass:
		d8 = random.randrange(0,8)
		d3 = random.randrange(0,3)
		dndClass = warlock_pact[d3] + " " + dndClass + " who was granted their power by " + warlock_subclass[d8]
		igotclass = "Warlock - " + warlock_subclass[d8]

	elif 'Wizard' in dndClass:
		d10 = random.randrange(0,10)
		choice = wizard_subclass[d10]
		if 'Artificer' in choice:
			dndClass = "Artificer (Wizard) - A tinkerer who melds magic into their creations"
			igotclass = "Wizard - Artificer"
		elif 'Bladesinger' in choice:
			dndClass = "Bladesinger (Wizard)"
			igotclass = "Wizard - Bladesinger"
		elif 'War Magic' in choice:
			dndClass = dndClass + " trained in " + choice
			igotclass = "Wizard - War Magic"
		else:
			dndClass = dndClass + " trained in " + choice
			igotclass = "Wizard - " + wizard_subclass[d10][10:end]

	elif 'Blood Hunter' in dndClass:
		d3 = random.randrange(0,3)
		d3One = random.randrange(0,3)

		dndClass = bloodhunter_subclass[d3] + " " + dndClass + " who has undertaken the " + bloodhunter_rites[d3]
		igotclass = "Blood Hunter - " + bloodhunter_subclass[d3][13:end]

	elif 'Artificer' in dndClass:
		d2 = random.randrange(0,2)
		dndClass = "Artificer - " + artificer_subclass[d2]
		igotclass = dndClass

	elif 'Illrigger' in dndClass:
		d3 = random.randrange(0,3)
		d4 = random.randrange(0,4)
		dndClass = "Illrigger - " + illrigger_subclass[d3] + " trained in the art of " + illrigger_style[d4]
		igotclass = "Illrigger - " + illrigger_subclass[d3]

	print("Class: " + colored(dndClass,'green'))
	#print(dndClass.split()[1])	#This will print the second word in a value

#################

def backgroundSel():
	global dndBackground,gender

	#d48 = random.randrange(0,48)
	#dndBackground = background[d48]
	dndBackground = random.choice(background)
	
	if 'Faction Agent' in dndBackground:
		d10 = random.randrange(0,10)
		dndBackground = dndBackground + " for " + factions[d10]

	d100 = random.randrange(1,101)
	if d100 > 93:
		for i in range(10):
			random.shuffle(bgFeature)
		bg_feature = random.choice(bgFeature)

		print("Background: " + colored(dndBackground, 'magenta') + colored(" with the ", 'magenta') + colored(bg_feature, 'magenta') + colored(" background feature.", 'magenta'))

	else:
		print("Background: " + colored(dndBackground, 'magenta'))

#################

def miscSel():
	global dndGender, dndAlignment, dndName, acqJob
	d2 = random.randrange(0,2)
	d9 = random.randrange(0,9)

	dndGender = gender[d2]
	dndAlignment = alignment[d9]
	colorMe = ""
	gendColor = ""

	if 'Evil' in dndAlignment:
		colorMe = 'red'
	elif 'Good' in dndAlignment:
		colorMe = 'green'
	elif 'Neutral' in dndAlignment:
		colorMe = 'cyan'

	if dndGender == 'Male':
		gendColor = 'yellow'
	else:
		gendColor = 'magenta'

	print("Gender: " + colored(dndGender, gendColor))
	print("Alignment: " + colored(dndAlignment, colorMe))

	colorMe = ""
	gendColor = ""
	d100 = random.randrange(1,101)
	#print("DEBUG -- d100 roll: " + str(d100))
	if d100 > 85:
		for i in range(10):
			random.shuffle(acquisitionsJob)
		acqJob = random.choice(acquisitionsJob)
		print("Acquisitions Inc. Franchise Member Role: " + colored(acqJob, 'green') + colored(" (Rank 1)", 'green'))

"""
	for i in range(3):
		d24 = random.randrange(0,24)
		#d69 = random.randrange(0,69)
		dndName += namePiece0[d24]
"""

#################

def nameSel():
	global dndName
# WORKING code below:
	nameChoice()
	print("Name: " + colored(dndName.title(), 'magenta'))
	dndName = ""

# Proposed Code (broken due to order of ops in printer())
'''
	if "Human" in dndRace:
		humeName(dndGender)
	else:
		nameChoice()
	print("Name: " + colored(dndName.title(), 'magenta'))
	dndName = ""
'''

#################

# This section should add in a new thing for human names, or i can do a function
# instead and pass in the gener value.
# the order of printer() breaks it, so if human is the first character generated
# then it will not recognize  that human is the race until after it prints a name :/
# and then on the next iteration, it will give that character a human name regardless 
# of race
'''
def humeName(dndGender):
	global dndName

	if dndGender == 'Female':
		dndName += random.choice(humanFemaleName) + " "

	else:
		dndName += random.choice(humanMaleName) + " "

	dndName += random.choice(humanSurname)
'''
#################

def nameChoice():
	global dndName
	x = 1
	for i in range(3):
		d20 = random.randrange(0,20)
		if x == 1:
			dndName += namePiece1[d20]
		elif x == 2:
			dndName += namePiece2[d20]
		elif x == 3:
			dndName += namePiece3[d20]
		else:
			print(x)
		#print("x: {x}\td20: {d20}\n").format(x = x, d20 = d20)
		x = x + 1
	x = 1

#################

def specialAbilities():
	global igotclass, acqJob
	hume = dndRace
	if 'Human' in hume:
		hume = "Human"
	print("Ability Score Bonuses: " + colored(racialScores[hume], 'yellow'))
	print("Racial Abilities: " + racials[hume] + "\n")
	print("Class Abilities: " + classAbilities[igotclass] + "\n")
	
	if acqJob != "":
		print("Acquisitions Inc Job Abilities: " + acqAbilities[acqJob] + "\n")
		acqJob = ""

	igotclass = ""

#################

def ogRolls():
	count = 0
	scoreType = ""

	for i in range(6):
		d20 = random.randrange(1,21)
		if d20 >= 18:
			scoreType = 'cyan'
		elif d20 <= 17 and d20 > 15:
			scoreType = 'green'
		elif d20 <=15 and d20 > 13:
			scoreType = 'yellow'
		elif d20 <=13 and d20 >= 10:
			scoreType = 'magenta' 
		elif d20 < 10:
			scoreType = 'red'

		if count == 0:
			print("Str: " + colored(d20, scoreType))
		elif count == 1:
			print("Dex: " + colored(d20, scoreType))
		elif count == 2:
			print("Con: " + colored(d20, scoreType))
		elif count == 3:
			print("Int: " + colored(d20, scoreType))
		elif count == 4:
			print("Wis: " + colored(d20, scoreType))
		elif count == 5:
			print("Cha: " + colored(d20, scoreType) + "\n")

		count = count + 1

	count = 0

#################

def normRolls():
	count = 0
	scoreTypee = ""
	scores = ""

	for i in range(6):
		stat = statgen()
		estat = int(stat)

		if estat >= 18:
			scoreTypee = 'cyan'
		elif estat <= 17 and estat > 15:
			scoreTypee = 'green'
		elif estat <=15 and estat > 13:
			scoreTypee = 'yellow'
		elif estat <=13 and estat >= 10:
			scoreTypee = 'magenta' 
		elif estat < 10:
			scoreTypee = 'red'

		#This is used to up the low stats to 8
		if int(stat) < 8:
			stat = "8"

		if count == 0:
			#print("Str: " + colored(stat, scoreTypee))
			scores += "Str: " + colored(stat, scoreTypee) + " "
		elif count == 1:
			#print("Dex: " + colored(stat, scoreTypee))
			scores += "Dex: " + colored(stat, scoreTypee) + " "
		elif count == 2:
			#print("Con: " + colored(stat, scoreTypee))
			scores += "Con: " + colored(stat, scoreTypee) + " "
		elif count == 3:
			#print("Int: " + colored(stat, scoreTypee))
			scores += "Int: " + colored(stat, scoreTypee) + " "
		elif count == 4:
			#print("Wis: " + colored(stat, scoreTypee))
			scores += "Wis: " + colored(stat, scoreTypee) + " "
		elif count == 5:
			#print("Cha: " + colored(stat, scoreTypee) + "\n")
			scores += "Cha: " + colored(stat, scoreTypee) + " "

		count = count + 1

	count = 0
	print("Ability Scores: " + scores)
	#scores = "" #used with the code above to make stats lower than 8 to an 8

#################

def statgen():
	roll = []

	for i in range(4):
		d6 = random.randrange(1,7)
		roll.append(d6)
	roll.remove(min(roll))

	return str(sum(roll))

#################

def umagicItems():
	d93 = random.randrange(0,93)
	for i in range(10):
		random.shuffle(uncommonItems)
	itemz = uncommonItems[d93]

	if 'Spell Scroll, 2' in itemz:
		d71 = random.randrange(0,71)
		for i in range(5):
			random.shuffle(spells2)
		itemz = "Spell Scroll, 2nd Level (" + spells2[d71] + ")"

	elif 'Spell Scroll, 3' in itemz:
		d62 = random.randrange(0,62)
		for i in range(5):
			random.shuffle(spells3)
		itemz = "Spell Scroll, 3rd Level (" + spells3[d62] + ")"

	elif 'Weapon +1' in itemz:
		d36 = random.randrange(0,36)
		for i in range(5):
			random.shuffle(weapons)
		itemz = weapons[d36] + " +1"

	print("Magic Item: " + colored(itemz, printColor) + colored(' (U)', printColor))

#################

def rmagicItems():
	d112 = random.randrange(0,112)
	for i in range(10):
		random.shuffle(rareItems)
	itemz1 = rareItems[d112]

	if 'Spell Scroll, 4' in itemz1:
		d45 = random.randrange(0,45)
		for i in range(5):
			random.shuffle(spells4)
		itemz1 = "Spell Scroll, 4nd Level (" + spells4[d45] + ")"

	elif 'Spell Scroll, 5' in itemz1:
		d58 = random.randrange(0,58)
		for i in range(5):
			random.shuffle(spells5)
		itemz1 = "Spell Scroll, 5rd Level (" + spells5[d58] + ")"

	elif 'Weapon +2' in itemz1:
		d36 = random.randrange(0,36)
		for i in range(5):
			random.shuffle(weapons)
		itemz1 = weapons[d36] + " +2"

	elif "Armor +1" in itemz1:
		d12 = random.randrange(0,12)
		for i in range(5):
			random.shuffle(armor)
		itemz1 = armor[d12] + " +1"

	print("Magic Item: " + colored(itemz1, printColor) + colored(' (R)', printColor))

#################

def itemSelection():
	global printColor
	itemRarity = ['uncommon', 'rare']
	printColor = ""

	for i in range(10):
		random.shuffle(itemRarity)

	for i in range(2):
		d2 = random.randrange(0,2)
		funBag = itemRarity[d2]

		if 'uncommon' in funBag:
			printColor = 'yellow'
			umagicItems()

		elif 'rare' in funBag:
			printColor = 'green'
			rmagicItems()

#################

def printer():
	for i in range(2):
		nameSel()
		raceSel()
		classSel()
		backgroundSel()
		miscSel()
		specialAbilities()
		#ogRolls()
		normRolls()
		itemSelection()
		print("")
		print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
		print("") #final newline

#################

# Main Routine
printer()

"""
	    print(str(x) + ":" + str(y) + ":" + str(z) + " - " + colored(races[x], 'yellow') + " " + \
	    	colored(dndclass[y], 'green') + " who is a " + colored(background[z], 'cyan'))

# Available colors : [grey, red, green, yellow, blue, magenta, cyan, white]
# Available attributes: [blink, bold, reverse, underline, dark, concealed] used as attrs=['blink, 'bold']
"""


# Things to add:
# ----------------
# - ?
#






	









