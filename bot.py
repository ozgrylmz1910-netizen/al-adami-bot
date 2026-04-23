import os
import sys
import tweepy
from google import genai

def start_bot():
    print("\n--- [BAŞLADI] FINAL TEST ---")
    
    try:
        # 1. Gemini Ayarı (Yeni Nesil Kütüphane)
        # Not: Render'da GEMINI_API_KEY isimli bir değişkenin olmalı
        gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        print("[1] İçerik üretiliyor...")
        # 1.5-flash kotası en geniş ve en stabil modeldir
        response = gemini_client.models.generate_content(
            model="gemini-1.5-flash",
            contents="X için çok kısa, başarı odaklı bir cümle yaz."
        )
        
        tweet_text = response.text.strip().replace('"', '')
        print(f"[2] Üretilen Tweet: {tweet_text}")

        # 2. Twitter Ayarı
        # Render panelindeki isimlerle birebir aynı olmalı
        twitter_client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # 3. Tweet At
        print("[3] Twitter'a gönderiliyor...")
        twitter_client.create_tweet(text=tweet_text)
        print("--- [TAMAM] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print(f"!!! KRİTİK HATA !!!: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    start_bot()
