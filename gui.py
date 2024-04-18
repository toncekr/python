import tkinter as tk
from pillar import generate_pillars, bubble_sort
import time
import random as random

class PillarSortApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pillar Sorting Program")

        # Create GUI elements (menus, buttons, canvas, etc.)
        self.num_pillars_var = tk.StringVar()
        self.num_pillars_var.set("5")  # Default number of pillars
        self.sorting_algorithm_var = tk.StringVar()
        self.sorting_algorithm_var.set("Select sorting algorithm")  # Default sorting algorithm

        self.num_pillars_label = tk.Label(master, text="Number of Pillars:")
        self.num_pillars_label.grid(row=0, column=0)
        self.num_pillars_entry = tk.Entry(master, textvariable=self.num_pillars_var)
        self.num_pillars_entry.grid(row=0, column=1)

        self.sorting_algorithm_label = tk.Label(master, text="Sorting Algorithm:")
        self.sorting_algorithm_label.grid(row=1, column=0)
        self.sorting_algorithm_option = tk.OptionMenu(master, self.sorting_algorithm_var, "Select sorting algorithm")
        self.sorting_algorithm_option["menu"].add_command(label="Bubble Sort", command=lambda: self.sorting_algorithm_var.set("Bubble Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Gnome Sort", command=lambda: self.sorting_algorithm_var.set("Gnome Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Selection Sort", command=lambda: self.sorting_algorithm_var.set("Selection Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Quick Sort", command=lambda: self.sorting_algorithm_var.set("Quick Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Heap Sort", command=lambda: self.sorting_algorithm_var.set("Heap Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Bogo Sort", command=lambda: self.sorting_algorithm_var.set("Bogo Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Cocktail Shaker Sort", command=lambda: self.sorting_algorithm_var.set("Cocktail Shaker Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Insertion Sort", command=lambda: self.sorting_algorithm_var.set("Insertion Sort"))
        self.sorting_algorithm_option["menu"].add_command(label="Radix Sort", command=lambda: self.sorting_algorithm_var.set("Radix Sort"))
        
        self.sorting_algorithm_option.grid(row=1, column=1)

        self.sort_button = tk.Button(master, text="Sort", command=self.start_sorting)
        self.sort_button.grid(row=2, columnspan=2)

        self.canvas = tk.Canvas(master, width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
        self.master.attributes('-fullscreen', True)
        self.canvas.grid(row=3, columnspan=2)

    def draw_pillars(self, pillars):
        self.canvas.delete("all")
        num_pillars = len(pillars)
        pillar_width = self.master.winfo_screenwidth() // num_pillars
        max_height = max(pillars)
        for i, height in enumerate(pillars):
            x0 = i * pillar_width
            y0 = self.master.winfo_screenheight() - (height / max_height) * self.master.winfo_screenheight()
            x1 = (i + 1) * pillar_width
            y1 = self.master.winfo_screenheight()
            if y0 < 0:
                y0 = 0
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")


    def start_sorting(self):
        num_pillars = int(self.num_pillars_var.get())
        sorting_algorithm = self.sorting_algorithm_var.get()

        # Generate pillars
        pillars = generate_pillars(num_pillars)

        # Sort pillars using selected algorithm
        if sorting_algorithm == "Bubble Sort":
            self.bubble_sort_animation(pillars)
        elif sorting_algorithm == "Gnome Sort":
            self.gnome_sort_animation(pillars)
        elif sorting_algorithm == "Selection Sort":
            self.selection_sort_animation(pillars)
        elif sorting_algorithm == "Quick Sort":
            self.quick_sort_animation(pillars)
        elif sorting_algorithm == "Heap Sort":
            self.heap_sort_animation(pillars)
        elif sorting_algorithm == "Bogo Sort":
            self.bogo_sort_animation(pillars)
        elif sorting_algorithm == "Cocktail Shaker Sort":
            self.cocktail_shaker_sort_animation(pillars)
        elif sorting_algorithm == "Insertion Sort":
            self.insertion_sort_animation(pillars)
        elif sorting_algorithm == "Radix Sort":
            self.radix_sort_animation(pillars)

    
    def bubble_sort_animation(self, pillars):
        n = len(pillars)
        for i in range(n):
            for j in range(0, n-i-1):
                if pillars[j] > pillars[j+1]:
                    pillars[j], pillars[j+1] = pillars[j+1], pillars[j]
                    self.draw_pillars(pillars)
                    self.master.update()  # Update the GUI

    def gnome_sort_animation(self, pillars):
        n = len(pillars)
        i = 0
        while i < n:
            if i == 0 or pillars[i] >= pillars[i-1]:
                i += 1
            else:
                pillars[i], pillars[i-1] = pillars[i-1], pillars[i]
                self.draw_pillars(pillars)
                self.master.update()  # Update the GUI
                # Adjust animation speed (in seconds)
                # time.sleep(0.1)
                i -= 1
    def selection_sort_animation(self, pillars):
        n = len(pillars)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if pillars[j] < pillars[min_index]:
                    min_index = j
            pillars[i], pillars[min_index] = pillars[min_index], pillars[i]
            self.draw_pillars(pillars)
            self.master.update()  # Update the GUI
            # Adjust animation speed (in seconds)
            # time.sleep(0.1)

    def quick_sort_animation(self, pillars):
        def partition(pillars, low, high):
            i = low - 1
            pivot = pillars[high]

            for j in range(low, high):
                if pillars[j] < pivot:
                    i += 1
                    pillars[i], pillars[j] = pillars[j], pillars[i]
                    self.draw_pillars(pillars)
                    self.master.update()  # Update the GUI
                    # Adjust animation speed (in seconds)
                    # time.sleep(0.1)

            pillars[i + 1], pillars[high] = pillars[high], pillars[i + 1]
            return i + 1

        def quick_sort(pillars, low, high):
            if low < high:
                pi = partition(pillars, low, high)
                quick_sort(pillars, low, pi - 1)
                quick_sort(pillars, pi + 1, high)

        quick_sort(pillars, 0, len(pillars) - 1)

    def heap_sort_animation(self, pillars):
        def heapify(pillars, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and pillars[i] < pillars[left]:
                largest = left

            if right < n and pillars[largest] < pillars[right]:
                largest = right

            if largest != i:
                pillars[i], pillars[largest] = pillars[largest], pillars[i]
                self.draw_pillars(pillars)
                self.master.update()  # Update the GUI
                # Adjust animation speed (in seconds)
                # time.sleep(0.1)

                heapify(pillars, n, largest)

        n = len(pillars)

        for i in range(n // 2 - 1, -1, -1):
            heapify(pillars, n, i)

        for i in range(n - 1, 0, -1):
            pillars[i], pillars[0] = pillars[0], pillars[i]
            self.draw_pillars(pillars)
            self.master.update()  # Update the GUI
            # Adjust animation speed (in seconds)
            # time.sleep(0.1)

            heapify(pillars, i, 0)

    def bogo_sort_animation(self, pillars):
        def is_sorted(pillars):
            for i in range(1, len(pillars)):
                if pillars[i] < pillars[i-1]:
                    return False
            return True

        while not is_sorted(pillars):
            random.shuffle(pillars)
            self.draw_pillars(pillars)
            self.master.update()  # Update the GUI
            # Adjust animation speed (in seconds)
            # time.sleep(0.1)
    
    def cocktail_shaker_sort_animation(self, pillars):
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
                    self.draw_pillars(pillars)
                    self.master.update()  # Update the GUI
                    # Adjust animation speed (in seconds)
                    # time.sleep(0.1)
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            # Perform a backward pass
            for i in range(end-1, start-1, -1):
                if pillars[i] > pillars[i+1]:
                    pillars[i], pillars[i+1] = pillars[i+1], pillars[i]
                    self.draw_pillars(pillars)
                    self.master.update()  # Update the GUI
                    # Adjust animation speed (in seconds)
                    # time.sleep(0.1)
                    swapped = True

            start += 1

    def insertion_sort_animation(self, pillars):
        n = len(pillars)
        for i in range(1, n):
            key = pillars[i]
            j = i - 1
            while j >= 0 and pillars[j] > key:
                pillars[j + 1] = pillars[j]
                j -= 1
                self.draw_pillars(pillars)
                self.master.update()  # Update the GUI
                # Adjust animation speed (in seconds)
                # time.sleep(0.1)
            pillars[j + 1] = key

    def radix_sort_animation(self, pillars):
        # Find the maximum number to determine the number of digits
        max_num = max(pillars)
        num_digits = len(str(max_num))

        # Perform counting sort for each digit
        for digit in range(num_digits):
            # Initialize count array and output array
            count = [0] * 10
            output = [0] * len(pillars)

            # Count occurrences of each digit
            for num in pillars:
                count[(num // 10**digit) % 10] += 1

            # Calculate cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array
            for i in range(len(pillars) - 1, -1, -1):
                digit_val = (pillars[i] // 10**digit) % 10
                output[count[digit_val] - 1] = pillars[i]
                count[digit_val] -= 1

            # Update the pillars with the sorted values
            pillars = output
            time.sleep(1)

            # Draw the pillars and update the GUI
            self.draw_pillars(pillars)
            self.master.update()
            # Adjust animation speed (in seconds)
            