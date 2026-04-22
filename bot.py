import tweepy
import google.generativeai as genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render port hatasını çözmek için mini sunucu
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Calisiyor!")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

def tweet_at():
    print("--- MAORE BOT OPERASYONU BASLADI ---")
    try:
        # 1. Gemini İçerik Üretme
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        print("Gemini metin yazıyor...")
        response = model.generate_content("X (Twitter) için çok kısa, bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Tweet: {tweet_text}")

        # 2. Twitter Bağlantısı (OAuth 1.0a - En Garanti Yöntem)
        auth = tweepy.OAuth1UserHandler(
            os.getenv("X_API_KEY"), 
            os.getenv("X_API_SECRET"), 
            os.getenv("X_ACCESS_TOKEN"), 
            os.getenv("X_ACCESS_TOKEN_SECRET")
        )
        api = tweepy.API(auth)
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # 3. Tweet Gönderme
        print("Tweet X'e gonderiliyor...")
        # V2 API kullanarak tweet atıyoruz
        res = client.create_tweet(text=tweet_text)
        print(f"--- BASARILI: Tweet ID: {res.data['id']} ---")
        
    except Exception as e:
        print(f"!!! KRITIK HATA !!!: {e}")

if __name__ == "__main__":
    # Port hatasını engellemek için sunucuyu başlat
    threading.Thread(target=run_server, daemon=True).start()
    
    # Tweeti at
    tweet_at()
    
    # Botun kapanmaması için döngü
    while True:
        time.sleep(3600)
