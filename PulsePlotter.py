import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import re

def load_raw_file():
    file_path = filedialog.askopenfilename(filetypes=[("Flipper RAW/IR files", "*.sub;*.ir;*.rfid")])
    if not file_path:
        return
    
    pulses = parse_flipper_raw(file_path)
    if not pulses:
        print("Error: No valid data")
        return
    
    plot_pulses(pulses)

def parse_flipper_raw(file_path):
    pulses = []
    reading_data = False
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if "RAW_Data:" in line or "data:" in line:
                numbers = re.findall(r'-?\d+', line)
                if numbers:
                    pulses.extend(map(int, numbers))
    
    print(f"Data: {pulses[:20]}...")
    return pulses

def plot_pulses(pulses):
    if len(pulses) < 2:
        print("Error: We need more data ")
        return

    x = range(len(pulses))
    
    plt.figure(figsize=(10, 4))
    plt.step(x, pulses, where='post', label='Flipper Zero Signal', color='blue')
    plt.xlabel('Time (µs)')
    plt.ylabel('Pulses')
    plt.title('Pulse Plotter - Flipper Zero')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()
    load_raw_file()

if __name__ == "__main__":
    main()
