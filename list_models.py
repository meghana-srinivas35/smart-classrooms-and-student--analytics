import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def list_available_models():
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found")
        return
    
    try:
        genai.configure(api_key=api_key)
        
        print("Available Gemini models:")
        print("-" * 30)
        
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                print(f"+ {model.name}")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    list_available_models()