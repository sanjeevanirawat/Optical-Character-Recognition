import streamlit as st 
from PIL import Image
import pytesseract
import numpy as np

# No need to set tesseract_cmd since Render will install it system-wide.

# Set up the Streamlit interface with custom CSS for dark pink color
st.markdown(
    """
    <style>
    /* Set the entire page background color */
    body {
        background-color: #FF69B4;  /* Dark pink background */
        color: white;                /* White text color */
    }

    /* Style for the main container */
    .stApp {
        background-color: #FF69B4;  /* Ensure the app container has a pink background */
    }

    /* Style for file uploader */
    .stFileUploader {
        background-color: white;     /* White background for the file uploader */
        color: black;                /* Black text for the file uploader */
        border-radius: 10px;         /* Rounded corners */
        padding: 10px;              /* Padding for a better look */
    }

    /* Style for buttons and text inputs */
    .stButton, .stTextInput {
        background-color: white;     /* White background for buttons and inputs */
        color: black;                /* Black text for buttons */
        border-radius: 5px;         /* Rounded corners for buttons */
    }

    /* Pink border for input fields */
    .stTextInput {
        border: 1px solid #FF69B4;  /* Pink border for input fields */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title and description
st.title("Image OCR Application")
st.write("Upload an image containing text in Hindi and English, and extract the text.")

# File uploader to upload images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Convert the image to a NumPy array for OCR processing
    img_np = np.array(img)

    # Use pytesseract to extract text from the image (in both Hindi and English)
    st.write("Extracting text...")

    try:
        extracted_text = pytesseract.image_to_string(img_np, lang='eng+hin')  # Specify both English and Hindi languages
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Allow users to search for keywords in the extracted text
        search_query = st.text_input("Enter a keyword to search in the extracted text:")

        if search_query:
            st.write("Search Results:")
            if search_query.lower() in extracted_text.lower():
                highlighted_text = extracted_text.replace(
                    search_query, f"**{search_query}**"
                )
                st.markdown(highlighted_text)
            else:
                st.write("No match found for the keyword.")

    except pytesseract.TesseractNotFoundError:
        st.error("Tesseract is not installed or not found in your system PATH. Please install Tesseract and try again.")
