basic_energy = 10

def sing():
    return "lalala"



class Amazon:				# 아마존 캐릭터 class 선언

	strength = 20         	# 강도 = 20
	dexterity = 25       	# 손재주 = 25
	vitality = 20        	# 활력 = 20
	energy = basic_energy + 15          	# 에너지 = 15

	def attack(self):		# attack method
		return '=> Jab'	# 쨉 공격

	def exercise(self):		# exercise method
		self.strength += 2	# 강도 + 2
		self.dexterity += 3	# 손재주 + 3
		self.vitality += 1	# 활력 + 1


