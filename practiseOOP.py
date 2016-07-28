class Customer(object):
	def __init__(self, name, balance=0.0):
		self.name = name
		self.balance = balance
		print "Hello %s" % (self.name)

	def withdraw(self,amount):
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance = self.balance - amount
		return self.balance

	def deposit(self, amount):
		self.balance = self.balance + amount
		print "money is: ", self.balance
		return self.balance

self = Customer('Jonny')
print self.balance


self.withdraw(-1000)
print self.balance