import requests
import json

def test_ai_chat():
    try:
        print("Testing AURIX AI Chat...")
        
        response = requests.post('http://localhost:5000/api/ai/chat', 
            json={
                'message': 'Hello AURIX, how are you?',
                'user_id': 'test@example.com',
                'role': 'student',
                'context': 'Test message'
            },
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success') and data.get('message'):
                print("✅ AURIX is working!")
                print(f"AI Response: {data['message']}")
            else:
                print("❌ AURIX returned empty response")
                print(f"Full response: {data}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_ai_chat()