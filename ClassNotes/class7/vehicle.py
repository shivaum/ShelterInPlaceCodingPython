class Vehicle:

	def __init__(self, make, color, gas_tank=20):
		self.model = make
		self.color = color
		self.gas_tank = gas_tank
		self.curr_gas = 0

	def change_model(self, model):
		self.model = model

	def add_gas(self, gallons):
		print("Adding", gallons, "to", self.curr_gas, "currently in the tank")
		self.curr_gas += gallons
		if (self.curr_gas > self.gas_tank):
			print("The gas tank is full!")
			self.curr_gas = self.gas_tank
		else:
			print("Successfully added gas!")

	def __str__(self):
		return ("Model: " + self.model + ", Color: " + self.color +
				", Tank Capacity: " + str(self.gas_tank) + 
				", Current Gas: " + str(self.curr_gas))

my_car = Vehicle('Acura', 'Black')
another_car = Vehicle('Mazda', 'Red', 10)

print("My car:", my_car)
print("Another car:", another_car)

my_car.add_gas(15)

another_car.add_gas(15)

print("My car:", my_car)
print("Another car:", another_car)

