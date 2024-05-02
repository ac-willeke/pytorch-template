"""
Main Script

This script servers as the entry point
for the sub-packages and modules of the project.
"""

import logging
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# import local modules
import src.decorators as dec  # noqa
from src.logger import setup_logging  # noqa
from src.config import load_catalog, load_parameters  # noqa

config_file = os.path.join(project_root, "config/logging.yaml")
setup_logger = setup_logging(config_file)
logger = logging.getLogger(__name__)

def main():
    """example main function"""
    import time

    # log project configuration
    logger.info("Starting main script..")
    logger.info("Load catalog  and parameters..")
    
    catalog = load_catalog()
    params = load_parameters()
    
    # test catalog and params
    test_data = catalog["test"]["filepath"]
    epsg = params["EPSG"]["utm32"]
    
    logger.info(f"Test data: {test_data}")
    logger.info(f"EPSG: {epsg}")
    

    @dec.timer
    @dec.dec_logger
    def divide(x, y):
        time.sleep(5)
        result = x / y
        return result

    divide(8, 4)
    divide(10, 0)


if __name__ == "__main__":
    main()
