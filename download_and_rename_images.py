import os
import unicodecsv as csv
import tkinter as tk
import requests
import shutil
from tkinter import filedialog

def main():
    download_and_rename_images()
    

def download_and_rename_images():
    id_col_idx = 0
    url_col_idx = 1
    csv_delimiter = ';'
    
    # loads file
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    if file:
        file_path = os.path.abspath(file)
        current_dir = os.path.dirname(file_path)
    
    # open and store the csv file
    pictures = {}
    with open(file=file, mode='rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=csv_delimiter)
        next(reader)
            
        # fill the dict with key (number) - value (list of image urls)
        for row in reader:
            pictures[row[id_col_idx]] = row[url_col_idx].strip().split("\\n") 
        # print(pictures)
            
        # download images 
        for key in pictures:
            for idx, url in enumerate(pictures[key]):
                if url != "":
                    url = url.split("?")[id_col_idx] # full size
                    # print(key,url)
                    res = requests.get(url, stream = True)
                    
                    if res.status_code == 200:
                        file_name = current_dir + '/' + str(key) + '-' + str(idx+1) + '.jpg'
                        with open(file_name,'wb') as f:
                            shutil.copyfileobj(res.raw, f)
                        print('Image sucessfully Downloaded: ',file_name)
                    else:
                        print('Image Couldn\'t be retrieved')
            

if __name__ == "__main__":
    main()