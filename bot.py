import tweepy
import google.generativeai as genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render canli tutma sistemi
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Aktif!")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

def tweet_at():
    while True:
        print("\n--- YENI TWEET OPERASYONU BASLADI ---")
        try:
            # Gemini Baglantisi
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            
            print("Gemini icerik uretiyor...")
            response = model.generate_content("X (Twitter) için çok kısa, etkileyici bir tweet yaz.")
            tweet_text = response.text.strip().replace('"', '')
            print(f"Uretilen Metin: {tweet_text}")

            # Twitter Baglantisi
            client = tweepy.Client(
                consumer_key=os.getenv("X_API_KEY"),
                consumer_secret=os.getenv("X_API_SECRET"),
                access_token=os.getenv("X_ACCESS_TOKEN"),
                access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
            )

            print("Tweet gonderiliyor...")
            res = client.create_tweet(text=tweet_text)
            print(f"--- BASARILI! Tweet ID: {res.data['id']} ---")
            
            print("Islem tamam. 10 dakika sonraki tweet icin bekleniyor...")
            time.sleep(600) # 10 dakika bekle

        except Exception as e:
            print(f"!!! KRITIK HATA !!!: {e}")
            print("Hata alindi, 2 dakika sonra tekrar denenecek...")
            time.sleep(120)

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    tweet_at()
