import tweepy
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render'ı kandırmak için mecburi sunucu
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot Aktif!")
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

if __name__ == "__main__":
    # Sunucuyu hemen başlat
    threading.Thread(target=run_server, daemon=True).start()
    
    print("\n--- TEST BASLIYOR: TWITTER'A BAGLANILIYOR ---")
    
    try:
        # En basit Twitter baglantisi
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )
        
        print("Twitter'a mesaj gonderiliyor...")
        client.create_tweet(text="Bu bir sistem testidir. Bot su an canli!")
        print("--- ZAFER: TWEET GITTI! ---")
        
    except Exception as e:
        print(f"!!! HATA: {e}")

    # Botun kapanmaması için sonsuz bekleme
    while True:
        time.sleep(10)
