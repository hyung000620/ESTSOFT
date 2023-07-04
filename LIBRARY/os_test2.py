import glob
import os

current_path = os.path.abspath(__file__)


pdf_files = glob.glob("C:\\Users\\dksms\\OneDrive\\Desktop\\**\\*.pdf",recursive=True)

for pdf_file in pdf_files:
    print(pdf_file)