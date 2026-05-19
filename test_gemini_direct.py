import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def test_gemini_direct():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        print(f"API Key found: {api_key[:10]}..." if api_key else "No API key")
        
        genai.configure(api_key=api_key)
        
        # Try different model names
        models_to_try = [
            'gemini-1.5-flash',
            'gemini-1.5-pro',
            'gemini-pro'
        ]
        
        for model_name in models_to_try:
            try:
                print(f"\nTrying model: {model_name}")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Hello, say hi back in one sentence.")
                
                if response and response.text:
                    print(f"✅ {model_name} works!")
                    print(f"Response: {response.text}")
                    return model_name
                else:
                    print(f"❌ {model_name} - Empty response")
                    
            except Exception as e:
                print(f"❌ {model_name} failed: {e}")
        
        print("\n❌ No working models found")
        return None
        
    except Exception as e:
        print(f"❌ General error: {e}")
        return None

if __name__ == "__main__":
    working_model = test_gemini_direct()
    if working_model:
        print(f"\n✅ Use this model: {working_model}")
    else:
        print("\n❌ Gemini API not working")