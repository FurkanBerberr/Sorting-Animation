import matplotlib.pyplot as plt


def partition(low, high, array):
    pivot = array[(low + high) // 2]
    left = low - 1
    right = high + 1
    while True:
        left += 1
        while array[left] < pivot:
            left += 1
        right -= 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            bars = plt.bar(list(range(len(array))), array, color="#BB8FCE")
            bars[left].set_facecolor('red')
            bars[right].set_facecolor('b')
            plt.pause(0.01)
            plt.clf()
            return right

        array[left], array[right] = array[right], array[left]


def quick_sort(low, high, array):
    if low >= 0 and high >= 0 and low < high:
        pivot = partition(low, high, array)
        quick_sort(low, pivot, array)
        quick_sort(pivot + 1, high, array)

