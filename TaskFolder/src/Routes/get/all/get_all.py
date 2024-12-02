from fastapi import APIRouter, Request    #Importing fastapi modules 
import json    #Importing JSON
from fastapi.templating import Jinja2Templates   #Importing jinja2 for html hadnling
from fastapi.responses import HTMLResponse   #HTMLResponse is fore returning an HTML page
from datetime import datetime   #Importing datetime module

router_get_all = APIRouter(tags=['Tag for /get/all'])    #Assigning route varuable
templates = Jinja2Templates(directory="src/templates")   #varuable that assigned directory where html page is stored

#Reading and loading data from json file in /src//known_exploited_vulnerabilities.json
with open('src/known_exploited_vulnerabilities.json', 'r') as file:
    data = json.load(file)
#Converting the input strings start_date_str and end_date_str into datetime objects using strptime
def filter_vulnerabilities_by_date_range(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    #Filtering by date in list
    filtered_vulnerabilities = [
        vuln for vuln in data["vulnerabilities"]
        if start_date <= datetime.strptime(vuln["dateAdded"], "%Y-%m-%d") <= end_date
    ]
    return filtered_vulnerabilities


filtered = filter_vulnerabilities_by_date_range("2024-11-21", "2024-11-25")  #Filtered list

extracted_data = []#preparing varuable with list

#Extracting by loop for in data in enumerated format where max results equel 40
for idx, entry in enumerate(filtered[:40], start=1):    #data[vulnerabilities] it is dicteonary in json file
    extracted_data.append({
        'Number': idx,
        'cveID': entry.get('cveID', ''),
        'vendorProject': entry.get('vendorProject', ''),
        'product': entry.get('product', ''),
        'vulnerabilityName': entry.get('vulnerabilityName', ''),
        'dateAdded': entry.get('dateAdded', ''),
        'shortDescription': entry.get('shortDescription', ''),
        'requiredAction': entry.get('requiredAction', ''),
        'dueDate': entry.get('dueDate', ''),
        'knownRansomwareCampaignUse': entry.get('knownRansomwareCampaignUse', ''),
        'notes': entry.get('notes', ''),
        'cwes': entry.get('cwes', [])
    })

@router_get_all.get("/get/all/json")   #assigned get request to the "/get/all/json" of the API
def read_json():
    return {"Data": extracted_data}   #return extracted data 


@router_get_all.get("/get/all", response_class=HTMLResponse)    #assigned get request to the "/get/new" of the API
def read_html(request: Request):
    return templates.TemplateResponse(     #templateresponse return html page "get_all.html"
        "get_all.html", 
        {"request": request, "data": extracted_data}  #return extracted data 
    )