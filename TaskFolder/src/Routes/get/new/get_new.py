from fastapi import APIRouter, Request  #Importing fastapi modules 
import json   #Importing JSON
from fastapi.templating import Jinja2Templates     #Importing jinja2 for html hadnling
from fastapi.responses import HTMLResponse    #HTMLResponse is fore returning an HTML page

router_get_new = APIRouter(tags=['Tag for /get/all'])   #Assigning route varuable
templates = Jinja2Templates(directory="src/templates")  #varuable that assigned directory where html page is stored

#Reading and loading data from json file in /src//known_exploited_vulnerabilities.json
with open('src/known_exploited_vulnerabilities.json', 'r') as file:
    data = json.load(file)


extracted_data = [] #preparing varuable with list

#Extracting by loop for in data in enumerated format where max results equel 10
for idx, entry in enumerate(data["vulnerabilities"][:10], start=1):    #data[vulnerabilities] it is dicteonary in json file
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


@router_get_new.get("/get/new/json")    #assigned get request to the "/get/new/json" of the API
def read_json():
    return {"Data": extracted_data}    #return extracted data 


@router_get_new.get("/get/new", response_class=HTMLResponse)    #assigned get request to the "/get/new" of the API
def read_html(request: Request):
    return templates.TemplateResponse(     #templateresponse return html page "get_new.html"
        "get_new.html", 
        {"request": request, "data": extracted_data}  #return extracted data 
    )
