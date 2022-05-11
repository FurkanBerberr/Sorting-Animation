import matplotlib.pyplot as plt


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            bars = plt.bar(list(range(len(lst))), lst, color="#BB8FCE")
            bars[j].set_facecolor('red')
            bars[j+1].set_facecolor('b')
            plt.pause(0.01)
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            if i != n-2:
                plt.clf()
        i -= 1
    plt.show()