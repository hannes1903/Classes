#class C(object):

#c = C()
#c.y = ['a', 'a', 'b','a', 'c' ]
#print (c.mostcommon(__dict__))


#c = MyCounter(['a', 'a', 'b','a', 'c' ])

#print(c.mostcommon())
#print(c['a'])

import math

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print (D['food'])

D['quantity'] += 1

print (D)

D = {}
D['name'] = 'Bob' # Create keys by assignment >>>
D['job'] = 'dev'
D['age'] = 40

print (D)
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40) # Keywords
print (bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping
print (bob2)


rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

print (rec['name'])

print (rec['name']['last'])

print (rec['jobs'])

print (rec['jobs'][-1])   #????????????

rec['jobs'].append('janitor')

print(rec)

D = {'a': 1, 'b': 2, 'c': 3}

print(D)

Ks = list(D.keys())

print (Ks)

for key in Ks:
    print(key, '=>', D[key])
