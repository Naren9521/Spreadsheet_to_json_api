import uvicorn
from fastapi import FastAPI
import requests
import io
import csv
import re

app = FastAPI()

@app.get("/spreadsheet-to-json")
def convert_spreadsheet_to_json(spreadsheet_url):
    try:
        spreadsheet_id_match = re.search(r"/d/(.*?)/", spreadsheet_url)
        spreadsheet_id = spreadsheet_id_match.group(1)

        sheet_id_match = re.search(r"[#&]gid=(\d+)", spreadsheet_url)
        sheet_id = sheet_id_match.group(1) if sheet_id_match else None

        csv_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={sheet_id}"

        response = requests.get(csv_url)
        csv_file = io.StringIO(response.text)
        csvReader = csv.DictReader(csv_file)
        paragraph = ""
        data = list(csvReader)
        for rows in data:
            if len(rows['Paragraph']) != 0:
                paragraph = ""
                paragraph += rows['Paragraph']
            elif len(rows['Paragraph']) == 0:
                rows['Paragraph'] = paragraph
        for i in data:
            if "" in i.keys():
                i.pop("")

        for i in data:
            if i["Sentence"] == "" and i["CentralNoun"] == "" and i["KeyPhrase"] == "":
                data.remove(i)

        para = data[0]['Paragraph']
        for i in data:
            if i["Paragraph"] != para and i["Paragraph"] == "":
                i.pop("Paragraph")
                i.pop("CentralNoun")
            elif i["Paragraph"] != para:
                para = i["Paragraph"]
                continue
        grouped_data = {}
        for data_dict in data:
            paragraph = data_dict["Paragraph"]
            central_noun = data_dict["CentralNoun"]
            data_dict.pop('Paragraph')
            data_dict.pop('CentralNoun')
            if paragraph in grouped_data:
                grouped_data[paragraph]["Collective_data"].append(data_dict)
            else:
                grouped_data[paragraph] = {
                    "Paragraph": paragraph, "CentralNoun": central_noun, "Collective_data": [data_dict]}

        grouped_data_list = list(grouped_data.values())
        return grouped_data_list
    except:
        try:   
            spreadsheet_id_match = re.search(r"/d/(.*?)/", spreadsheet_url)
            spreadsheet_id = spreadsheet_id_match.group(1)

            sheet_id_match = re.search(r"[#&]gid=(\d+)", spreadsheet_url)
            sheet_id = sheet_id_match.group(1) if sheet_id_match else None

            csv_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={sheet_id}"

            response = requests.get(csv_url)
            csv_file = io.StringIO(response.text)
            csvReader = csv.DictReader(csv_file)
            paragraph = ""
            data = list(csvReader)
            return data
        except Exception as e:
            return "ERROR:NOT ABLE TO PROCESS THE URL"