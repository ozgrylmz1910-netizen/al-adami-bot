import tweepy
import google.generativeai as genai
import os
import sys

def start_operation():
    print("--- [BAŞLADI] TWEET OPERASYONU ---")
    
    try:
        # 1. Gemini Bağlantısı
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "X (Twitter) için çok kısa, girişimci ruhlu, bilgece bir tweet yaz. Sadece metni ver."
        response = model.generate_content(prompt)
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Tweet: {tweet_text}")

        # 2. Twitter Bağlantısı (OAuth 1.0a - En sağlamı)
        client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

        # 3. Tweet At
        client.create_tweet(text=tweet_text)
        print("--- [BAŞARILI] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print(f"!!! HATA OLUŞTU !!!: {e}")
        sys.exit(1) # Hata varsa Render'a bildir

if __name__ == "__main__":
    start_operation()
