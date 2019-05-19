import requests
from django.urls import reverse
from django.shortcuts import render
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse, JsonResponse
import json,os,hashlib,io, base64, time, datetime
from requests import Response
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt



#Setting some Variables
Amount = 1
accountReference = "Spacehuru"  #Used for paybills
transactionDescription = "Pay For Listing your Space for 1 month"
consumer_key = "GumpL70YFBHx5G4Dj3UfbwagEVnO4z12"
consumer_secret = "HnAy7hiRGrHn2Tff"
access_token_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
business_short_code = "174379"

#Generating Access Token
r = requests.get(access_token_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
data = r.json()
access_token = "Bearer" + ' ' + data['access_token']

#Generate Password
data = business_short_code + passkey + timestamp
encoded = base64.b64encode(data.encode())
password = encoded.decode('utf-8')

def simulatePayment(PhoneNumber):
    payload = {
        "BusinessShortCode": business_short_code,
        "Password": "{}".format(password),
        "Timestamp": "{}".format(timestamp),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": Amount,
        "PartyA": '254' + PhoneNumber[-9:],
        "PartyB": business_short_code,
        "PhoneNumber": '254' + PhoneNumber[-9:],
        "CallBackURL": "https://darajambili.herokuapp.com/express-payment",
        "AccountReference": accountReference,
        "TransactionDesc": transactionDescription 
    }

    #POPULATING THE HTTP HEADER
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    } 
    initiate_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #
    response = requests.post(initiate_url, json=payload, headers=headers)
    return HttpResponse(response.text)

@method_decorator(csrf_exempt, name='dispatch')
class ListenRequests(View):
    def post(self, request):
        received_json = json.loads(request.body.decode('utf-8'))

        print("REQUEST INFO: ", received_json)

        return HttpResponse(json.dumps({'status': 'ok', 'Data': received_json}))



