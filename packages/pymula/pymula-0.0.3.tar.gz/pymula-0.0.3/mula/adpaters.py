import json
from datetime import timedelta, datetime

import requests


class MulaAdapter(object):

    SANDBOX_DOMAIN = 'https://beep2.cellulant.com:9212/checkout/v2/custom'
    LIVE_DOMAIN = 'https://online.mula.africa/v2/custom'

    AUTH_PATH = '/oauth/token'
    INITIATE_REQUEST_PATH = '/requests/initiate'
    CHARGE_REQUEST_PATH = '/requests/charge'
    QUERY_STATUS_PATH = '/requests/query-status'

    def __init__(self, client_id, client_secret, service_code):

        self.client_id = client_id
        self.client_secret = client_secret
        self.service_code = service_code
        self.domain = self.SANDBOX_DOMAIN

    def get_access_token(self):
        url  = "{}{}".format(self.domain, self.AUTH_PATH)

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, payload)
        return response.json()['access_token']

    def get_headers(self):
        token = self.get_access_token()
        return {"Authorization": "Bearer {}".format(token)}

    def get_payment_options(self):

        path = self.PAYMENT_OPTIONS_PATH.format(
            client_code=self.client_code,
            country='KE',
            languange='en'
        )
        url = "{}{}".format(self.domain, path)
        token = self.get_access_token()
        response = requests.get(url, auth="Bearer {}".format(token))
        print response

    def checkout_request(self,
                         msisdn,
                         transaction_id,
                         account_number,
                         amount,
                         currency_code='KES',
                         country_code='KE',
                         description='',
                         due_date='',
                         callback_url='',
                         customer_first_name='',
                         customer_last_name='',
                         customer_email=''):
        if not due_date:
            # set due date for tomorrow by default.
            due_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

        payload = {
            "merchantTransactionID": transaction_id,
            "accountNumber": account_number,
            "customerFirstName": customer_first_name,
            "customerLastName": customer_last_name,
            "MSISDN": msisdn,
            "customerEmail": customer_email,
            "requestAmount": amount,
            "currencyCode": currency_code,
            "serviceCode": self.service_code,
            "dueDate": due_date,
            "requestDescription": description,
            "countryCode": country_code,
            "paymentWebhookUrl": callback_url
        }

        url = "{}{}".format(self.domain, self.INITIATE_REQUEST_PATH)
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response.json()

    def charge_request(self,
                       msisdn,
                       transaction_id,
                       checkout_request_id,
                       amount,
                       currency_code='KES',
                       country_code='KE',
                       payer_mode_id=1,
                       language_code='en'):

        payload = {
            "merchantTransactionID": transaction_id,
            "checkoutRequestID": checkout_request_id,
            "chargeMsisdn": msisdn,
            "chargeAmount": amount,
            "currencyCode": currency_code,
            "payerModeID": payer_mode_id,
            "languageCode": language_code,
            "countryCode": country_code
        }

        url = "{}{}".format(self.domain, self.CHARGE_REQUEST_PATH)
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response.json()


    def request_status(self,
                       transaction_id,
                       checkout_request_id):

        payload = {
            "merchantTransactionID": transaction_id,
            "checkoutRequestID": checkout_request_id
        }

        url = "{}{}".format(self.domain, self.QUERY_STATUS_PATH)
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response.json()
