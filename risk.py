import random
def roll_dice(number_dice):
	"""
	Cette fondtion simule le lancé de dé(s) d'un.e joueur.se et retourne une liste des valeurs des dés lancés dans l'orde décroissant.
	"""
	dice = []
	for i in range(number_dice):
		dice.append(random.randint(1,6))
	dice.sort(reverse=True)
	return dice


def battle(number_red_dice, number_blue_dice):
	"""
	Cette fonction compare les lancés de dés des deux joueur.se.s et retourne le nombre de régiment(s) perdu(s) par chacun.e.
	"""
	red_dice = roll_dice(number_red_dice)
	blue_dice = roll_dice(number_blue_dice)
	print()
	print(red_dice)
	print(blue_dice)
	attacker_lost_troops = 0
	defender_lost_troops = 0
	for i in range(min(len(red_dice), len(blue_dice))):
		if red_dice[i] > blue_dice[i]:
			defender_lost_troops += 1
		else:
			attacker_lost_troops += 1
	print(f"Vous perdez {attacker_lost_troops} régiment(s).")
	print(f"Votre adversaire perd {defender_lost_troops} régiment(s).")
	return attacker_lost_troops, defender_lost_troops



def war(attacker_total_troops, defender_total_troops, number_attacks):
	"""
	Cette fonction simule toutes les attaques de l'utilisateur.trice jusqu'à qu'il ne reste plus d'unités à l'un.e des deux joueur.se.s dans la limite du nombre d'attaques choisi.
	"""
	attacker_total_lost_troops = 0
	defender_total_lost_troops = 0
	while attacker_total_troops > 1 and defender_total_troops > 0 and number_attacks > 0:
		number_red_dice = 0
		number_blue_dice = 0		
		if attacker_total_troops < 4:
			number_red_dice = attacker_total_troops - 1
		else:
			number_red_dice = 3
		if defender_total_troops < 2:
			number_blue_dice = 1
		else:
			number_blue_dice = 2
		a, b = battle(number_red_dice, number_blue_dice)
		attacker_total_lost_troops += a
		defender_total_lost_troops += b
		attacker_total_troops -= a
		defender_total_troops -= b
		number_attacks -= 1
	print()
	print(f"Vous avez perdu {attacker_total_lost_troops} régiment(s). Il vous reste {attacker_total_troops} régiment(s).")
	print(f"Votre adversaire a perdu {defender_total_lost_troops} régiment(s). Il reste {defender_total_troops} régiment(s) à votre adversaire.")
	print()
	if defender_total_troops == 0:
		print("Vous avez éliminé tous les régiments de votre adversaire. Vous capturez le territoire.")
	elif attacker_total_troops == 1:
		print("Il ne vous reste plus qu'un seul régiment. Vous ne pouvez plus attaquer depuis ce territoire.")
	return attacker_total_lost_troops, defender_total_lost_troops


def prompt():
	"""
	Cette fonction demande à l'utilisateur.trice :
		- le nombre de régiment(s) avec lequel iel souhaite attaquer;
		- le nombre de régiment(s) avec lequel son adversaire souhaite défendre;
		- le nombre de fois qu'iel souhaite répéter son attaque.
	"""
	import os
	clear = lambda: os.system('clear')
	clear()

	global attacker_total_troops
	while True:
		try:
			attacker_total_troops = int(input("Avec combien de régiment(s) souhaitez-vous attaquer ? "))
			if attacker_total_troops < 2:
				print("Veuillez saisir un nombre entier supérieur à 1.")
				continue
		except ValueError:
			print("Veuillez saisir un nombre entier supérieur à 1.")
			continue
		else:
			break
	
	global defender_total_troops
	while True:
		try:
			defender_total_troops = int(input("Avec combien de régiment(s) votre adversaire souhait-il défendre ? "))
			if defender_total_troops < 1:
				print("Veuillez saisir un nombre entier supérieur à 0.")
				continue
		except ValueError:
			print("Veuillez saisir un nombre entier supérieur à 0.")
			continue
		else:
			break
	
	global number_attacks
	while True:
		try:
			number_attacks = int(input("Combien de fois souhaitez-vous attaquer ? "))
			if number_attacks < 1:
				print("Veuillez saisir un nombre entier supérieur à 0.")
				continue
		except ValueError:
			print("Veuillez saisir un nombre entier supérieur à 0.")
			continue
		else:
			break


prompt()
war(attacker_total_troops, defender_total_troops, number_attacks)