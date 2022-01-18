import requests
import csv
from bs4 import BeautifulSoup as bs


def extract_item(raw):
    item = raw.text
    item = item.strip()
    item.replace("\"", "")
    return item


def extract_description(base_url, tag):
    url_data_tags = requests.get(base_url+tag)
    soup = bs(url_data_tags.content, 'html.parser')

    tr = soup.find("tr")
    td = tr.find("td")
    description_raw = td.find(id="definition")
    if description_raw:
        description = extract_item(description_raw)
        description = description[description.find('\n'):]
        return description.strip()

    return ""


base_url = "" # DATA URL
url_data_tags = requests.get("//") # DATA additional Tags URL
soup = bs(url_data_tags.content, 'html.parser')

filename = "data_all.csv"
csv_writer = csv.writer(open(filename, 'w'), lineterminator='\n')

csv_writer.writerow(["Name", "Tag", "Type", "Units",
                     "Year", "Description", "Historic"])

for tr in soup.find_all("tr"):
    data = []

    body = tr.find_all("td")

    if body:
        name_raw = body[0]
        tag_raw = body[1]
        type_raw = body[2]
        units_raw = body[3]

        data.append(extract_item(name_raw))
        data.append(extract_item(tag_raw))
        data.append(extract_item(type_raw))
        data.append(extract_item(units_raw))

        if data:
            print("Inserting data: {} ".format(','.join(data)))
            csv_writer.writerow(data)