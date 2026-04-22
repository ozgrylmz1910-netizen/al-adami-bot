import tweepy
import google.generativeai as genai
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render'ın kapanmaması için sahte sunucu
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Aktif")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

def tweet_at():
    print("--- OPERASYON BASLADI ---")
    try:
        # Gemini Baglantisi
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("Icerik uretiliyor...")
        response = model.generate_content("X (Twitter) için çok kısa bir tweet yaz.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Metin: {tweet_text}")

        # Twitter Baglantisi (Senin panelindeki X_ isimlerine gore)
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Tweet gonderildi! ---")
        
    except Exception as e:
        print(f"!!! KRITIK HATA !!!: {e}")

if __name__ == "__main__":
    # Arka planda sunucuyu ac
    threading.Thread(target=run_server, daemon=True).start()
    
    # Tweeti gonder
    tweet_at()
    
    # Render'in botu oldurmemesi icin sonsuz dongu
    while True:
        time.sleep(3600)
