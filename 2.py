result_list1 = []
list1 = [(w) for w in input("Введите список чисел для исходного списка: ").split()]
for w in range(1, len(list1)):
    if list1[w] > list1[w - 1]:
        (result_list1.append(list1[w]))
print("Исходный список чисел: ", list1)
print("Список, элементы которого больше предыдущего элемента: ", result_list1)
