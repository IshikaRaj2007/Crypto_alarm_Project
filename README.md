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

## 🛠️ Tech Stack

| Category | Technology |
| --- | --- |
| Language | Python 3.x |
| Libraries | `requests`, `time`, `plyer` |
| API | CoinGecko API v3 |
| OS | Windows / Mac / Linux |

## 📁 Project Structure
