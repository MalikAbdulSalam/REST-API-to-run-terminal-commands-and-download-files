# REST API to run terminal command in server and download files from server

**Clone Repository**

**unzip json.zip file**

**Open Terminal and type following command to install necessary libraries of flask**

`pip install -r requirements.txt`

**Open Terminal in and switch to downloaded directory**

**Type follwoing command to start API**

`python REST_api.py` 

*API will be started at http://127.0.0.1:5000 (IP adress may be change according to your PC)*

## For Running Terminal Command

**Open Browser and typ URL http://127.0.0.1:5000 and press enter. Home page will be displayed**

*Type URL http://127.0.0.1:5000/comand_text/<Write Terminal Command Which you want to executer on Server> as given below*

`http://127.0.0.1:5000/comand_text/touch creatNewFile.txt`

*as Output You will see new file created in your downloaded directory*

## For downloading File from server

**Type below given URL**

`http://127.0.0.1:5000/geojson` 

*In the result file will be downloaded to client*
