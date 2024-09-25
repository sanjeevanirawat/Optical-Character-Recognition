#!/bin/bash

# Install Tesseract OCR
apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-hin

# Start the Streamlit application
streamlit run app.py
