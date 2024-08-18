import requests
from loguru import logger


class PromoManager:
    def __init__(self, session_id):
        self.session_id = session_id

    def get_promo(self):
        url = "https://m.vodafone.com.tr/maltgtwaycbu/api/"
        headers = self._get_promo_headers()

        payload = {
            'method': 'getNetworkPromo',
            'promoType': 'growth',
            'sid': self.session_id
        }

        response = requests.post(url, headers=headers, data=payload)
        result = response.json()

        if result.get("result") == "SUCCESS":
            logger.info("50GB internet promo activated.")
        else:
            logger.error(result.get("resultDesc", "An unknown error occurred."))

        return result

    def _get_promo_headers(self):
        return {
            "Accept": "application/json",
            "Language": "tr",
            "ApplicationType": "1",
            "ClientKey": "AC491770-B16A-4273-9CE7-CA790F63365E",
            "sid": self.session_id,
            "Content-Type": "application/json",
            "Content-Length": "54",
            "Host": "m.vodafone.com.tr",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.10.0"
        }
