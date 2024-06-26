"""Project configuration"""

import logging
import os
from pathlib import Path

from src.logger import setup_logging
from src.utils import yaml_load

# --------------------------------------------------------------------------- #
# Load catalog and parameters
# --------------------------------------------------------------------------- #
# utils.py allows for loading of .env variables into the .yaml files

# path to yaml project configuration file
project_root = Path(__file__).parents[1]

def load_catalog():
    catalog = os.path.join(project_root, "config/catalog.yaml")
    with open(catalog, "r") as f:
        catalog = yaml_load(f)

    return catalog


def load_parameters():
    parameters = os.path.join(project_root, "config/parameters.yaml")
    with open(parameters, "r") as f:
        parameters = yaml_load(f)
    return parameters

# --------------------------------------------------------------------------- #
# Google Earth Engine (GEE) authentication
# --------------------------------------------------------------------------- #

def ee_authenticate():
    """
    Authenticate with Google Earth Engine GEE.
    
    Generated token and auth info are stored locally at:
    ` ~/.config/earthengine/credentials`.
    Docs: https://developers.google.com/earth-engine/guides/auth
    """
    import ee
    logger = logging.getLogger(__name__)

    try:
        ee.Initialize()
        logger.info("Google Earth Engine initialized successfully.")

    except Exception as e:
        logger.error("Failed to initialize Google Earth Engine: %s", e)
        ee.Authenticate()
        ee.Initialize()
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)


def ee_st_authenticate():
    """
    Authenticate and initialize Google Earth Engine (GEE) for a Streamlit application.
    
    Steps for setting up the token:
    1. Google Cloud > Service Accounts > Choose project > Create key
    2. Ensure the GEE API is enabled for your project (contact your admin).
    3. Export the generated key as a JSON file and store it at `~/.streamlit/credentials.json`.
    4. Convert the JSON file to TOML format.
    5. Upload the TOML file to Streamlit: Streamlit > Settings > Secrets. 
    6. Run your Streamlit app using the command: `streamlit run app.py`.

    Note: Direct use of `ee.Authenticate()` is not compatible with Geemap/Streamlit applications.
    """
    import streamlit as st
    import geemap    

    logger = logging.getLogger(__name__)
    
    try:
        EARTHENGINE_TOKEN = st.secrets["EARTHENGINE_TOKEN"]
        geemap.ee_initialize(token_name=EARTHENGINE_TOKEN)
        logger.info(f"Earth Engine authenticated successfully: {EARTHENGINE_TOKEN}")
    except KeyError:
        logger.error("EARTHENGINE_TOKEN is not set in Streamlit secrets.")
    except Exception as e:
        logger.error(f"An unexpected error occurred during Earth Engine authentication: {e}")
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    # set up logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # load catalog
    logger.info("Loading catalog...")
    catalog = load_catalog()
    parameters = load_parameters()
    logger.info(catalog["project_data"]["filepath"])
