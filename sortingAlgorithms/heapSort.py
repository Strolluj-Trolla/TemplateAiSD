def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def heap_restore(lst, index, limit):
    while True:
        left = index*2+1
        right = index*2+2
        if max(left, right) < limit:
            if lst[index] >= max(lst[left], lst[right]):
                return
            elif lst[left]>lst[right]:
                swap(lst, index, left)
                index = left
            else:
                swap(lst, index, right)
                index = right
        elif left < limit:
            if lst[left] > lst[index]:
                swap(lst, index, left)
                index = left
            else:
                return
        elif right < limit:
            if lst[right] > lst[index]:
                swap(lst, index, right)
                index = right
            else:
                return
        else:
            return

def heap_sort(lst):
    for i in range((len(lst)-2)//2, -1, -1):
        heap_restore(lst, i, len(lst))
    print(lst)
    for i in range(len(lst)-1, 0, -1): #i is the index of last element
        swap(lst, 0, i)
        heap_restore(lst, 0, i)