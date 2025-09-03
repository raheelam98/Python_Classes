# read some real world data files
# (1) image  (2) csv  (3) live camera
# pandas handle tabular data in Python.

import pandas as pd

print("read some real world data files")
print("\nopen cvs file")
datafram_csv : pd.DataFrame = pd.read_csv("./data1.csv")
print(type(datafram_csv))
print(datafram_csv)
#    id   name education   (output)
# 0   1  Akbar       Msc
# 1   2    Sun       Bsc

print("\nopen imge")
# read image
# pip install matplotlib (terminal)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img = mpimg.imread("cartoonboy1.jpg")# covert into numpy array
# printimage = plt.imshow(img)
# print(type(printimage))
# print(printimage)

# ChatFPT
img = mpimg.imread("cartoonboy1.jpg")  # convert into a numpy array
img_plot = plt.imshow(img)

print(type(img_plot))
#print(img_plot)
plt.show()  # Display the image

print("\nopen pdf")
# open pdf
#  pip install PyPDF2
from typing import List
import PyPDF2

def read_pdf(file_path: str) -> List[str]:
    with open(file_path, 'rb') as file:  # The 'b' in 'rb' stands for binary mode
        reader: PyPDF2.PdfReader = PyPDF2.PdfReader(file)
        text_content: List[str] = [page.extract_text() for page in reader.pages]
        return text_content

pages: list[str] = read_pdf("./mypdf.pdf")
print(pages) 

print("\nopen excel - not working")
#  pip install openpyxl
# datafram_excel : pd.DataFrame = pd.read_excel("./demo.xlsx")
# print(datafram_excel)

# # Assuming you have a file named "demo.xlsx" in the current directory
# excel_file_path = "./demo.xlsx"

# # Read the Excel file into a DataFrame using openpyxl as the engine
# dataframe_excel = pd.read_excel(excel_file_path, engine="openpyxl")

# # Print the contents of the DataFrame
# print(dataframe_excel)

print("\nopen audio file - audio.wav  to do")