
"""name='subhasis mahapatra'
dob='24-04-1997'
password=name[0:4:1]+dob[-4:]
print(password)"""
"""s='bengaluru'
print(type(s))
print(s.capitalize())
s='KASHI'
print(s.lower())"""


"""s='kashi'
print(s.upper())
s='KAShi'
print(s.swapcase())

"""
"""ip='192.168.0.0'
print(ip.startswith('1'))
s='deepmala'
print(s.find ('p'))"""


"""li=[1,2,34,5]
print(li[2])"""
"""li=[1,2,3,4]
print(dir(li))
"""
"""li=[1,2,3,4,56]
li.append(222)
print(li)
li=[1,2,3,4,5,6]
li.insert(3,7)
print(li)"""

"""se={1,2,3,4,5,6,7,8}
print(dir())"""

#data=input('enter your name')
"""num=int(input('enter your num'))
if num%2==0:
    print(num,'even')
else:
    print(num,'odd')

"""
"""st=input('enter your name')
if st==st[::-1]:
    print(st,'pallindrom')
else:
    print(st,'not pallindrom')
"""
"""num=int(input('enter your number'))
if num%2==0 and num%3==0:
    print('num,is div by both 2 & 3')
elif num%2==0:
    print('num,div by 2')
elif num%3==0:
    print('num,div by 3')"""

"""age=int(input('enter your age'))
if age>=18:
    print('go  to voting')
else:
    print('not voting')"""
"""num=int(input('enter ur num'))
if num==1:
    print('monday')
elif num==2:
    print('tuesday')
elif num==3:
    print('wednesday')
elif num==4:
    print('thursday')
elif num==5:
    print('friday')
elif num==6:
    print('saturday')
else:
    print('go for month')
"""
"""city=input('enter your city')
if city=='delhi':
    print('red fort')
elif city=='agra':
    print('taj mahal')
elif city=='jaypur':
    print('jal_mahal')
else:
    print('not any monument')
    

"""
"""wd=int(input('enter ur num day of working day'))
ad=int(input('enter ur  num days of absent day'))
per=(wd-ad)/wd*100

print('ur attendance,per')
if per<75:
    print('is not eligible')
else:
    print('is eligible')
"""
"""li=[1,2,3,4,5]
for var in li:
    print(var)
    add=var+5
print(add)"""
"""for i in range(1,11):
    print(i)"""

"""for i in range(1,11):
    if i%2==0:
        print(i)"""
"""given_number=129475
given_number=str(given_number)
count=0
for i in given_number:
    count+=1
    print(count)"""
"""given_string=input('enter ur string')
reverse_string=''
for i in given_string:

    reverse_string=i+reverse_string
if given_string==reverse_string:
    print('is_pallindrom')
else:
    print('is_not pallindrom')

"""
"""string=input('enter ur string')
reverse_string=''
for i in string:
    reverse_string=i+reverse_string
if reverse_string==string:
    print('is pallindrom')
else:
    print('is not pallindrom')"""


"""print('*')
    print('*',end=' ')
for i in range(2,11,2):
    print('*'*i)
for i in range(5):"""



"""class A:
    def f1(self):
        print('func f1')
    def f2(self):
        print('func f2')
class B(A):
    def f3(self):
        print('func f3')
    def f4(self):
        print('func f4')
obj_a=A()
obj_b=B()
obj_a.f1()
obj_a.f2()
obj_a.f3()

"""
var=open('C:\\Users\\Kashi\\Desktop\\file_handling\\file handling 2.txt','a')
var.write('i am deepmala my daughter name kashi,my husband name is himanshu')

"""data=var.readlines()
print(data)
#data3=var.readlines()
#print(data3)
"""
#var=open('C:\\Users\\Kashi\\Documents\\kashi\\Kashi\\class_1_2_python_introduction.txt','a')
#var.write('i am deepmala i am from maheswar i am 26 yr old\nmy father name pappu\n my mother name is jyoti')
#var.close()
#print(var.closed)



"""import csv
with open('C:\\Users\\Kashi\\Documents\\kashi\\Kashi\\data._csv_write.csv','a',newline='')as file:

    w= csv.writer(file)
    w.writerow(['eno','ename','esalary','eaddr'])
    data=int(input('enter ur employee'))
    for i in range(data):
        eno=int(input('enter ur employee num'))
        ename=input('enter ur employee name')
        esalary=int(input('enter ur employee esalary'))
        eaddr=input('enter ur employee address')
        w.writerow([eno,ename,esalary,eaddr])
print('total employee data entered')"""

import pandas
data={'name':['gourav','vishal','sumit','bishnu'],
'age':[23,25,27,24,25],
'city':['mumbai','pune','kolhapur','banglore','udupur']}
df=pandas.DataFrame(data)
#print(df)

df.to_excel('output.xlsx',index=false)




































































































































































































































































