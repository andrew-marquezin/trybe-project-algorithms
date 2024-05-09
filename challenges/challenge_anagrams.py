def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)


def partition(list, start, end):
    pivot = list[end]
    delimiter = start - 1

    for i in range(start, end):
        if list[i] <= pivot:
            delimiter += 1
            list[i], list[delimiter] = list[delimiter], list[i]

    list[delimiter + 1], list[end] = list[end], list[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    lower_first = list(first_string.lower())
    lower_second = list(second_string.lower())
    quick_sort(lower_first, 0, len(lower_first) - 1)
    quick_sort(lower_second, 0, len(lower_second) - 1)
    sorted_first = "".join(lower_first)
    sorted_second = "".join(lower_second)

    if not first_string or not second_string:
        return (sorted_first, sorted_second, False)

    return (sorted_first, sorted_second, sorted_first == sorted_second)
