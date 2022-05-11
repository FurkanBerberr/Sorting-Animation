import matplotlib.pyplot as plt


def merge_sort(array, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    bars = plt.bar(list(range(len(array))), array, color="#BB8FCE")
    bars[mid].set_facecolor('red')
    plt.pause(0.01)
    plt.clf()

    merge_sort(array, low, mid)
    merge_sort(array, mid+1, high)
    merge(array, low, mid, high)

    bars = plt.bar(list(range(len(array))), array, color="#BB8FCE")
    bars[mid].set_facecolor('red')
    plt.pause(0.01)
    plt.clf()


def merge(array, low, mid, high):
    left_copy = array[low:mid + 1].copy()
    right_copy = array[mid + 1:high + 1].copy()

    left_counter, right_counter, list_counter = 0, 0, low

    while left_counter < len(left_copy) and right_counter < len(right_copy):
        if left_copy[left_counter] <= right_copy[right_counter]:
            array[list_counter] = left_copy[left_counter]
            left_counter += 1
        else:
            array[list_counter] = right_copy[right_counter]
            right_counter += 1
        list_counter += 1

    while left_counter < len(left_copy):
        array[list_counter] = left_copy[left_counter]
        left_counter += 1
        list_counter += 1
    while right_counter < len(right_copy):
        array[list_counter] = right_copy[right_counter]
        right_counter += 1
        list_counter += 1
