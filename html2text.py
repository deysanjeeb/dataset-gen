from bs4 import BeautifulSoup
import os
import glob
import csv
# Path to the directory
dir_path = "paulgraham"

# Get a list of all files in the directory
files = glob.glob(os.path.join(dir_path, "*"))
file_path = "metadata.csv"

# Read each file
data=[['file_name', 'original-text','length']]
for file in files:
    if os.path.splitext(file)[1] == ".html":
        with open(file, 'rb') as f:    
            # Create a BeautifulSoup object
            soup = BeautifulSoup(f, 'html.parser')
            # print(soup)
            # Extract the body text
            body_text = soup.body.get_text()

            leng=len(body_text)

            data.append([file, body_text,leng])

with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)