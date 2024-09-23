import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime
from Sophia import *
from pyrogram import *

def fetch_crypto_details(crypto):
    url = f"https://www.coingecko.com/en/coins/{crypto}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_tag = soup.find("span", {"class": "no-wrap"})
    current_price_usd = price_tag.text.strip() if price_tag else "N/A"
    high_price_tag = soup.find("span", {"data-target": "price.high_24h"})
    low_price_tag = soup.find("span", {"data-target": "price.low_24h"})
    high_price_usd = high_price_tag.text.strip() if high_price_tag else "N/A"
    low_price_usd = low_price_tag.text.strip() if low_price_tag else "N/A"
    percent_change_tag = soup.find("span", {"class": "percent-change"})
    percent_change = percent_change_tag.text.strip() if percent_change_tag else "N/A"
    launch_date_tag = soup.find("td", string="Launch Date")
    launch_date = launch_date_tag.find_next_sibling("td").text.strip() if launch_date_tag else "N/A"
    
    return current_price_usd, high_price_usd, low_price_usd, percent_change, launch_date

def plot_crypto_price(timestamps, prices, crypto):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, label=f'{crypto.capitalize()} Price (USD)')
    plt.title(f'{crypto.capitalize()} Cryptocurrency Performance')
    plt.xlabel('Time')
    plt.ylabel('Price in USD')
    plt.legend()
    image_path = f'{crypto}_performance.png'
    plt.savefig(image_path)
    plt.close()
    
    return image_path

def format_caption(crypto, current_price, high_price, low_price, percent_change, launch_date):
    caption = (f"**{crypto.capitalize()} Performance**\n\n"
               f"**Current Price** (USD): ${current_price}\n"
               f"**High Price (24h)**: ${high_price}\n"
               f"**Low Price (24h)**: ${low_price}\n"
               f"**Launch Date**: {launch_date}\n"
               f"**Percentage Change (24h)**: {percent_change}\n")
    
    return caption

@Sophia.on_message(filters.command("crypto", prefixes=HANDLER) & filters.user('me'))
def crypto_graph(_, message):
    if len(message.command) < 2:
        return message.edit("Please enter a crypto name!")
    crypto = message.text.split(None, 1)[1]
    current_price, high_price, low_price, percent_change, launch_date = fetch_crypto_details(crypto)
    
    if current_price == "N/A":
        return message.edit("Could not fetch current price. Please check the cryptocurrency name.")
    
    timestamps = [datetime.now() for _ in range(10)]
    prices = [float(current_price.strip('$').replace(',', '')) for _ in range(10)]
    image_path = plot_crypto_price(timestamps, prices, crypto)
    caption = format_caption(crypto, current_price, high_price, low_price, percent_change, launch_date)
    message.reply_photo(photo=image_path, caption=caption)
