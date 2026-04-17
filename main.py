import requests
import time
from plyer import notification
SYMBOL="bitcoin"
CURRENCY="usd"
THRESHOLD=80000
CHECK_INTERVAL=60
def get_crypto_price(coin_id, currency):
    try:
        url=f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
        response=requests.get(url)
        data=response.json()
        print(data)

        if coin_id in data and currency in data[coin_id]:
         return data[coin_id][currency]
        else:
            print("API returned unexpected data:",data)
            return None
    except Exception as e:
        print(f"Error fetching data:{e}")
        return None
    
def send_alert(price):
    notification.notify(title="CRYPTO ALERT!", message=f"{SYMBOL.upper()} has hit $ {price}!Action required.",
                        app_name="crypto alarm",timeout=10)
def main():
    print(f"---Monitoring{SYMBOL.upper()}---")
    print(f"Alert set for prices below:$ {THRESHOLD}")
    while True:
        price=get_crypto_price(SYMBOL,CURRENCY)
        if price is not None:
            print(f"current price:${price}| Time:{time.strftime('%H:%M:%S')}")
            if price<=THRESHOLD:
                print("THRESHOLD HIT!Sending notification...")
                send_alert(price)
        else:
            print("failed to fetch price")

        time.sleep(CHECK_INTERVAL)
if(__name__=="__main__"):
    main()



                        