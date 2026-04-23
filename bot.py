import tweepy
import google.generativeai as genai
import os
import sys

def start_operation():
    print("\n--- [BAŞLADI] TWEET OPERASYONU ---")
    
    try:
        # 1. Gemini Bağlantısı
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        # En garantili model ismini kullanıyoruz
        model = genai.GenerativeModel('gemini-pro')
        
        print("[1] İçerik üretiliyor...")
        prompt = "X (Twitter) için çok kısa, girişimci ruhlu, etkileyici bir cümle yaz. Sadece metni ver."
        response = model.generate_content(prompt)
        tweet_text = response.text.strip().replace('"', '')
        print(f"[2] Üretilen Tweet: {tweet_text}")

        # 2. Twitter Bağlantısı (OAuth 1.0a)
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # 3. Tweet At
        print("[3] Twitter'a gönderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- [BAŞARILI] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print(f"!!! KRİTİK HATA !!!: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_operation()
