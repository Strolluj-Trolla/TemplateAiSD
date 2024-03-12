def selection_sort(lst):
    for i in range(len(lst)-1):
        min = i
        for j in range(i+1, len(lst), 1):
            if lst[j] < lst[min]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]