<<<<<<< HEAD

# Spreadsheet to JSON Converter
This is a Python script that provides a FastAPI-based web service to convert data from a Google Sheets spreadsheet to a JSON format. The script uses the FastAPI framework for creating the web application and the Requests library for handling HTTP requests to Google Sheets.


## Requirements
To run the script,you'll need the following:
#### (i) Python 
#### (ii) FastAPI library
#### (iii) Requests library 

## Usage
#### (i) Clone the repository or download the script.
#### (ii) Run the script using the uvicorn command:
#### 'uvicorn script_name:app --reload'

#### (i) The web service will be available at "http://127.0.0.1:8000."

#### (ii) Access the following endpoint in your web browser or through an HTTP client:
"GET http://127.0.0.1:8000/spreadsheet-to-json?spreadsheet_url=<google_sheet_url>"

#### Replace <google_sheet_url> with the URL of the Google Sheets spreadsheet you want to convert to JSON.

#### (i) The script will fetch the data from the specified Google Sheets spreadsheet,process it, and return the JSON data

## How it Works 
#### (i) The script uses FastAPI to create a web service with a single endpoint (/spreadsheet-to-json) that accepts a query parameter spreadsheet_url.

#### (ii)The convert_spreadsheet_to_json function processes the Google Sheets URL and extracts the spreadsheet_id and sheet_id from it.

#### (iii)The function then constructs a CSV URL and makes a request to Google Sheets to fetch the data in CSV format.

#### (iv)The CSV data is read and processed using the csv.DictReader class to get a list of dictionaries containing the data.

#### (v)The function performs some data cleaning and grouping operations to structure the data in a meaningful way.

#### (vi) The final JSON data is returned as a list of dictionaries, where each dictionary represents a paragraph from the Google Sheets spreadsheet along with associated data.

## Error Handling
#### The script handles exceptions that may occur during processing.If there's an issue with the Google Sheets URL or any other error, the script will return an error message:
"ERROR:NOT ABLE TO PROCESS THE URL."

## Note
#### The google spreadsheet must be accessible to everyone.It shouldnt be restricted.
=======
# Proshort2
>>>>>>> 71ea96871b7b7d685cd1e8fad9f24209fb0f1c23
