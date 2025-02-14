import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import re

def load_raw_file():
    """Opens a dialog to select a Flipper Zero RAW file and plot its pulses."""
    file_path = filedialog.askopenfilename(filetypes=[("Flipper RAW/IR files", "*.sub;*.ir;*.rfid")])
    if not file_path:
        return
    
    pulses = parse_flipper_raw(file_path)
    if not pulses:
        messagebox.showerror("Error", "No valid data found in the file.")
        return
    
    plot_pulses(pulses)

def parse_flipper_raw(file_path):
    """Parses a Flipper Zero file for RAW signal data."""
    pulses = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if "RAW_Data:" in line or "data:" in line:
                    numbers = re.findall(r'-?\d+', line)
                    if numbers:
                        pulses.extend(map(int, numbers))
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open file: {e}")
        return []
    
    if not pulses:
        print("Warning: No valid data found in the file.")
    else:
        print(f"Data loaded: {pulses[:20]}...")
    
    return pulses

def plot_pulses(pulses):
    """Generates a plot of the pulses extracted from the RAW file."""
    if len(pulses) < 2:
        messagebox.showerror("Error", "More data is needed to plot.")
        return

    x = range(len(pulses))
    
    plt.figure(figsize=(10, 4), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor("#111")
    plt.step(x, pulses, where='post', label='Flipper Zero Signal', color='lime')
    plt.xlabel('Time (µs)', color='white')
    plt.ylabel('Pulses', color='white')
    plt.title('fsociety Signal Intercept', color='red')
    plt.legend()
    plt.grid(color='gray')
    plt.tick_params(colors='white')
    plt.tight_layout()
    plt.show()

def main():
    """Initializes the Tkinter UI for file selection."""
    root = tk.Tk()
    root.withdraw()
    load_raw_file()

if __name__ == "__main__":
    print("Hello, friend. This is just the beginning.")
    main()
