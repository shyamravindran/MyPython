
class A(object):
	def __init__(self):
		print "first"
class B(object):
	def __init__(self):
		print "second"
class C(A,B):
	def __init__(self):
		super(C, self).__init__()
		print "third"


C()
