s = 'tata consultancy services limited'
list_str = list(s)
print(list_str)
tuple_syn = ('a', 'e','i', 'o','u')
count = 0
while list_str:
    temp = list_str.pop()
    if temp in tuple_syn:
        count += 1
print(count)

s = 'tata consultancy services limited'
list_str = list(s)
list_syn = ['a', 'e', 'i', 'o', 'u']
count = 0
while list_str:
    temp = list_str.pop()
    if temp in list_syn:
        count += 1
print(count)

s = 'tata consultancy services limited'
list_str = list(s)
list_syn = ['a', 'e', 'i', 'o', 'u']
count = 0
while list_str:
    if list_str.pop() in list_syn:
        count += 1
print(count)

s = 'tata consultancy services limited'
list_str = list(s)
count = 0
for val in list_str:
    list_syn = ['a', 'e', 'i', 'o', 'u']
    if val in list_syn:
        count += 1
print(count)


total_average = 68.3
if total_average >= 90:
    print('Distinct')
elif 60 <= total_average < 90:
    print('Above average ')
elif 40 <= total_average < 60:
    print('Average')
else:
    print("Fail")

name = input("First and last name  to reverse ->")
first, last = name .split()
print(first[::-1], last[::-1])

for char in 'Welcome':
    print (char, end='*')
print()