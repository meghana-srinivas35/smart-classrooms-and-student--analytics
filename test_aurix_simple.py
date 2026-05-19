import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.ai_service import AIService

def test_aurix():
    try:
        print("Testing AURIX AI Service...")
        ai = AIService()
        
        # Test basic chat
        response = ai.chat_response("Hello AURIX, how are you?", "student")
        print(f"Success: {response['success']}")
        print(f"Response: {response.get('response', 'No response')}")
        
        if response['success'] and response.get('response'):
            print("✅ AURIX is working correctly!")
        else:
            print("❌ AURIX response is empty or failed")
            print(f"Full response: {response}")
            
    except Exception as e:
        print(f"❌ Error testing AURIX: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_aurix()