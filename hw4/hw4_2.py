#не очень понял, что делать с первым числом
old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = list(el for i, el in enumerate(old_list) if el > old_list[i - 1])
del new_list[0]
print(new_list)
