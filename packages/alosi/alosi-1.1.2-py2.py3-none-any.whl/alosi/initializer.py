import alosi.bridge_api

from alosi import engine_api
import pprint
import os
from alosi.google_drive import get_service_account_credentials, export_sheet_to_dataframe
from alosi.bridge_api import BridgeApi
import requests
import pandas as pd
import numpy as np

# client email: vpaldata@vpal-data.iam.gserviceaccount.com
SERVICE_ACCOUNT_FILE = os.path.expanduser("~/.keys/vpal-data-6c3bd3f37392.json")
# https://docs.google.com/spreadsheets/d/108oXPDnveafXT45vRBAutCN2faYK7aJlyGVuJSjn5Kc/edit#gid=670969643
FILE_ID = '1_4LBfOe48rSVCtMsMNO8XO6uQYYRGwtbRQBv0te5ydg'

COURSE_CODE = 'HarvardXSPU30x2T2018'

credentials = get_service_account_credentials(SERVICE_ACCOUNT_FILE)


