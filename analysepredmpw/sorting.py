def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    ##More docstring and error handling to follow
    for i, num in enumerate(items):
        try:
            if items[i+1] < num:
                items[i] = items[i+1]
                items[i+1] = num
                bubble_sort(items)
        except IndexError:
            pass
    return items


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    ##More docstring and error handling to follow
    def merge(list1, list2):
        new_list = []
        c1=c2=0
        while c1<len(list1) and c2<len(list2):
            if list1[c1] <= list2[c2]:
                new_list.append(list1[c1])
                c1 += 1
            else:
                new_list.append(list2[c2])
                c2 += 1

        new_list.extend(list1[c1:])
        new_list.extend(list2[c2:])
        return new_list

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    ##More docstring and error handling to follow

    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[-1]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
