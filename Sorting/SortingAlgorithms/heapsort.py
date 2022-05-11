import matplotlib.pyplot as plt

def heapify(array, length, index):
    largest = index
    left_child = index * 2 + 1
    right_child = index * 2 + 2

    bars = plt.bar(list(range(len(array))), array, color="#BB8FCE")
    bars[largest].set_facecolor('red')
    plt.pause(0.01)
    plt.clf()

    if left_child < length and array[largest] < array[left_child]:
        largest = left_child

    if right_child < length and array[largest] < array[right_child]:
        largest = right_child

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, length, largest)


    bars = plt.bar(list(range(len(array))), array, color="#BB8FCE")
    bars[largest].set_facecolor('red')
    plt.pause(0.01)
    plt.clf()


def heap_sort(array):
    length = len(array)

    for i in range((length-2) // 2, -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)