from .Animal import Animal

class Kosmita(Animal):

	def __init__(self, kosmita=None, position=None, world=None):
		super(Animal, self).__init__(kosmita, position, world)

	def clone(self):
		return Kosmita(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 45
		self.liveLength = 1000
		self.powerToReproduce = 1000
		self.sign = 'K'


	def getFreeNeighboringPosition(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))




