import tweepy
from google import genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render'ın "Port" hatası vermemesi için
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
    print("--- MAORE BOT MODERNIZE OPERASYON BASLADI ---")
    try:
        # Yeni Nesil Gemini Bağlantısı
        client_genai = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        print("Yeni Gemini modeliyle metin üretiliyor...")
        response = client_genai.models.generate_content(
            model="gemini-1.5-flash", 
            contents="X (Twitter) için çok kısa, bilgece bir tweet yaz. Sadece metni ver."
        )
        tweet_text = response.text.strip().replace('"', '')
        print(f"Üretilen Tweet: {tweet_text}")

        # Twitter Bağlantısı (Senin panelindeki isimlerle)
        client_twitter = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        print("Tweet gönderiliyor...")
        res = client_twitter.create_tweet(text=tweet_text)
        print(f"--- BAŞARILI: Tweet ID: {res.data['id']} ---")
        
    except Exception as e:
        print(f"!!! HATA DETAYI !!!: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    tweet_at()
    # Botun canlı kalması için
    while True:
        time.sleep(3600)
