from SortingAlgorithms.bubblesort import *
from SortingAlgorithms.quicksort import *
from SortingAlgorithms.mergesort import *
from SortingAlgorithms.heapsort import *
import numpy as np

amount = 50

lst = np.random.randint(0, 100, amount)
print(lst)


# bubble_sort(lst)
# quick_sort(0, len(lst) - 1, lst)
merge_sort(lst, 0, len(lst) - 1)
# heap_sort(lst)

bars = plt.bar(list(range(len(lst))), lst, color="#1ABC9C")
plt.show()
print(lst)