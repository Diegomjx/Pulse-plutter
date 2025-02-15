# Flipper Zero RAW Signal Plotter

## Description
This project provides a graphical interface to parse and visualize RAW signal data extracted from Flipper Zero files (`.sub`, `.ir`, `.rfid`). The script opens a file selection dialog, extracts pulse data, and plots it in a stylized fsociety-themed graph.

## Features
- Opens Flipper Zero RAW signal files.
- Extracts pulse data from valid `RAW_Data` lines.
- Displays a step plot with a dark cyberpunk aesthetic.
- Uses Tkinter for GUI interaction and Matplotlib for visualization.
- Inspired by *Mr. Robot* aesthetics.

## Requirements
Ensure you have the following Python libraries installed:
```bash
pip install matplotlib numpy tkinter
```

## Usage
Run the script using Python:
```bash
python flipper_plot.py
```
You will be prompted to select a Flipper Zero file. If valid pulse data is found, a plot will be generated.

## File Structure
- `flipper_plot.py` - Main script to load, parse, and visualize Flipper Zero RAW data.


