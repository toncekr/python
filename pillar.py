import random

def generate_pillars(num_pillars):
    return random.sample(range(1, num_pillars + 1), num_pillars)

def bubble_sort(pillars):
    n = len(pillars)
    for i in range(n):
        for j in range(0, n-i-1):
            if pillars[j] > pillars[j+1]:
                pillars[j], pillars[j+1] = pillars[j+1], pillars[j]
    return pillars

def selection_sort(pillars):
    n = len(pillars)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if pillars[j] < pillars[min_index]:
                min_index = j
        pillars[i], pillars[min_index] = pillars[min_index], pillars[i]
    return pillars

def gnome_sort(pillars):
    i = 0
    while i < len(pillars):
        if i == 0 or pillars[i-1] <= pillars[i]:
            i += 1
        else:
            pillars[i], pillars[i-1] = pillars[i-1], pillars[i]
            i -= 1
    return pillars

def quick_sort(pillars):
    if len(pillars) <= 1:
        return pillars
    pivot = pillars[0]
    lesser = [x for x in pillars[1:] if x <= pivot]
    greater = [x for x in pillars[1:] if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


def heapify(pillars, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and pillars[i] < pillars[l]:
        largest = l

    if r < n and pillars[largest] < pillars[r]:
        largest = r

    if largest != i:
        pillars[i], pillars[largest] = pillars[largest], pillars[i]
        heapify(pillars, n, largest)

def heap_sort(pillars):
    n = len(pillars)

    for i in range(n, -1, -1):
        heapify(pillars, n, i)

    for i in range(n-1, 0, -1):
        pillars[i], pillars[0] = pillars[0], pillars[i]
        heapify(pillars, i, 0)

    return pillars

def bogo_sort(pillars):
    while not is_sorted(pillars):
        random.shuffle(pillars)
    return pillars

def is_sorted(pillars):
    n = len(pillars)
    for i in range(1, n):
        if pillars[i] < pillars[i-1]:
            return False
    return True

def cocktail_shaker_sort(pillars):
    n = len(pillars)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Perform a forward pass
        for i in range(start, end):
            if pillars[i] > pillars[i+1]:
                pillars[i], pillars[i+1] = pillars[i+1], pillars[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Perform a backward pass
        for i in range(end-1, start-1, -1):
            if pillars[i] > pillars[i+1]:
                pillars[i], pillars[i+1] = pillars[i+1], pillars[i]
                swapped = True

        start += 1

    return pillars


def insertion_sort(pillars):
    n = len(pillars)
    for i in range(1, n):
        key = pillars[i]
        j = i - 1
        while j >= 0 and key < pillars[j]:
            pillars[j + 1] = pillars[j]
            j -= 1
        pillars[j + 1] = key
    return pillars


def radix_sort(pillars):
    # Find the maximum number to determine the number of digits
    max_num = max(pillars)
    
    # Perform counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(pillars, exp)
        exp *= 10
    
    return pillars

def counting_sort(pillars, exp):
    n = len(pillars)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = pillars[i] // exp
        count[index % 10] += 1
    
    # Change count[i] so that count[i] contains the actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = pillars[i] // exp
        output[count[index % 10] - 1] = pillars[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the output array to pillars[] so that pillars[] contains
    # sorted numbers according to the current digit
    for i in range(n):
        pillars[i] = output[i]

