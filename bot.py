import tweepy
import google.generativeai as genai
import os
import time

def tweet_at():
    print("--- MAORE BOT FINAL DENEME ---")
    
    # Render Panelindeki isimler
    gemini_key = os.getenv("GEMINI_API_KEY")
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    try:
        # Gemini Kurulumu
        genai.configure(api_key=gemini_key)
        
        # 1.5 Flash hata verdigi icin en garanti model olan gemini-pro'yu kullaniyoruz
        print("Gemini baglantisi kuruluyor (Model: gemini-pro)...")
        model = genai.GenerativeModel('gemini-pro')
        
        print("Icerik uretiliyor...")
        response = model.generate_content("X (Twitter) için çok kısa, etkileyici bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        print(f"Uretilen Metin: {tweet_text}")
        
        # Twitter Kurulumu
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        print("Tweet gonderiliyor...")
        client.create_tweet(text=tweet_text)
        print("--- BASARILI: Islem Tamamlandi! ---")
        
    except Exception as e:
        print(f"!!! KRITIK HATA !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    time.sleep(10)
