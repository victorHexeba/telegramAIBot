import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv(".env")
gkey = os.getenv("GOOGLE_KEY")
genai.configure(api_key=gkey)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("whats the latest in technology as of april 19th 2024")
print(response.text)
