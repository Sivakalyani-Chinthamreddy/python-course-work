#sys-information/control related to Python and its environment
'''import sys
print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")'''

#platform → information about the computer's operating system and hardware
'''import platform

print(platform.system())
print(platform.release())
print(platform.processor())


#math module in Python, it is a built-in module that provides mathematical functions and constants.
import math

print(math.pi)
print(math.e)
print(math.sqrt(49))
print(math.factorial(2))
print(math.sin(45))
print(math.tan(90))
print(math.cos(60))
print(math.log(5,2))
print(math.degrees(2))
print(math.radians(30))
print(math.gcd(8,35))
print(math.pow(3,2))

print(round(12.898989))
import math
print(math.ceil(12.233435546547576574))#ceil wiil give upper value
print(math.ceil(12.0001))
print(math.ceil(12.8888))

print(math.floor(12.999999))#floor will give lower value
print(math.floor(12.001))

#random-random is a built-in Python module used to generate random values and make random selections.
import random

print(random.random())
print(random.randint(2,10))
print(random.uniform(1,6))#if we want o/p as deciml vlue
l=[1,2,3,4,45,66,6,0]
print(random.choices(l))

corses=['python','java','servicenow']
print(random.choice(corses))
random.shuffle(corses)
print(corses)

#frequency
s='pyhton programming'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#using counter
from collections import Counter
s="python programming language"
res=Counter(s)
print(res)

#defaultdict
from collections import Counter,defaultdict

l="pyhton programming"
res=defaultdict(int)
for i in l:
    res[i]+=1

print(res)

l=['pyhton','java','c++']
res=defaultdict(list)
for i in l:
    res[i].append(['varaibles','datatypes','oops'])
print(res)'''

#deque

from collections import deque
l=deque([])
'''l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.popleft()'''
l.appendleft(10)#40 30 20 70
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.append(70)
print(l)
