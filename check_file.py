import os

pdf_path = r"C:\Users\chait\OneDrive\Desktop\AIDS\fecus103.pdf"
if os.path.exists(pdf_path):
    print("File exists.")
else:
    print("File does not exist.")
