import tweepy
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render'ı kandırmak için mecburi sunucuimport tweepy
import os
import time
import random
import schedule
import requests
from dotenv import load_dotenv

load_dotenv()

# X API
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

HF_TOKEN = os.getenv("HF_TOKEN")

# -------------------------
# ÜCRETSİZ AI (HuggingFace)
# -------------------------
def ai_generate(prompt):
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    try:
        return response.json()[0]["generated_text"][:200]
    except:
        return "Stay focused. Stay winning."

# -------------------------
# Tweet at
# -------------------------
def post_tweet():
    try:
        prompt = "Write a short viral tweet about success, money or mindset:"
        tweet = ai_generate(prompt)

        client.create_tweet(text=tweet)
        print("Tweet:", tweet)

    except Exception as e:
        print("Tweet hata:", e)

# -------------------------
# SAFE REPLY (SPAM YOK)
# -------------------------
def safe_reply():
    try:
        query = "success OR money OR AI -is:retweet lang:en"

        tweets = client.search_recent_tweets(query=query, max_results=3)

        if tweets.data:
            for t in tweets.data:
                prompt = f"Reply shortly and smart to this tweet: {t.text}"
                reply = ai_generate(prompt)

                client.create_tweet(
                    text=reply,
                    in_reply_to_tweet_id=t.id
                )

                print("Reply:", reply)

                time.sleep(random.randint(120, 300))  # çok önemli

    except Exception as e:
        print("Reply hata:", e)

# -------------------------
# ZAMANLAMA
# -------------------------
schedule.every(4).hours.do(post_tweet)
schedule.every(6).hours.do(safe_reply)

# -------------------------
# LOOP
# -------------------------
while True:
    schedule.run_pending()
    time.sleep(10)
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
