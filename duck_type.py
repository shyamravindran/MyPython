# doesn't care about what object, only care the behaviuor,
# if it is capable to do the same things
class Duck:

	def quack(self):
		print " quack quack"
	
	def fly(self):
		print "flap flap"

class man:

        def quack(self):
                print " quacking like a duck"

        def fly(self):
                print "flapping my arms "

def quack_and_fly(thing):
	if isinstance(thing, Duck):
		thing.quack()
		thing.fly()
	else:
		print "this has to be a duck"

d = Duck()
quack_and_fly(d)

m = man()
quack_and_fly(m)
