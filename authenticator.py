import requests
import base64
import json
from loguru import logger

class Authenticator:
    def __init__(self, phone_number, password):
        self.phone_number = phone_number
        self.password = password
        self.session_id = None

    def authenticate(self):
        url = "https://m.vodafone.com.tr/maltgtwaycbu/api/"
        headers = self._get_headers()

        payload = {
            "context": "e30=",
            "username": self.phone_number,
            "method": "twoFactorAuthentication",
            "password": self.password
        }

        response = requests.post(url, headers=headers, data=payload)
        self.session_id = response.json().get('process_id')

        if not self.session_id:
            logger.error("Incorrect password or phone number.")
            raise SystemExit()

        logger.info("Password verification successful.")

    def submit_otp(self, otp_code):
        url = "https://m.vodafone.com.tr/maltgtwaycbu/api/"
        headers = self._get_headers()

        verification_data = {
            "langId": "tr_TR",
            "clientVersion": "17.2.5",
            "reportAdvId": "0AD98FF8-C8AB-465C-9235-DDE102D738B3",
            "pbmRight": "1",
            "rememberMe": "true",
            "sid": self.session_id,
            "otpCode": otp_code,
            "platformName": "iPhone"
        }

        encoded_data = base64.b64encode(json.dumps(verification_data).encode('utf-8'))

        payload = {
            "context": encoded_data,
            "grant_type": "urn:vodafone:params:oauth:grant-type:two-factor",
            "code": otp_code,
            "method": "tokenUsing2FA",
            "process_id": self.session_id,
            "scope": "ALL"
        }

        response = requests.post(url, headers=headers, data=payload)
        return response.json()

    def _get_headers(self):
        return {
            "User-Agent": "VodafoneMCare/2308211432 CFNetwork/1325.0.1 Darwin/21.1.0",
            "Content-Length": "83",
            "Connection": "keep-alive",
            "Accept-Language": "tr_TR",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "m.vodafone.com.tr",
            "Cache-Control": "no-cache",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded"
        }
