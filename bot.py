import tweepy
import google.generativeai as genai
import os
import time

# API Bilgileri
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

def tweet_at():
    print("--- OPERASYON BASLADI ---")
    try:
        # Gemini Kurulumu
        genai.configure(api_key=gemini_key)
        
        # 1.5 hata verdigi icin en stabil model olan gemini-pro'ya donduk
        print("Gemini modeline baglaniyor (gemini-pro)...")
        model = genai.GenerativeModel('gemini-pro')
        
        # İçerik Üretme
        response = model.generate_content("X (Twitter) için çok kısa, bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Tweet: {tweet_text}")
        
        # Twitter Kurulumu
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # Tweet Atma
        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- ISLEM TAMAM: Tweet X'e ulasti! ---")
        
    except Exception as e:
        print(f"!!! KRITIK HATA !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    print("Sistem 20 saniye icinde kapanacak...")
    time.sleep(20)
