import tweepy
import google.generativeai as genai
import os

# Render Environment Variables
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

# Gemini Setup
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-pro')

# Twitter Setup
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def tweet_at():
    try:
        response = model.generate_content("X (Twitter) için çok kısa, etkileyici ve bilgece bir tweet yaz. Sadece metni ver.")
        tweet_text = response.text.strip().replace('"', '')
        client.create_tweet(text=tweet_text)
        print(f"Basarili! Tweet: {tweet_text}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    tweet_at()
