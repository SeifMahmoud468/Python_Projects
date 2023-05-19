import random
import time
import matplotlib.pyplot as plt

Threshod = 10
kth = 4
def selection_sort(array):
    for i in range(0, len(array)):
        Amin = i
        for j in range(i + 1, len(array)):
            if array[j] < array[Amin]:
                Amin = j
        if i != Amin:
            array[i], array[Amin] = array[Amin],array[i]
def insertion_sort(array):
    for i in range(0, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
def bubble_sort(array):
    for i in range(1, len(array)):
        notsorted = False
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                notsorted = True
        if not notsorted:
            break
def merge_Sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_Sort(left)
        merge_Sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
def partition(array, low, high):
    i = (low - 1)
    n = random.randint(low, high)
    array[high], array[n] = array[n], array[high]
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)
def quick_Help(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
        quick_Help(array, low, pi - 1)
        quick_Help(array, pi + 1, high)
def quick_Sort(array):
    quick_Help(array, 0, len(array) - 1)
def copy(first):
    second = [0] * len(first)
    for i in range(0,len(first)):
        second[i]=first[i]
    return second
def rand(num):
    array = [0] * num
    for i in range(0,num):
        array[i]=random.randrange(200000)
    return array
def hybrid_merge(array):
    if len(array) > Threshod:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_Sort(left)
        merge_Sort(right)
    else:
        quick_Sort(array)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
def find_Kth(array,left,right,k):
    if left == right:
        return array[left]
    pi = partition(array,left,right)
    count = pi - left + 1
    if count == k:
        return array[pi]
    if count > k:
        return find_Kth(array,left,pi-1,k)
    if count < k:
        return find_Kth(array,pi+1,right,k-count)
A=rand(100)
C=copy(A)
B=find_Kth(C,0,len(C)-1,kth)
quick_Sort(A)
print("Main Array: ",A)
print("Kth smallest Elements: ",B)
A=rand(1000)
B=copy(A)
begin = time.time()
hybrid_merge(A)
end = time.time()
print("Hybrid time = ",end-begin)
begin = time.time()
merge_Sort(B)
end = time.time()
print("Merge time = ",end-begin)
x = [100,1000,2500,5000,7500,10000]
n=len(x)
y_merge = [0]*n
y_quick = [0]*n
y_selection = [0]*n
y_insertion = [0]*n
y_bubble = [0]*n
#Report Loop
for i in range(0,n):
    array=rand(x[i])
    print("Round ",x[i])
    # selection sort
    array1 = copy(array)
    begin = time.time()
    selection_sort(array1)
    end = time.time()
    y_selection[i] = end - begin
    print("Selection time: ",y_selection[i]," Sec")
    # insertion Sort
    array2 = copy(array)
    begin = time.time()
    insertion_sort(array2)
    end = time.time()
    y_insertion[i] = end - begin
    print("Insertion time: ",y_insertion[i]," Sec")
    # bubble sort
    array3 = copy(array)
    begin = time.time()
    bubble_sort(array3)
    end = time.time()
    y_bubble[i] = end - begin
    print("Bubble time: ",y_bubble[i]," Sec")
    # merge sort
    array4 = copy(array)
    begin = time.time()
    merge_Sort(array4)
    end = time.time()
    y_merge[i] = end - begin
    print("Merge time:",y_merge[i]," Sec")
    # quick sort
    array5 = copy(array)
    begin = time.time()
    quick_Sort(array5)
    end = time.time()
    y_quick[i] = end - begin
    print("Quick time: ",y_quick[i]," Sec")
plt.plot(x, y_selection, label="Selection Sort")
plt.plot(x, y_insertion, label="Insertion Sort")
plt.plot(x, y_bubble, label="Bubble Sort")
plt.plot(x, y_merge, label="Merge Sort")
plt.plot(x, y_quick, label="Quick Sort")
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken')
plt.title('Sorting Algorithms')
plt.legend()
plt.show()