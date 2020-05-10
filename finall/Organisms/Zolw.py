from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Position import Position

class Zolw(Animal):

	def __init__(self, zolw=None, position=None, world=None):
		super(Zolw, self).__init__(zolw, position, world)

	def clone(self):
		return Zolw(self, None, None)

	def initParams(self):
		self.power = 6
		self.initiative = 3
		self.liveLength = 25
		self.powerToReproduce = 40
		self.sign = 'Z'

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithOtherSpecies(self.world.getNeighboringPositions(self.position), Zolw)

	def consequences(self, atackingOrganism):
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))

		return result