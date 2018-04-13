empty_list = list()
print('empty_list ->', empty_list)

list_str = list('hello')
print('list_str ->', list_str)
list_tup = list((1, 2, (3, 5, 7)))
print('list_tup ->', list_tup)
empty_list = []
print('empty_list ->', empty_list)
list_syn = [3, 4, 'a', 'b']
print('list_syn ->', list_syn)
print("'a' in list syn ->", 'a' in list_syn)
print("1 not in list_syn ->", 1 not in list_syn)
empty_list.append(5)
print('empty_list ->', empty_list)
empty_list.append([6, 7])
print('empty_list.append ->', empty_list)
last_elem = empty_list.pop()
print('last_elem ->', last_elem)
print('empty_list ->', empty_list)
empty_list.extend([6, 7])
print('empty_list.extend ->', empty_list)
first_elem = empty_list.pop(0)
print('first_elem ->', first_elem)
print('empty_list ->', empty_list)
empty_list.insert(0, 10)
print('empty_list.insert ->', empty_list)
empty_list.insert(3, 100)
print('empty_list.insert ->', empty_list)
empty_list.remove(7)
print('empty_list.remove ->', empty_list)
empty_list.clear()
print('empty_list.clear ->', empty_list)
print('list str ->', list_str)
print('min(list str)', min(list_str))
print('max(list str)', max(list_str))
print('sorted(list str)', sorted(list_str))
print('list str ->', list_str)
list_str.sort()
print('list_str ->', list_str)
list_str.reverse()
print('list_str ->', list_str)
print('list_str.count("o") ->', list_str.count("o"))
print('list_str.index("o") ->', list_str.index("o"))

# **********8

emplist1 = list()
print('empist1 ->', emplist1)
emplist1.append(9)
print('emplist1 ->', emplist1)
emplist1.append(10)
print('emplist1 ->', emplist1)
emplist2 = list()
print('empist1 ->', emplist2)
emplist2.extend(['a', 'b', 'c'])
print('emplist2 ->', emplist2)
e = emplist2.remove('c')
print('emplist2 ->', emplist2)
print('e  ->', e)





emplist1 = list()
print(emplist1)
emplist1.append(9)
emplist1.append(10)
print(emplist1)
emplist2 = []
print(emplist2)
emplist2.extend(['a', 'b', 'c'])
print(emplist2)
e = emplist2.pop()
print(emplist2)
print(e)




