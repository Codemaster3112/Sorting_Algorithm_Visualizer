import random
import time
speed_val={
    1:0.4,
    2:0.3,
    3:0.2,
    4:0.1,
    5:0

}

class Algorithms():
    def __init__(self, name,size=25,speed=1):
        self.array = random.sample(range(50, 450), size)
        self.name = name
        global speed_val
        self.speed=speed_val[speed]

    def update_screen(self, swap1=None, swap2=None, parse=None, mid=None, end=None, temp=None):
        import sorting_visualizer
        if self.name == "Bubble Sort":
            sorting_visualizer.update_bubblesort(self, swap1, swap2, parse)
        if self.name == "Selection Sort":
            sorting_visualizer.update_selectionsort(self, swap1, swap2, parse)
        if self.name == "Insertion Sort":
            sorting_visualizer.update_insertionsort(self, swap1, swap2, parse)
        if self.name == "Merge Sort":
            sorting_visualizer.update_mergesort(
                self, swap1, swap2, parse, mid, end, temp)
        if self.name == "Quick Sort":
            sorting_visualizer.update_quicksort(
                self, swap1, swap2, parse, mid, end)
        if self.name == "Heap Sort":
            sorting_visualizer.update_heapsort(self, swap1, swap2, parse, mid)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        self.end_time = time.time() - self.start_time
        return self.end_time


class BubbleSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Bubble Sort",size,speed)

    def algorithm(self):
        for i in range(len(self.array)+1):
            for j in range((len(self.array)-1-i)):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j + 1] = self.array[j+1], self.array[j]
                self.update_screen(self.array[j], self.array[j+1], i)
                time.sleep(self.speed)
        if i == len(self.array) or i == len(self.array)+1:
            self.update_screen(self.array[j], self.array[j + 1], i)


class SelectionSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Selection Sort",size,speed)

    def algorithm(self):
        for i in range(len(self.array)+1):

            smallest = i
            if i < len(self.array):
                for j in range(i, len(self.array)):
                    if self.array[j] < self.array[smallest]:
                        smallest = j
                    self.update_screen(self.array[smallest], self.array[j], i)
                    time.sleep(self.speed)
                self.array[smallest], self.array[i] = self.array[i], self.array[smallest]
        if i == len(self.array):
            self.update_screen(swap1=None, swap2=None, parse=i)


class InsertionSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Insertion Sort",size,speed)

    def algorithm(self):

        for i in range(1, len(self.array)):
            temp = self.array[i]
            j = i-1
            while j >= 0 and self.array[j] > temp:
                self.array[j+1] = self.array[j]
                j -= 1
                self.update_screen(i, j, temp)
                time.sleep(self.speed)
            self.array[j+1] = temp
            self.update_screen(i)
            time.sleep(self.speed)


class MergeSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Merge Sort",size,speed)

    def algorithm(self):
        self.merge_sort(0, len(self.array)-1)
        self.update_screen(None, None, None, None, None, [])

    def merge_sort(self, start, end):
        if start < end:
            mid = (start+end)//2
            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)
            self.merge(start, mid, end)

    def merge(self, start, mid, end):
        i = start
        j = mid+1
        temp = []
        while i <= mid and j <= end:
            self.update_screen(i, j, start, mid, end, temp)
            time.sleep(self.speed)
            if self.array[i] < self.array[j]:
                temp.append(self.array[i])
                i += 1
            else:
                temp.append(self.array[j])
                j += 1


        while i <= mid:
            self.update_screen(i, j, start, mid, end, temp)
            time.sleep(self.speed)
            temp.append(self.array[i])
            i += 1

        while j <= end:
            self.update_screen(i, j, start, mid, end, temp)
            time.sleep(self.speed)
            temp.append(self.array[j])
            j += 1

        self.array[start:end+1] = temp
        self.update_screen(None, None, start, mid, end, [])
        time.sleep(self.speed)


class QuickSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Quick Sort",size,speed)

    def algorithm(self):
        start = 0
        end = len(self.array)-1
        self.quick_sort(start, end)

    def sort(self, start, end):
        pivot = start
        i = start
        j = start+1

        while j <= end:
            if self.array[j] < self.array[pivot]:
                i += 1
                self.array[j], self.array[i] = self.array[i], self.array[j]
            self.update_screen(i, j, start, end)
            time.sleep(self.speed)

            j += 1

        self.array[i], self.array[pivot] = self.array[pivot], self.array[i]
        pivot = i
        self.update_screen(i, j, start, end, self.array[pivot])
        time.sleep(self.speed)
        return pivot

    def quick_sort(self, start, end):
        if start <= end:
            pivot = self.sort(start, end)
            self.quick_sort(start, pivot-1)
            self.quick_sort(pivot+1, end)


class HeapSort(Algorithms):
    def __init__(self,size,speed):
        super().__init__("Heap Sort",size,speed)

    def algorithm(self):
        length = len(self.array)
        i = (length-2)//2
        while i >= 0:
            self.heapify(i, length-1, 0)
            i -= 1

        for i in range(len(self.array)):
            self.array[0], self.array[length -1] = self.array[length-1], self.array[0]
            length -= 1
            self.heapify(0, length-1, i)
        self.update_screen(-1,-1,-1, len(self.array)+1)

    def heapify(self, index, end, parse):
        largest = index
        right_child = (index*2)+2
        left_child = (index*2)+1
        if (right_child <= end) and self.array[right_child] > self.array[largest]:
            largest = right_child
        if (left_child <= end) and self.array[left_child] > self.array[largest]:
            largest = left_child
        self.update_screen(index, right_child, left_child, parse)
        time.sleep(self.speed)
        if(index != largest):

            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.heapify(largest, end, parse)


#
# algo=HeapSort()
# print(algo.array)
# x=sorted(algo.array)
# algo.run()
# print(algo.array)
# if x == algo.array:
#     print(True)
