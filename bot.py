import tweepy
import google.generativeai as genai
import os
import time

# API Anahtarları
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

def tweet_at():
    print("--- Islem Basliyor ---")
    try:
        genai.configure(api_key=gemini_key)
        
        # En garanti model cagirma yontemi
        print("Gemini metin uretiyor...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        response = model.generate_content("X (Twitter) için çok kısa ve etkileyici bir tweet yaz.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Metin: {tweet_text}")
        
        # Twitter Baglantisi
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Tweet gonderildi! ---")
        
    except Exception as e:
        print(f"!!! HATA !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    print("Sistem 20 saniye icinde kapanacak...")
    time.sleep(20)
