from http.server import HTTPServer, SimpleHTTPRequestHandler # Correctly import HTTPServer
import json
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

PORT = 8000
API_KEY = os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')

print(f"API KEY Found: {API_KEY[:5]}..." if API_KEY else "API KEY Not Found!")

class CloudflareMockHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                request_body = json.loads(post_data)
                message = request_body.get('message')
                country = request_body.get('country')
                currency = request_body.get('currency')

                if not API_KEY:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'API Key not configured on mock server'}).encode())
                    return

                prompt = f"""당신은 프리랜서 시급 추천 전문가입니다. 
현재 선택된 국가: {country}
사용자 질문: {message}

사용자의 업종, 경력, 지역 정보를 바탕으로 적정 시급을 추천해주세요.
추천 시급은 {currency} 기준으로 제시하고, 간단한 설명을 덧붙여주세요.
답변은 친근하고 간결하게 작성해주세요."""

                # Call Gemini API directly (backend-to-backend)
                gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                
                payload = {
                     "contents": [{"parts": [{"text": prompt}]}],
                     "generationConfig": {
                         "temperature": 0.7,
                         "maxOutputTokens": 800,
                     }
                 }

                api_response = requests.post(
                    gemini_url,
                    headers={'Content-Type': 'application/json'},
                    json=payload
                )
                
                self.send_response(api_response.status_code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(api_response.content)

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_error(404)

print(f"Starting server at http://localhost:{PORT}")
httpd = HTTPServer(('localhost', PORT), CloudflareMockHandler)
httpd.serve_forever()
