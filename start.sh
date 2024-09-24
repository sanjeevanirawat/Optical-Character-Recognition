#!/bin/bash

# Install Tesseract
apt-get update && apt-get install -y tesseract-ocr

# Start the Streamlit app
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
