#lambda dunction is a small anyanymous fun used when we need a  small operation in short term
'''
var=lambda arg:exp
'''
wish = lambda name:f"welcome to course {name}"
print(wish('kalyani'))

gst=lambda price:price+price*0.18
print(gst(199))
print(gst(67809))

avg=lambda a,b,c:(a+b+c)/3
print(avg(6,3,4))
print(avg(1,2,3))

largest=lambda a,b,c:a if a>b and a>c else (b if b>c else c)
print(largest(1,2,3))
print(largest(3,6,8))

iseven=lambda a:"even" if a%2==0 else "odd"
print(iseven(4))
print(iseven(7))

isvowel=lambda vowel: "vowel" if vowel in 'aeiouAEIOU' else "conso"
print(isvowel('b'))
print(isvowel('e'))

#map is used to update the list
#add 10 to each elemnt 
l=[1,2,3,4,5,6,7,8]
update=list(map(lambda i:i+10,l))
print(update)

#give discount 30% and write result to all elements
t=(234,678,97,4567,90)
discount=list(map(lambda i:i-i*0.3,t))
print(discount)

#write only odd from list
l=[2,3,4,5,6]
isodd=list(filter(lambda j:j%2!=0,l))
print(isodd)

#write only >100
l=[100,400,500,899,4,6,90]
isgrater=tuple(filter(lambda k:k>100,l))
print(isgrater) 

#print only domain name
l=['kalyani@gmail.com','kalyani@yahoo.com','kalyani@codegnan.com','kalyani@hackerrank.com']
domine=list(map(lambda i:i.split('@')[-1],l))
print(domine)

a='kalyani.chinthamreddy'
b=a.split('.')
print(b)

#sum of elements
#reduce is used to reduce the output in single element it automatically intialize with 1
from functools import reduce
l=[1,2,3,4,5,6,7,88,9]
res = reduce(lambda sum,i:sum+i,l)
print(res)

#product of elements
res1=reduce(lambda pro,i:pro*i,l)
print(res1)
#print avalable seats which are false
seats={'s1':True,
       's2':False,
       's3':True,
       's4':False,
       's5':False}
res=list(filter(lambda i:seats[i]!=True,seats))
print(res)

#print values which are greater than 50
pro={'eggs':80,'sugar':30,'rice':90}
res=list(filter(lambda i:pro[i]>50,pro))
print(res)
#print in assending with values
res=dict(sorted(pro.items(),key=lambda i:i[1]))
print(res)
#decending
print(dict(sorted(pro.items(),key=lambda i:i[1],reverse=True)))


