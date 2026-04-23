import os
import sys
import tweepy

def start_bot():
    print("\n--- [DEDEKTÖR BAŞLADI] ---")
    
    # 1. Render'daki isimleri buraya harf hatasız yazdım
    # Bunların Render panelindeki isimlerle %100 aynı olması lazım
    k_key = os.getenv("X_API_KEY")
    k_secret = os.getenv("X_API_SECRET")
    a_token = os.getenv("X_ACCESS_TOKEN")
    a_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    # Boş anahtar kontrolü
    if not all([k_key, k_secret, a_token, a_token_secret]):
        print("!!! KRİTİK HATA: Render panelindeki isimlerden biri koddakiyle uyuşmuyor!")
        print(f"Kontrol Et: X_API_KEY={bool(k_key)}, X_API_SECRET={bool(k_secret)}")
        return

    try:
        # Twitter'a bağlanmayı dene
        client = tweepy.Client(
            consumer_key=k_key,
            consumer_secret=k_secret,
            access_token=a_token,
            access_token_secret=a_token_secret
        )

        print("[1] Twitter kapısı çalınıyor...")
        client.create_tweet(text="Maore Bot test sürüşü! Bu tweeti görüyorsan başardık baba.")
        print("--- [ZAFER] TWEET HESABA DÜŞTÜ! ---")
        
    except Exception as e:
        print("\n--- !!! TWITTER'DAN GELEN GERÇEK HATA !!! ---")
        print(str(e))
        print("-------------------------------------------\n")

if __name__ == "__main__":
    start_bot()
