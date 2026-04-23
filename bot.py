import os
import sys
import time
from google import genai
import tweepy

def start_operation():
    print("\n--- [BAŞLADI] YENİ NESİL OPERASYON ---")
    
    try:
        # 1. Yeni Nesil Gemini Bağlantısı
        client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        print("[1] İçerik üretiliyor...")
        response = client_gemini.models.generate_content(
            model="gemini-2.0-flash", 
            contents="X (Twitter) için çok kısa, etkileyici bir motivasyon cümlesi yaz. Sadece metni ver."
        )
        
        tweet_text = response.text.strip().replace('"', '')
        print(f"[2] Üretilen Tweet: {tweet_text}")

        # 2. Twitter Bağlantısı
        client_twitter = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # 3. Tweet At
        print("[3] Twitter'a gönderiliyor...")
        client_twitter.create_tweet(text=tweet_text)
        print("--- [BAŞARILI] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print(f"!!! KRİTİK HATA !!!: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    start_operation()
