# -*- coding: utf-8 -*-
"""


@author: sara
"""

#ex1 string
fruit='banana'
let=fruit[2]
print(let)

fruit='banana'
x=2
w=fruit[x-1]
print(w)



#ex2 error
zot='abc'
print(zot[5])


#ex3 def len
fruit='banana'
x=len(fruit)
print(x)


#ex4 len string loop
fruit='banana'
index=0
while index<len(fruit):
    i=fruit[index]
    print(index,i)
    index=index+1
print('done')


#ex5 for
fruit='banana'
for i in fruit:
    print(i)
    
    

#ex6 range
s='mont python'
print(s[0:4]) #0123
print(s[5:20]) #no error


#ex7 change type
x = '40'
y = int(x) + 2
print(y) #42


#ex8 make it uppercase
greet = 'Hello Bob'
print(greet.upper())


#ex9
a='Hello'
b=a+'Sara'
print(b) #HelloSara
c=a +' '+'Sara'
print(c) #Hello Sara



#ex10 in like ==
fruit='banana'
'n' in fruit #output True

if 'ana' in fruit:
    print('yes')
    
    
    
#ex11 capt
a='ABN'
print(str.capitalize(a)) #Abn
 


#ex12
a='ABN'
print(str.lower(a)) #abn



#ex13
a='abc'
print(str.upper(a)) #ABC



#ex14 find
fruit='banana'
pos=fruit.find('na')
print(pos) #2
poss=fruit.find('z')
print(poss) #-1



#ex15  replace
a='hello bob'
srt=a.replace('bob', 'Alex')
print(srt) #hello Alex
srtt=a.replace('o', 'x')
print(srtt) #hellx bxb



#ex16 lstrip rstrip strip
print(str.strip('       Hello     ')) #delete space
print(str.rstrip('    Hello       ')) #delete left space
print(str.lstrip('     Hello   '))   #delete right space



#ex17 startswith
a='Sara Haghighi'
a.startswith('sara') #false
a.startswith('Sara') #True




#ex18 find adv
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3]) #.ma
a=data.find('@')
b=data.find(' ',a)
print(b) #31
print(a) #21
c=data[a+1:b]
print(c) #uct.ac.za




