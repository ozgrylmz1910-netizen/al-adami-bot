import os
import sys
import random
import tweepy
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# 1. RENDER'IN KAPANMASINI ÖNLEYEN SUNUCU
def run_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Maore Bot Sorunsuz Calisiyor!")
    
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), Handler)
    httpd.serve_forever()

# 2. TWEET HAVUZU (Gemini yerine buradan rastgele seçer)
TWEET_LISTESI = [
    "Başarı, her gün tekrarlanan küçük disiplinlerin toplamıdır. 🚀",
    "Gelecek, bugünden hazırlananlara aittir. Durmak yok!",
    "Zorluklar, yetenekli insanları ortaya çıkarır. Devam et.",
    "Girişimcilik, kimsenin cesaret edemediği yerlerde fırsat görmektir.",
    "Hata yapmaktan korkmayın, sadece aynı hatayı iki kez yapmaktan korkun.",
    "Sabır ve azim, başarının anahtarıdır. Çalışmaya devam!",
    "Maore ile fark yaratmaya devam ediyoruz. 🛠️",
    "İşine odaklan, gerisi kendiliğinden gelecek."
]

def start_bot():
    print("\n--- [BAŞLADI] TWEET OPERASYONU ---")
    
    try:
        # Twitter Bağlantısı
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # Havuzdan rastgele bir tweet seç
        secilen_tweet = random.choice(TWEET_LISTESI)
        
        print(f"[1] Seçilen Tweet: {secilen_tweet}")
        client.create_tweet(text=secilen_tweet)
        print("--- [TAMAM] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print(f"!!! KRİTİK HATA !!!: {str(e)}")
        # Eğer hata buraya düşerse Twitter API Key'lerini kontrol etmelisin.

if __name__ == "__main__":
    # Render'ı canlı tutacak sunucuyu başlat
    threading.Thread(target=run_server, daemon=True).start()
    
    # İlk tweeti hemen at
    start_bot()
    
    # 4 saatte bir yeni tweet atması için döngü
    while True:
        time.sleep(14400) # 4 Saat bekle
        start_bot()
