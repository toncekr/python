import tkinter as tk
from gui import PillarSortApp
from pillar import generate_pillars, bubble_sort

def main():
    root = tk.Tk()
    app = PillarSortApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
