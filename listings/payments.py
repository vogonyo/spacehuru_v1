import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse, JsonResponse
import datetime
import time
import base64
import json


#Setting some Variables
Amount = 1
accountReference = "PropertyHuru"  #Used for paybills
transactionDescription = "Pay For Listing your Property for 1 month"
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


#Payload/Body
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
        "CallBackURL": "https://darajambili.herokuapp.com/callback",
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


