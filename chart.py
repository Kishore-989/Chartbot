import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client(api_key=os.getenv("GENAI_API_KEY"))


response=client.models.generate_content( model="gemini-3.6-flash",
                                     contents="Write a short story about virat kohli.")

print(response.text)