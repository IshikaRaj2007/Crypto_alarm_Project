# Crypto_alarm_Project
# Crypto Alarm - Price Alert Bot

[Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[CoinGecko API](https://img.shields.io/badge/API-CoinGecko-00D1B2?style=for-the-badge)
[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python script that monitors cryptocurrency prices in real-time and sends desktop notifications when the price drops below your set threshold.

Never miss a dip again. This bot checks prices every 60 seconds using CoinGecko API and alerts you instantly.

---

## ✨ Features

- **Real-time Price Tracking**: Fetches live crypto prices from CoinGecko API
- **Custom Price Alerts**: Set any threshold price to trigger an alert
- **Desktop Notifications**: Uses `plyer` library to send system pop-up alerts
- **Configurable**: Change coin, currency, threshold, and check interval easily
- **Continuous Monitoring**: Runs in a loop and logs current price + timestamp
- **Error Handling**: Handles API failures gracefully


# Crypto Alarm - Real-Time Crypto Price Alert Bot

[Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[CoinGecko API](https://img.shields.io/badge/API-CoinGecko-00D1B2?style=for-the-badge)
[Status: Active](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A lightweight Python automation script that monitors cryptocurrency prices 24/7 and sends instant desktop notifications when the price falls below your target. 

Built with `requests`, `plyer`, and CoinGecko API. No API keys required.

### 🎯 Problem it Solves
Crypto prices move fast. Instead of constantly checking charts, this bot watches for you and pings you the moment your buy price hits.

---

## ✨ Key Features

- **Live Price Monitoring**: Tracks any coin supported by CoinGecko
- **Smart Alerts**: Desktop notification when price <= threshold
- **Highly Configurable**: Change coin, currency, threshold, and check frequency in 4 lines
- **Logging**: Prints current price + timestamp to console every check
- **Error Resilient**: Handles API errors and network issues without crashing
- **Cross-Platform**: Works on Windows, Mac, and Linux

## 🛠️ Tech Stack

| Category | Technology |
| --- | --- |
| Language | Python 3.9+ |
| HTTP Client | `requests` |
| Notifications | `plyer` |
| Data Source | CoinGecko Public API v3 |
| Concepts Used | API Integration, Automation, Exception Handling |

## 📁 Project Structure
