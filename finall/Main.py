from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Antylopa import Antylopa
from Organisms.Zolw import Zolw
from Organisms.Toadstool import Toadstool
from Organisms.Kosmita import Kosmita
import os

if __name__ == '__main__':

	pyWorld = World(8, 8)

	newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=0, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Dandelion(position=Position(xPosition=0, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Wolf(position=Position(xPosition=7, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Toadstool(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Antylopa(position=Position(xPosition=7, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Zolw(position=Position(xPosition=6, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Kosmita(position=Position(xPosition=5, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	skrot={
		'Antylopa':"A",
		'Dendelion':"D",
		'Grass':"G",
		'Kosmita':"K",
		'Sheep':"S",
		'Toadstool':"T",
		'Wolf':"W",
		'Zolw':"Z"

	}

	def DodajAntylope(pyWorld, x, y):
		return Antylopa(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajDandelion(pyWorld, x, y):
		return Dandelion(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajWilka(pyWorld, x, y):
		return Wolf(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajZolwia(pyWorld, x, y):
		return Zolw(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajToadstool(pyWorld, x, y):
		return Toadstool(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajSheep(pyWorld, x, y):
		return Sheep(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def DodajGrass(pyWorld, x, y):
		return Grass(position=Position(xPosition=x, yPosition=y), world=pyWorld)
	def stworzNoweIstoty(pyworld, addOrganism, position):
		lives={
			'D':DodajDandelion,
			'A':DodajAntylope,
			'W':DodajWilka,
			'Z':DodajZolwia,
			'T':DodajToadstool,
			'S':DodajSheep,
			'G':DodajGrass
		}

	def add():
		print("Jeśli chcesz dodać organizm kliknij T")
		print("Jeśli chcesz przejść do następnej rundy kliknij ENTER")
		if(input()=="T"):
			print("Podaj organizm jaki chcesz dodać: ")
			for key, value in skrot.items():
				print("Aby dodać "+key+" wpisz "+skrot[key])
			addOrganism=input().upper()
			print("Podaj x i y z zakresu:(0-7,0-7)")
			x=input()
			x=int(x)
			y=input()
			y=int(y)

			position = Position(int(x), int(y))
			if pyWorld.positionOnBoard(position):
				if pyWorld.getOrganismFromPosition((position)):
					stworzNoweIstoty(addOrganism, position)
				else:
					print("nie możesz tutaj stworzyć nowego organizmu")
					info()
			else:
				print("nie dodano organizmu")



	print(pyWorld)

	for _ in range(0, 100):
		input('')
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
		add()


