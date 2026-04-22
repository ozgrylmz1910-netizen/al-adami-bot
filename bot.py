import tweepy
import google.generativeai as genai
import os
import time

def tweet_at():
    print("--- MAORE BOT OPERASYONU BASLADI ---")
    
    # Render Panelindeki (Fotograftaki) isimlere gore cekiyoruz
    gemini_key = os.getenv("GEMINI_API_KEY")
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    try:
        # Gemini Kurulumu
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("Gemini içerik üretiyor...")
        response = model.generate_content("X (Twitter) için çok kısa ve bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Tweet: {tweet_text}")
        
        # Twitter Kurulumu
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        print("Tweet gönderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Tweet X'e ulaştı! ---")
        
    except Exception as e:
        print(f"!!! KRITIK HATA !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    time.sleep(15)
