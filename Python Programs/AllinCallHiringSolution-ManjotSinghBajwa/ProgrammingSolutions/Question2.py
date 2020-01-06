def my_list(list1, list2):
    list3 = list1 + list2
    set1 = set(list3)
    remove_same = set(list1) & set(list2)
    for i in remove_same:
        set1.remove(i)
    list4 = list(set1)
    print(list4)


A = ['a', 'b', 'cc', 'd', 'e']
B = ['f', 'g', 'cc', 'd', 'h', 'i']

my_list(A, B)
