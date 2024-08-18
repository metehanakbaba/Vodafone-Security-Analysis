import subprocess
import sys
from loguru import logger

class ModuleManager:
    @staticmethod
    def install_module(module_name):
        logger.info(f"Installing {module_name} module...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

    @staticmethod
    def check_module(module_name):
        try:
            __import__(module_name)
            logger.info(f"{module_name} module is already installed.")
        except ImportError:
            logger.warning(f"{module_name} module not found. Installing...")
            ModuleManager.install_module(module_name)
