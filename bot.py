import tweepy
import os
import time

# API Bilgileri (Render'daki Environment Variables)
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

def tweet_at():
    print("--- TEST OPERASYONU BASLADI ---")
    try:
        # Twitter Kurulumu
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # Test Tweeti
        test_mesaji = "Bu bir sistem testidir. Bot artik aktif! 🚀"
        print(f"Gonderilecek mesaj: {test_mesaji}")
        
        client.create_tweet(text=test_mesaji)
        print("--- BASARILI: Test tweeti X'e ulasti! ---")
        
    except Exception as e:
        print(f"!!! TWITTER HATASI !!!: {e}")

if __name__ == "__main__":
    tweet_at()
    time.sleep(10)
