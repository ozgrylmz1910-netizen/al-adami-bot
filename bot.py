import tweepy
import os
import time

def tweet_at():
    print("--- TEST BASLADI ---")
    try:
        # Render'daki Environment Variables'lari cek
        client = tweepy.Client(
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        
        print("Twitter'a mesaj gonderiliyor...")
        client.create_tweet(text="Sistem Testi: Bot aktif ve baglanti kuruldu!")
        print("--- BASARILI: Tweet gonderildi! ---")
        
    except Exception as e:
        print(f"!!! HATA !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    time.sleep(5)
