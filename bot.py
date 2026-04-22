import tweepy
import google.generativeai as genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Aktif!")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

def start_bot():
    while True:
        print("\n--- [1] BOT TETIKLENDI ---")
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            print("[2] Gemini metni uretiliyor...")
            response = model.generate_content("X icin cok kisa bir tweet yaz.")
            tweet_text = response.text.strip().replace('"', '')
            print(f"[3] Uretilen Metin: {tweet_text}")

            client = tweepy.Client(
                consumer_key=os.getenv("X_API_KEY"),
                consumer_secret=os.getenv("X_API_SECRET"),
                access_token=os.getenv("X_ACCESS_TOKEN"),
                access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
            )
            
            print("[4] Tweet gonderilmeye calisiliyor...")
            res = client.create_tweet(text=tweet_text)
            print(f"--- [OK] BASARILI! Tweet ID: {res.data['id']} ---")
            break # Basarili olursa donguden cik

        except Exception as e:
            print(f"!!! HATA ALINDI: {e}")
            print("30 saniye sonra tekrar denenecek...")
            time.sleep(30)

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    start_bot()
    while True:
        time.sleep(3600)
