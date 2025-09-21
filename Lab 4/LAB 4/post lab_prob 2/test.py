#updated: get the name of a text file
import tkinter as tk
from tkinter import filedialog  
import os

def get_filename():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    filename = filedialog.askopenfilename(
        title="Select a txt file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    basename = os.path.basename(filename)
    print("Selected file:", basename)
    return filename

if __name__ == "__main__":
    get_filename()