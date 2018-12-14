
class MyCounter(object):

    def __init__(self, n):
        self.name = n  #conversion to variable
        #self.n = n

    def some_method (self):
        print(self.name)

    def __repr__(self):
        return str(self. __dict__)

def main():
    pass

c= MyCounter(n='cool_counter')
print (c)

if __name__ =="__main__":
    main()

#def add(a, b):
#    c = a + b
#    return c
#print (add(1, 2))

a = [1,2,3,1,2,1,1,1,4]

m = a[0]

for i in a [1:]:
     if i > m:
         m=i

print (m)