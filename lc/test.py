class A:

    var = 1
    def printvar(self):
        print "self.var is %d" % self.var
        print "A.var is %d" % A.var

#print A.var

a = A()
a.printvar()



print A.var is a.var

A.var = 3
a.printvar()

print id(A.var)
print id(a.var)
print A.var is a.var

a.var = 2
a.printvar()
print id(A.var)
print id(a.var)
print A.var is a.var