from bs4 import BeautifulSoup
import os
import glob
import csv
# Path to the directory
dir_path = "samaltman"

# Get a list of all files in the directory
files = glob.glob(os.path.join(dir_path, "*"))
file_path = "metasam.csv"
if os.path.exists(file_path):
    # Open the existing CSV file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        existing_data = list(reader)
    
    for data in existing_data:
        print(data[1])
        data[1]=data[1].replace('\xa0', ' ')
        data[1]=data[1].replace('\n', ' ')
    
    # Write the updated data back to the CSV file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(existing_data)

else:
# Read each file
    data=[['file_name', 'original-text','length']]
    for file in files:
        # if os.path.splitext(file)[1] == ".html":
        with open(file, 'rb') as f:    
            # Create a BeautifulSoup object
            soup = BeautifulSoup(f, 'html.parser')
            # print(soup)
            # Extract the body text
            div = soup.find('div', class_='post-body')
            body_text = div.get_text()

            leng=len(body_text)

            data.append([file, body_text,leng])

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)