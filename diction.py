# the dic class allows creating an associative array
# of keys and values. Keys ,must be unique immutable objects

empty_dict = dict()
print('empty_dict ->', empty_dict)
empty_dict ={}
print('empty_dict ->', empty_dict)
dict_syn = {'k1': 'v1', 'k2': 'v2'}
print('dict_syn ->', dict_syn)
dict_syn = dict(k1='v1', k2='v2')
print('dict_syn ->', dict_syn)
print("dict_syn['k2'] ->", dict_syn['k2'])
dict_syn['k3'] = 'v3'
print('dict_syn ->', dict_syn)
del(dict_syn['k3'])
print('dict_syn ->', dict_syn)
dict_syn['k1'] = 1
print('dict_syn ->', dict_syn)
dict_syn['k2'] = 2
print('dict_syn ->', dict_syn)

dict_ref = dict_syn
dict_copy = dict_syn.copy()
dict_syn.clear()
print('dict_syn ->', dict_syn)
print('dict_syn ->', dict_ref)
print('dict_copy ->', dict_copy)

key_list = dict_copy.keys()
print('key List ->', key_list)
value_list = dict_copy.values()
print('value_list ->', value_list)
mapping = zip(key_list, value_list)
print('mapping ->', mapping)
dict_new = dict(mapping)
print('dict_new ->', dict_new)

print(" 'k3' in dict_new ->", 'k3' in dict_new)
print(" 'k3' in dict_new ->", 'k3' not in dict_new)

d1 = dict()
print('d1', d1)
d2 = dict(p='play', t='talk')
print('d2', d2)
d2['v'] = 'vibe'
d2['d'] = 'docs'
print('d2', d2)
del(d2['v'])
print('d2', d2)
