import os

def get_data_from_pdf(input):
    with open(input, "rb") as f:
        pdf = pdftotext.PDF(f)
    
    txt = []
    for page in pdf:
        line = page.split()
        txt.append(line)

    txt.pop(0)

    data = {}
    max_v = 0
    min_v = 100
    for page in txt:
        for i, word in enumerate(page):
            if word == "(%T)":
                a = i + 1
            
            elif word == "Seite":
                b = i

        for i in range(a, b):
            if i % 3 == 0:
                data[page[i]] = {}
                data[page[i]]["wn"] = int(round(float(page[i + 1]), 0))

                transmittance = float(page[i + 2])
                data[page[i]]["t"] = transmittance

                if 100 - transmittance < min_v:
                    min_v = 100 - transmittance
                
                if 100 - transmittance > max_v:
                    max_v = 100 - transmittance
    
    output = ""

    keys = list(data.keys())
    for key in keys:

        v = 100 - data[key]["t"]

        if v > max_v * 0.75:
            suffix = "s"
        elif v > max_v * 0.25:
            suffix = "m"
        else:
            suffix = "w"


        if key != keys[len(keys) - 1]:
            output += str(data[key]["wn"]) + suffix + ", "
        else:
            output += str(data[key]["wn"]) + suffix + " cm-1.\n\n\n"

    return output


def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst ]
    return lst

#----------------------------------------------------------------------------------------------------------#

if os.system("python --version") != 0:
    print("\nYou need to install python")

if os.system("python -c 'import pdftotext'") != 0:
    print("\nYou need to install the pdftotext module")

if os.system("python -c 'import tkinter'") != 0:
    print("\nYou need to install the tkinter module")

import pdftotext
import tkinter as tk
from tkinter import filedialog

# Open a file
root = tk.Tk()
root.withdraw()

print("\nSelect a folder containing IR Files to convert")
path = filedialog.askdirectory()
if os.path.isdir(path) == False:
    quit()

print("\nSelect a folder to save the output file\n")
home = filedialog.askdirectory()
if os.path.isdir(home) == False:
    quit()

dirs = os.listdir( path )

dirs = sort(dirs)
entry = ""

# This would print all the files and directories
for file in dirs:
    os.chdir(path)
    if file[0] != ".":
        entry = get_data_from_pdf(file)
    os.chdir(home)
    if entry != "":
        with open("out.txt", "a") as op:
            op.write(file + ":\n\n")
            op.write(entry)