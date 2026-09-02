#A generator is a function that uses yield to produce values one at a time when needed.
'''def reels():
    data=['1...100',
          '101...200',
          '201...300',
          '301..400']
    for i in data:
        yield i
#res=reels()
print(next(reels()))
print(next(reels()))
print(next(reels()))
print(next(reels()))

#countdown using yeild
def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res=countdown()
for i in res:
    print(i)

#factors of a number using generator
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
res=factors(20)
for i in res:
    print(i)

#prime numbers from 1 to 100 using yield
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i
res=prime(100)
for i in res:
    print(i,end=' ')'''

