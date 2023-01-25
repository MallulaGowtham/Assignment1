Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Online Python compiler (interpreter) to run Python online.
... # Write Python 3 code in this online editor and run it.
... 
... #***************** QUESTION 1 *****************
... ages = [19,22,19,24,20,25,26,24,25,24]
... 
... #Sort the list and find the min and max age
... ages.sort()
... print(ages)
... Min=min(ages)
... Max=max(ages)
... print("Minimum age in the list:",Min)
... print("Maximum age in the list:",Max)
... 
... #Add the min age and the max age again to the list
... 
... ages.append(Min)
... ages.append(Max)
... print(ages)
... 
... #Find the median age (one middle item or two middle items divided by two)
... #calculating index position
... Len=len(ages)
... k=(Len-1)//2
... print(k)
... 
... if(Len%2!=0):
...     print("Median of the list :",ages[k])
... else:
...     print("Median of the list is :",(ages[k]+ages[k+1])//2 )
...     
... #Find the average age (sum of all items divided by their number)
... 
... sum=0
... for i in range (0,len(ages)):
...     sum = sum + ages[i]
... print("The average of the list is :", sum//Len)  

#Find the range of the ages (max minus min)

print ("The range of the list is :", Max-Min)


#***************** QUESTION 2 *****************

#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Cutie'
dog['color'] = 'white'
dog['breed'] = 'Bulldog'
dog['legs'] = '4'
dog['age'] = '1'
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name" : "Tom",
    "last_name" : "David", 
    "gender" : "Male",
    "age" : "23", 
    "marital status" : "Married",
    "skills" : ["reading", "playing"],
    "country" : "us", 
    "city" : "kansas",
    "address" : "Overland Park"
    }
print(student)
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
print(student.get("skills"))
print(type(student.get("skills")))
student['skills'].append('writing')
print(student)
#Get the dictionary keys as a list
print(list(student.keys()))
#Get the dictionary values as a list
print(list(student.values()))

#***************** QUESTION 3 *****************

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine
Sisters= ("Radha" , "Geetha", "Sita")
Brothers= ("Bobby", "Rama", "krishna")
print(Sisters)
print(Brothers)
#Join brothers and sisters tuples and assign it to siblings
Siblings = Sisters + Brothers
print(Siblings)

#How many siblings do you have
k = len(Siblings)
print ( "I have",k,"siblings")

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Family = ("Mahesh","Ria")
family_members = Siblings + Family
print(family_members)

#***************** QUESTION 4 *****************

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print("Length of set it_companies is",len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['TCS','INFOSYS','WIPRO','DXC'])
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove(‘DXC’)
print(it_companies)
#What is the difference between remove and discard
#Join A and B
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print("Is A subset of B:", A.issubset(B))
#Are A and B disjoint sets
print("Are A and B disjoint sets:", A.isdisjoint(B))
#Join A with B and B with A
A|=B
B|=A
print(A,B)
#What is the symmetric difference between A and B
print(("symmetric difference between A and B :", A.symmetric_difference(B)))
#Delete the sets completely
del A
del B
#Convert the ages to a set and compare the length of the list and the set.
m=set(age)
print("the length of list ages ",len(age))
print("the length of set ages ", len(m))

#***************** QUESTION 5 *****************

r=30
_area_of_circle_ = 3.14 * (r * r)
print("Area of circle :", _area_of_circle_)
_circum_of_circle_ = 2 * 3.14 * r
print("Circumference of circle is :", _circum_of_circle_)

r=int(input())
_area_of_circle_ = 3.14 * (r * r)
print("Area of circle with user input is :", _area_of_circle_)

#***************** QUESTION 6 *****************

sentence="I am a teacher and I love to inspire and teach people"
sentence=sentence.split()
set=set(sentence)
print("unique words is:",len(set))

#***************** QUESTION 7 *****************

print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

#***************** QUESTION 8 *****************
radius = 10
area = int(3.14 * radius ** 2)
print("The area of a circle with radius %d is %d meters square."%(radius,area))

#***************** QUESTION 9 *****************

lbs = []
kgs = []

print("enter number of students")
l=int((input()))

for i in range(0,l):
    lbs.append((int(input())))
for k in range(0,l):
    t=round(lbs[k]/2.20462262,2) 
    kgs.append(t)
print(kgs)  
