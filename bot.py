import tweepy
import os
import time

def tweet_at():
    print("--- TEST OPERASYONU BASLADI ---")
    
    # Değişkenleri tek tek çek ve kontrol et
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    # Eğer bir tanesi bile eksikse logda hangisinin eksik olduğunu söyleyecek
    if not all([api_key, api_secret, access_token, access_token_secret, bearer_token]):
        print("!!! HATA: Render panelindeki anahtar isimleri (Environment Variables) eksik veya yanlış!")
        return

    try:
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        print("Twitter'a baglanildi, tweet gonderiliyor...")
        client.create_tweet(text="Sistem baglantisi basarili. Degiskenler artik okunuyor! 🚀")
        print("--- BASARILI: Tweet gonderildi! ---")
        
    except Exception as e:
        print(f"!!! TWITTER HATASI !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    time.sleep(5)
