from ActionEnum import ActionEnum


class Action(object):

	def __init__(self, action, position, value, organism):
		self.__action = action
		self.__position = position
		self.__value = value
		self.__organism = organism

	@property
	def action(self):
		return self.__action

	@property
	def position(self):
		return self.__position

	@property
	def value(self):
		return self.__value

	@property
	def organism(self):
		return self.__organism

	def __str__(self):
		className = self.organism.__class__.__name__
		choice = {
			ActionEnum.A_ADD: '{0}: Dodany w punkcie: {1}'.format(className, self.position),
			ActionEnum.A_INCREASEPOWER: '{0} increase power: {1}'.format(className, self.value),
			ActionEnum.A_MOVE: '{0} Przemieścił się z punktu: {1} do punktu: {2}'.format(className, self.organism.position, self.position),
			ActionEnum.A_REMOVE: '{0} Usunięty z : {1}'.format(className, self.organism.position)
		}
		return choice[self.action]

