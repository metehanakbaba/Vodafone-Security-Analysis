import os
import time
import pyfiglet
from loguru import logger
from vodafone_app.module_manager import ModuleManager
from vodafone_app.data_loader import DataLoader
from vodafone_app.authenticator import Authenticator
from vodafone_app.promo_manager import PromoManager

class VodafoneApp:
    def __init__(self):
        self.authenticator = None

    def start(self):
        self.setup_logging()
        ModuleManager.check_module("requests")
        ModuleManager.check_module("pyfiglet")

        logger.info(pyfiglet.figlet_format("requmen"))

        if "VP8" in DataLoader.load_json_data():
            logger.info("@requmeninternet.")
            time.sleep(3)
        else:
            logger.error("Access denied.")
            time.sleep(3)
            raise SystemExit()

        os.system("clear")

        phone_number = input("Enter phone number without 0: ")
        password = input("Enter VF password: ")

        self.authenticator = Authenticator(phone_number, password)
        self.authenticator.authenticate()

        otp_code = input("Enter the OTP code received via SMS: ")
        self.authenticator.submit_otp(otp_code)

        logger.info("Successfully logged in.")
        time.sleep(1)

        self.show_menu()

    def show_menu(self):
        promo_manager = PromoManager(self.authenticator.session_id)

        while True:
            os.system("clear")
            logger.info("What do you want to do?")
            logger.info("\n[1] Get 50GB Promo Internet\n")
            choice = input("Your choice: ")

            if choice == "1":
                logger.info("Getting 50GB internet promo. Can be done once a month.")
                promo_manager.get_promo()
                time.sleep(3)
            else:
                logger.warning("Invalid choice. Please try again.")
                time.sleep(2)

    def setup_logging(self):
        logger.add("vodafone_app.log", rotation="1 MB", level="INFO")

if __name__ == "__main__":
    VodafoneApp().start()
