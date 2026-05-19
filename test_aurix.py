import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def test_gemini_connection():
    api_key = os.getenv('GEMINI_API_KEY')
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")
    print(f"API Key (first 10 chars): {api_key[:10] if api_key else 'None'}...")
    
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in environment variables")
        return False
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        print("Testing simple request...")
        response = model.generate_content("Say hello in one word")
        print(f"Success! Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing AURIX/Gemini Connection...")
    print("=" * 40)
    test_gemini_connection()