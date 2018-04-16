empty_set = set()
print('empty_set ->', empty_set)
alpha = set(('a', 'b', 'c', 'd'))
print('alpha ->', alpha)
dup_list = ['c', 'd', 'c', 'd', 'e', 'f']
beta = set(dup_list)
print('beta ->', beta)
uniq_list = list(beta)
print('uniq_list -> ', uniq_list)

gamma = alpha.union(beta)
print('gamma ->', gamma)
gamma = alpha | beta
print('gamma ->', gamma)

delta = alpha.intersection(beta)
print('delta ->', delta)
delta = alpha & beta
print('delta ->', delta)

epsilon = alpha.difference(beta)
print('epsilon ->', epsilon)
epsilon = alpha - beta
print('epsilon ->', epsilon)

eta = alpha.symmetric_difference(beta)
print('eta ->', eta)
eta = alpha ^ beta
print('eta ->', eta)

print('epsilon.isdisjoint(delta) ->', epsilon.isdisjoint(delta))
print('epsilon.isdisjoint(eta) ->', epsilon.isdisjoint(eta))

print('epsilon.issubset(eta) ->', epsilon.issubset(eta))
print('epsilon.issubset(beta) ->', epsilon.issubset(beta))

print('eta.issuperset(epsilon) ->', eta.issuperset(epsilon))
print('beta.issuperset(epsilon) ->', beta.issuperset(epsilon))

feta = frozenset(eta) # frozen sets are immutabel without updating methods
print('feta ->', feta)


zeta = set()
print('zeta ->', zeta)
zeta.add(3)
print('zeta ->', zeta)
zeta.add(3)
print('zeta ->', zeta)
zeta.add(4)
print('zeta ->', zeta)


print('gamma ->', gamma)
gamma.discard('a')
print('gamma ->', gamma)
gamma.discard('z')
print('gamma ->', gamma)
gamma.remove('b')
print('gamma ->', gamma)
random_element = gamma.pop()
print('random_element ->', random_element)
print('gamma ->', gamma)


zeta_ref = zeta
zeta_copy = zeta.copy()
zeta.clear()
print('zeta ->', zeta)
print('zeta_ref ->', zeta_ref)
print('zeta_copy ->', zeta_copy)

print('alpha -> ', alpha)
alpha_diff = alpha.copy()
alpha_diff.difference_update(beta)
print('alpha_diff ->', alpha_diff)

alpha_intersect = alpha.copy()
alpha_intersect.intersection_update(beta)
print('alpha_intersect ->', alpha_intersect)

alpha_sym_diff = alpha.copy()
alpha_sym_diff.symmetric_difference(beta)
print('alpha_sym_diff ->', alpha_sym_diff)

alpha_union = alpha.copy()
alpha_union.update(beta)
print('alpha_union ->', alpha_union)

a = set(('10', '20', '30', '40'))
b = set(('30', '60'))
print(a)
print(b)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
d = a.difference(b)
print(d)
sd = a.symmetric_difference(b)
print(sd)

a = set(('10', '20', '30', '40'))
b = set(('30', '60'))
print(a)
print(b)
u = a | b
print(u)
i = a & b
print(i)
d = a - b
print(d)
sd = a ^ b
print(sd)


test1 = ['10', '20', '30', '40']
test2 = ['30', '60']
a = set (test1)
b = set(test2)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
d = a.difference(b)
print(d)
sd = a.symmetric_difference(b)
print(sd)