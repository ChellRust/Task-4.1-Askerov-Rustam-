from fastapi import APIRouter, Request, Query   #Importing fastapi modules 
import json    #Importing JSON
from fastapi.templating import Jinja2Templates  #Importing jinja2 for html hadnling
from fastapi.responses import HTMLResponse  #HTMLResponse is fore returning an HTML page

router_query_filter = APIRouter(tags=['Tag for /get'])  #Assigning route varuable
templates = Jinja2Templates(directory="src/templates")   #varuable that assigned directory where html page is stored
#Reading and loading data from json file in /src//known_exploited_vulnerabilities.json
with open('src/known_exploited_vulnerabilities.json', 'r') as file:
    data = json.load(file)


def filter_by_keyword(keyword: str):   #set that keyword must be a string
    keyword_lower = keyword.lower()   #make words lower for case insensitive filtering
    filtered_results = []  #prepare list
    

    #Extracting by loop for in data in enumerated format
    for idx, entry in enumerate(data["vulnerabilities"], start=1):
        if any(
            keyword_lower in str(value).lower()  #checking if keyword_lower is a substring of the lowercase string
            for value in entry.values() #loop that iterates over each value in the dictionary returned by entry.values().
            if isinstance(value, (str, list))   #checks the type of each value in the dictionary
        ):
            
            filtered_results.append({  #adding internals in filtered_result list
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
    return filtered_results


@router_query_filter.get("/get/json")   #assigned get request to the "/get/json" of the API
def filter_by_query_json(query: str = Query("", description="Keyword to search in the vulnerabilities")):
    filtered_data = filter_by_keyword(query)
    return {"Query": query, "Data": filtered_data}   #return extracted data



@router_query_filter.get("/get", response_class=HTMLResponse)  #assigned get request to the "/get" of the API
def filter_by_query(request: Request, query: str = Query("", description="Keyword to search in the vulnerabilities")):
    filtered_data = filter_by_keyword(query)
    return templates.TemplateResponse(         #return extracted data
        "get_query.html", 
        {"request": request, "data": filtered_data, "query": query}
    )
