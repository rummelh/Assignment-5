# Name: Hannah Rummel
# OSU Email: rummelh@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 3/6/2023
# Description: Heap


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """adds a value in the proper position"""
        child_index = self._heap.length()
        self._heap.append(node)
        #adds new element at the end of the arrays
        if self._heap.length() == 1:
            #checks to see if only one item in array
            return
        parent_index = (child_index - 1) // 2
        while child_index >= 0:
            if child_index >= self._heap.length() or child_index < 0:
                return
            if parent_index >= self._heap.length() or parent_index < 0:
                return
            if self._heap[parent_index] > self._heap[child_index]:
                self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
                #swaps values at child and parent index
                child_index = parent_index
                parent_index = (child_index -1) //2
                #recalculate parent index
            else:
                return


    def is_empty(self) -> bool:
        """returns true if heap is empty and False otherwise"""
        if self._heap.length() == 0:
            return True
        else:
            return False

    def get_min(self) -> object:
        """returns smallest value"""
        if self._heap.length() == 0:
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """removes the minimum value from the heap"""
        if self._heap.length() == 0:
            raise MinHeapException
        min_val = self.get_min()
        start_index = 0
        last_element = self._heap[self._heap.length()-1]
        self._heap[start_index] = last_element
        self._heap.remove_at_index(self._heap.length()-1)
        _percolate_down(self._heap,0)
        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """builds a heap"""
        length = da.length()
        copy = DynamicArray()
        for i in range(length):
            copy.append(da[i])
        index = (length //2) - 1
        while index >= 0:
            _percolate_down(copy, index)
            index -=1
        self._heap = copy


    def size(self) -> int:
        """returns size of heap"""
        return self._heap.length()

    def clear(self) -> None:
        """clears contents of heap"""
        self._heap = DynamicArray()

def heapsort(da: DynamicArray) -> None:
    heap = MinHeap()
    heap.build_heap(da)
    counter = da.length()-1
    keep_count = 0
    while counter > 0:
        da[counter], da[0] = da[0], da[counter]
        counter -= 1
        keep_count += 1
        if counter == 1:
            if da[0] > da[1]:
                break
        _percolate_down_help(da, 0, keep_count)




# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """percolates down tree"""
    left_index = (2 * parent) + 1
    right_index = (2 * parent) +2
    parent_index = parent
    while left_index < da.length():
        #checks to make sure not a leaf node
        if left_index < da.length() and right_index < da.length():
            #makes sure both indexes are valid
            if da[left_index] <= da[right_index]:
                #figures out which index should be the candidate for flipping
                min_child = left_index
            else:
                min_child = right_index
            if da[min_child] < da[parent_index]:
                #checks to make sure the min child is smaller than the parent
                da[min_child], da[parent_index] = da[parent_index], da[min_child]
                parent_index = min_child
                left_index = (2 * parent_index) + 1
                right_index = (2 * parent_index) + 2
            elif da[min_child] >= da[parent_index]:
                #need this to make sure exiting if parent is in correct position
                return
        if left_index < da.length() and right_index >= da.length():
            if da[left_index] < da[parent_index]:
                da[left_index], da[parent_index] = da[parent_index], da[left_index]
                parent_index = left_index
                left_index = (2 * parent_index) + 1
                right_index = (2 * parent_index) + 2
            elif da[left_index] >= da [parent_index]:
                return


def _percolate_down_help(da: DynamicArray, parent: int, sub: int) -> None:
    """percolates down tree"""
    left_index = (2 * parent) + 1
    right_index = (2 * parent) +2
    parent_index = parent
    while left_index < da.length()-sub:
        #checks to make sure not a leaf node
        if left_index < da.length()-sub and right_index < da.length()-sub:
            #makes sure both indexes are valid
            if da[left_index] <= da[right_index]:
                #figures out which index should be the candidate for flipping
                min_child = left_index
            else:
                min_child = right_index
            if da[min_child] < da[parent_index]:
                #checks to make sure the min child is smaller than the parent
                da[min_child], da[parent_index] = da[parent_index], da[min_child]
                parent_index = min_child
                left_index = (2 * parent_index) + 1
                right_index = (2 * parent_index) + 2
            elif da[min_child] >= da[parent_index]:
                #need this to make sure exiting if parent is in correct position
                return
        if left_index < da.length()-sub and right_index >= da.length()-sub:
            if da[left_index] < da[parent_index]:
                da[left_index], da[parent_index] = da[parent_index], da[left_index]
                parent_index = left_index
                left_index = (2 * parent_index) + 1
                right_index = (2 * parent_index) + 2
            elif da[left_index] >= da [parent_index]:
                return


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("remove_min my example")
    h = MinHeap([-88078, -8265, -64532, 80428, 63740, -38410, -6778])
    print(h, end = '')
    print(h.remove_min())
    print(h)

    print("remove_min second example")
    h = MinHeap([-54585, -24594, -12853, 42294, 42294, 4547, 73951, 98245])
    print(h, end = '')
    print(h.remove_min())
    print(h)

    print("my heap test")
    da = DynamicArray([89958, -20588, 68338, -25703, -33182])
    h = MinHeap(['zebra', 'apply'])
    h.build_heap(da)
    print(h)

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
