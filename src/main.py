import time
import json
import tweepy
import requests
import schedule
from datetime import datetime

auth = tweepy.OAuth1UserHandler("{}", "{}") # Add your own api credentials here
auth.set_access_token("{}", "{}") # Add your own api credentials here
tweepy.OAuth1UserHandler
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def call():
    while True:
        utc_time_date = datetime.utcnow().strftime("%H:%M:%S")

        url_general_market_data = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false')
        general_market_data = json.loads(url_general_market_data.text)

        url_different_currencies = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd%2Cgbp%2Ceur%2Ccny')
        different_currencies = json.loads(url_different_currencies.text)

        xrp_usd = different_currencies['ripple']['usd']
        xrp_gbp = different_currencies['ripple']['gbp']
        xrp_eur = different_currencies['ripple']['eur']
        xrp_cny = different_currencies['ripple']['cny']

        daily_high = general_market_data[0]['high_24h']
        daily_low = general_market_data[0]['low_24h']
        daily_percent_change = "{:0.2f}".format(general_market_data[0]['price_change_percentage_24h'])
        daily_volume = "{:,}".format(general_market_data[0]['total_volume'])


        tweet = f"""
🔔 XRP Price Alert 
→ 🇺🇸 ${xrp_usd}
→ 🇬🇧 £{xrp_gbp}
→ 🇪🇺 €{xrp_eur}
→ 🇨🇳 ¥{xrp_cny}
Market Performance in 🇺🇸
→ 📈 24h-High: ${daily_high}
→ 📉 24h-Low: ${daily_low}
→ 🔃   24h-% Change: {daily_percent_change}% 
→ 🌊 Volume: ${daily_volume}
#XRP #XRPCommunity #XRPHolders
"""

        image_text = f"""
        24 hour Price Change
        ${xrp_usd}
        """
        img = Image.open("base_image.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Futura.ttc", 65)
        draw.text((160, 90),f"${xrp_usd}",(255,255,255),font=font)
        img.save('image_to_tweet.png')
        image_to_tweet = "image_to_tweet.png"
        time.sleep(10800)
        media = api.media_upload("image_to_tweet.png")
        api.update_status(status=tweet, media_ids=[media.media_id])
        print("Tweeted")
        

while True:
        call()
