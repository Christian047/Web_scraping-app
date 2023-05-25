# Build an application that extracts phone number, email and link from a website and stores them in a separate file
import re
import requests
import csv



Url = input("Which web page do you want to scrape? :")
# use requests module to access the site
response = requests.get(Url)
# convert response to text
my_text_url = response.text

# we use regular expressions to extract the phone number, email, and link.
scrape =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b|\b(?:https?://|www\.)\S+\b|\b(?:\+\d{1,3}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"

Data = re.findall(scrape, my_text_url)



# We output the extracted data to a csv file
with open('Data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data'])
    writer.writerows([[data] for data in Data])

print("Completed,your file can be found at'Data.csv'.")