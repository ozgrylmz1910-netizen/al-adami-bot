import tweepy
import google.generativeai as genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render için port bekçisi
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Aktif!")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Sunucu {port} portunda baslatildi.")
    httpd.serve_forever()

def start_bot():
    print("\n--- [1] BOT TETIKLENDI ---")
    
    # 1. Gemini Kismi
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        print("[2] Gemini metni uretiliyor...")
        response = model.generate_content("X için çok kısa bir tweet yaz.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"[3] Uretilen Metin: {tweet_text}")
    except Exception as e:
        print(f"!!! GEMINI HATASI: {e}")
        return

    # 2. Twitter Kismi (OAuth 1.0a - En Garanti Yontem)
    try:
        print("[4] Twitter'a baglaniliyor...")
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )
        
        print("[5] Tweet gonderilmeye calisiliyor...")
        res = client.create_tweet(text=tweet_text)
        print(f"--- [OK] BASARILI! Tweet ID: {res.data['id']} ---")
    except Exception as e:
        print(f"!!! TWITTER HATASI: {e}")

if __name__ == "__main__":
    # Önce sunucuyu başlat (Render kapatmasın)
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    
    # Botu hemen çalıştır
    start_bot()
    
    # Botun açık kalması için bekleme
    while True:
        time.sleep(10)
