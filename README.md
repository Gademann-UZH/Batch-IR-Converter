# Batch IR Converter

This script can be used for the batch extraction of IR spectra from machine generated PDFs and conversion into text. It's especially usefull when preparing manuscripts and theses and can save you hours of tedious work.

The converter consists of a python script which does all the work for you and can be run from the command line.

Necessary python modules are:

- pdftotext
- tkinter

In case you are on a Mac you can also run the script via double-clicking the Bash file "convert_spectra.command".

## Workflow

After you download the IRConverter and you ensured that all necessary modules are installed, you can create a second folder in which you place all spectra you want to convert. Then you run the script and first pick the folder with all spectra, then a folder were the output.txt file should be saved. This can be the same folder. As soon as you choose the second folder the program will start to convert all spectra, order them alphanumerically, and generate a output.txt file.