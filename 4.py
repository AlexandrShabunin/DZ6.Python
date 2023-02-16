our_list = [6, 7, 6, 8, 1, 1, 7, 7, 2, 3]
print("Исходные элементы списка:\n", our_list)
new_list = [i for i in our_list if our_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)
