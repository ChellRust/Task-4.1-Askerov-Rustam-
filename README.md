# Task-4.1-Askerov-Rustam-
#VERY IMPORTANT, you need to install requerment via "pip install -r \PATH.\requerments.txt"
All explanations inside the files.

I have Main directory /src

Directory for html templates /templates

I have dorectory rouse with all python scripts

Inside the /Routes scripts contained in their own directories

!!!!Attention!!!!: for interacting with API you just need to go to "/" endpoint and you will get HTML page with buttons that linked to task endpoints. 

              P.s. Python script with description in it`s own /info directory in /Routes
/src
| _ main.py
| _ /templates
|             | _ "six .html files"
| _ /Routes
           | _ /get
           |        | _ /all
           |        |        | _ get_all.py
           |        | _ /known
           |        |        | _ get_known.py
           |        | _ /new
           |        |        | _ get_new.py
           |        | _ /query
           |                 | _ getquery.py
           | _ /info
                    | _ info.py
