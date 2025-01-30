
import os
import openai
import glob
# from utils.formatters import format_json_output
# from utils.image_processor import process_image
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import json
import base64
import pytesseract
from PIL import Image
import requests
from openai import OpenAI
# import test
from pydantic import ValidationError
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date
import datetime
import json
from datetime import datetime
import streamlit as st

def ocr_extract(image_path:str ):
  img = Image.open(image_path)
  custom_config = r'--oem 3 --psm 6 -l eng+ita'
  return pytesseract.image_to_string(img, config=custom_config)

def analyze(image_path: str, use_ocr: bool = True):
  extracted_text = None
  if use_ocr:
    extracted_text = ocr_extract(image_path)
  return extracted_text

testo = analyze("images/page_0_copy.jpg", True)
st.write(testo)
