import tweepy
import google.generativeai as genai
import os
import time

# Render Environment Variables
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

# Gemini Setup
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Twitter Setup
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def tweet_at():
    print("--- Islem Basliyor ---")
    try:
        print("Gemini metin uretiyor...")
        response = model.generate_content("X (Twitter) için çok kısa, etkileyici ve bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Metin: {tweet_text}")
        
        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Tweet X'e ulasti! ---")
    except Exception as e:
        print(f"!!! HATA OLISTU !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    print("Loglari okumaniz icin 30 saniye bekleniyor...")
    time.sleep(30)
