import tkinter as tk
from tkinter import ttk
import random
import time

# Function to draw the bars representing the array
def draw_bars(array, color_array):
    canvas.delete("all")  # Clear the canvas
    c_width = 800
    c_height = 400
    bar_width = c_width / len(array)  # Width of each bar

    for i, height in enumerate(array):
        x0 = i * bar_width
        y0 = c_height - height
        x1 = (i + 1) * bar_width
        y1 = c_height
        # Draw the rectangle (bar)
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

    root.update_idletasks()  # Refresh the GUI

# Bubble Sort Algorithm
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_bars(array, ["green" if x == j or x == j + 1 else "blue" for x in range(len(array))])
                time.sleep(speed.get())

# Selection Sort Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        draw_bars(array, ["green" if x == i or x == min_index else "blue" for x in range(len(array))])
        time.sleep(speed.get())

# Quick Sort Algorithm
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            draw_bars(array, ["green" if x == i or x == j else "blue" for x in range(len(array))])
            time.sleep(speed.get())
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Generate a random list of numbers
def generate_array():
    global array
    array = [random.randint(10, 390) for _ in range(int(size_entry.get()))]
    draw_bars(array, ["blue" for _ in range(len(array))])

# Start the sorting process
def start_sorting():
    if algorithm_menu.get() == "Bubble Sort":
        bubble_sort(array)
    elif algorithm_menu.get() == "Selection Sort":
        selection_sort(array)
    elif algorithm_menu.get() == "Quick Sort":
        quick_sort(array, 0, len(array) - 1)

# Create the main window
root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("900x600")

# Create a canvas to draw bars
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack(pady=20)

# Frame for controls
frame = tk.Frame(root)
frame.pack()

# Algorithm selection dropdown
algorithm_menu = ttk.Combobox(frame, values=["Bubble Sort", "Selection Sort", "Quick Sort"])
algorithm_menu.grid(row=0, column=0, padx=10)
algorithm_menu.current(0)

# Entry to set array size
size_entry = tk.Entry(frame)
size_entry.grid(row=0, column=1, padx=10)
size_entry.insert(0, "50")

# Start button
start_button = tk.Button(frame, text="Start Sorting", command=start_sorting)
start_button.grid(row=0, column=2, padx=10)

# Speed scale
speed = tk.DoubleVar()
speed_slider = tk.Scale(frame, from_=0.01, to=1.0, length=200, digits=2, resolution=0.01, orient=tk.HORIZONTAL, label="Speed [seconds]")
speed_slider.grid(row=0, column=3, padx=10)
speed_slider.set(0.1)

# Generate array button
generate_button = tk.Button(frame, text="Generate Array", command=generate_array)
generate_button.grid(row=0, column=4, padx=10)

# Initialize and run the application
root.mainloop()
