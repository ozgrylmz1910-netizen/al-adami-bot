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
        # Gemini Kurulumu
        genai.configure(api_key=gemini_key)
        
        # En yeni model ismini tırnak içinde veriyoruz
        print("Gemini metin uretiyor...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        response = model.generate_content("X (Twitter) için çok kısa, bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Metin: {tweet_text}")
        
        # Twitter Kurulumu
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Tweet X'e ulasti! ---")
        
    except Exception as e:
        print(f"!!! HATA OLISTU !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    # Logları okuyabilmen için sistemi 20 saniye açık tutar
    print("Sistem 20 saniye icinde kapanacak...")
    time.sleep(20)
