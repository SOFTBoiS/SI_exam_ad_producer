# SI_exam_ad_producer
This is our ad producer microservice. The goal of this microservice is for a marketing team to send out marketing emails based on a specific audience they want to target. Example would be they've used our [metrics analyzer microservice](https://github.com/SOFTBoiS/SI_exam_kafka_metrics) to figure out who they want to target and then send emails out. 

With this microservice you hit and endpoint with your query and the message you would like to send out in the email. Application connects through gRPC (google RPC) to the monolithic flight application and retrieves all emails based on the query. The ad producer microservice then uses the mails to send out a marketing email with content specified.

## Getting started
### Requirements
- Python 3.7+ 
- [Monolithic flight application](https://github.com/SOFTBoiS/SI_Exam_Monolithic_Flight_Application) up and running on port 44361 using HTTPS
- cURL or Postman to make POST requests

### Running the project
- Clone project and go into directory: ```cd "SI_exam_ad_producer"```
- create virtual environment: ```python3 -m venv venv```
- Activate virtual environment using respective activate file based on your running shell. eg. Powershell: ``` .\venv\Scripts\Activate.ps1``` 
- Install pip packages: ```pip install -r requirements.txt```
- set environment variable FLASK_APP=controllers.py. Eg. in PowerShell: ```$env:"./controllers.py"```
- Run flask: ```flask run```
- POST request on localhost:5000/produce-ads with JSON body:
```
{
    "field": "departureAirport",
    "filter": "CPH",
    "message": "Go to italy for only 299DKK"
}
```