import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv(".env")
gkey = os.getenv("GOOGLE_KEY")
genai.configure(api_key=gkey)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("hi")
print(response.text)
#TESTING