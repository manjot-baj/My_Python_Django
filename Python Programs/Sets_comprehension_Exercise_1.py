# We do not use Set Comprehension much but it is simple
set1 = {k**2 for k in range(1,11)}
print(set1)
# output: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

names = {"Manjot","Singh","Bajwa"}
names1 = {name[0] for name in names}
print(names1)
# output : {'M', 'S', 'B'}