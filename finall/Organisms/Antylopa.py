from .Animal import Animal
from .Wolf import Wolf


class Antylopa(Animal):

	def __init__(self, antylopa=None, position=None, world=None):
		super(Antylopa, self).__init__(antylopa, position, world)

	def clone(self):
		return Antylopa(self, None, None)

	def initParams(self):
		self.power = 3
		self.initiative = 3
		self.liveLength = 10
		self.powerToReproduce = 6
		self.sign = 'A'

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

	def getNeighboringPositionWolf(self):
		return self.world.filterPositionsWithOtherSpecies(self.world.getOrganismFromPosition(self.position), (Wolf))

