myset1 = {1,2,3,4,5}

print(myset1)

print(type(myset1))

myset2 = set({4,5,6,76,7,5,34,23})

print(myset2)

for i in myset1:
    print("\t",i)


print(2 in myset1)


check = 4 in myset2

print(check)


myset1.add(4)
print(myset1)

myset1.remove(5)
print(myset1)

myset1.pop()
print(myset1)

myset4 = {5,6,7,8,9,10}

print(myset4)


myset4.pop()
print(myset4)

myset4.remove(6)
print(myset4)

myset4.add(10)
print(myset4)

print(len(myset4))

myset3 = {1,2,3,4}
print(myset3)

myset3.clear()
print(myset3)

myset3 = {1,2,3,4}

myset4.update(myset3)
print(myset4)


newset = myset4.union(myset3)

print(newset)


s1 = {1,2,34,5,6,7}
s2 = {5,6,7,8,89,4}

s1.intersection_update(s2)

print(s1)

s1.intersection(s2)
print(s1)

s4={3,4}
s5={3,4}

# s1.symmetric_differnce_update(s2)

# print(s1)