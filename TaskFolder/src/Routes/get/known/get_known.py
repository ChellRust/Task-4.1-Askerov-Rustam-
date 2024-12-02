from fastapi import APIRouter, Request   #Importing fastapi modules 
import json    #Importing JSON
from fastapi.templating import Jinja2Templates    #Importing jinja2 for html hadnling
from fastapi.responses import HTMLResponse   #HTMLResponse is fore returning an HTML page
 
router_get_known = APIRouter(tags=['Tag for /get/known'])   #Assigning route varuable
templates = Jinja2Templates(directory="src/templates")  #varuable that assigned directory where html page is stored

#Reading and loading data from json file in /src//known_exploited_vulnerabilities.json
with open('src/known_exploited_vulnerabilities.json', 'r') as file:
    data = json.load(file)

def filter_vulnerabilities_with_ransomware_use():  #def function to filter by knownRansomewareCampingUse that have "known" value
    filtered_vulnerabilities = [
        vuln for vuln in data["vulnerabilities"]
        if vuln.get("knownRansomwareCampaignUse", "").lower() in ["true", "known"]
    ]
    return filtered_vulnerabilities


filtered = filter_vulnerabilities_with_ransomware_use() #Filtered list

extracted_data = []  #preparing varuable with list

# Extract the required fields for each filtered entry
for idx, entry in enumerate(filtered[:40], start=1):
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

@router_get_known.get("/get/known/json") #assigned get request to the "/get/all/json" of the API
def read_json():
    return {"Data": extracted_data}   #return extracted data 

@router_get_known.get("/get/known", response_class=HTMLResponse)   #assigned get request to the "/get/new" of the API
def read_html(request: Request):
    return templates.TemplateResponse(     #templateresponse return html page "get_all.html"
        "get_known.html", 
        {"request": request, "data": extracted_data}   #return extracted data 
    )
