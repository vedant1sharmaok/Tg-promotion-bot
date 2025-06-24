
<!-- ENHANCED HEADER SECTION -->
<div align="center">
  <h1 style="font-size: 2.5rem;">Tg-Promotion-Bot</h1>
  <p style="font-size: 1.5rem;">⚡ Enterprise Telegram Automation | 🚀 Mass Messaging Solution</p>
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1500&color=FF5733&center=true&width=600&height=60&lines=Automated+Message+Promotion;Multi-Account+Support;Intelligent+Scheduling;Real-time+Analytics" alt="Typing animation">
  
  <img src="https://raw.githubusercontent.com/vedant1sharmaok/Tg-promotion-bot/main/assets/logo.png" width="200" style="margin-top: 20px;">

  <!-- STAR & CONTRIBUTOR COUNTERS -->
  <div style="margin: 20px 0;">
    <img src="https://img.shields.io/github/stars/vedant1sharmaok/Tg-promotion-bot?style=for-the-badge&logo=github&color=00F7FF&labelColor=0D1117" alt="Stars">
    <img src="https://img.shields.io/github/contributors/vedant1sharmaok/Tg-promotion-bot?style=for-the-badge&logo=github&color=00F7FF&labelColor=0D1117" alt="Contributors">
    <img src="https://img.shields.io/github/last-commit/vedant1sharmaok/Tg-promotion-bot?style=for-the-badge&logo=github&color=00F7FF&labelColor=0D1117" alt="Last Commit">
  </div>
</div>

<!-- DEPLOYMENT BADGES -->
<div align="center">
  [![Deploy on Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/vedant1sharmaok/Tg-promotion-bot)
  [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=github.com/vedant1sharmaok/Tg-promotion-bot)
  [![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/vedant1sharmaok/Tg-promotion-bot)
  [![Join Telegram](https://img.shields.io/badge/Join-Telegram%20Channel-0088CC?style=for-the-badge&logo=telegram)](https://t.me/yourchannel)
</div>

<!-- ANIMATED DIVIDER -->
<img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/divider.gif?raw=true" width="100%">

## 🌟 Feature Galaxy

<table>
  <tr>
    <td width="33%">
      <h3><img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/icons/auth.gif?raw=true" width=20> Smart Auth</h3>
      <ul>
        <li>🔐 Session String Login</li>
        <li>📱 OTP+Password Support</li>
        <li>🔄 Auto Session Backup</li>
        <li>🔑 AES-256 Encryption</li>
      </ul>
    </td>
    <td width="33%">
      <h3><img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/icons/rocket.gif?raw=true" width=20> Promotion Engine</h3>
      <ul>
        <li>💬 Dynamic Templates</li>
        <li>🖼️ Media Attachments</li>
        <li>⏱️ Precision Scheduling</li>
        <li>🌐 Geo-Targeting</li>
      </ul>
    </td>
    <td width="33%">
      <h3><img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/icons/shield.gif?raw=true" width=20> Security</h3>
      <ul>
        <li>🛡️ Proxy Rotation</li>
        <li>🚨 Flood Protection</li>
        <li>📛 Account Rotation</li>
        <li>🔒 IP Obfuscation</li>
      </ul>
    </td>
  </tr>
</table>

<!-- ANIMATED DEMO -->
<div align="center">
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/demo.gif?raw=true" width="800" alt="Feature Demo">
</div>

<!-- SCREENSHOTS CAROUSEL -->
## 📸 Screenshot Showcase
<div align="center">
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/screenshots/dashboard.png?raw=true" width="30%">
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/screenshots/campaign.png?raw=true" width="30%"> 
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/screenshots/analytics.png?raw=true" width="30%">
</div>

## 👥 Contributor Hall of Fame
<div align="center">
  <a href="https://github.com/vedant1sharmaok/Tg-promotion-bot/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=vedant1sharmaok/Tg-promotion-bot&max=12&columns=6" alt="Contributors">
  </a>
</div>

## 🛠️ How to Contribute
<div align="center">
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/contribute.gif?raw=true" width="600" alt="Contribution Guide">
</div>

```markdown
1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request
```

## 🏗️ Technical Architecture
```mermaid
graph TD
    A[User Interface] --> B[API Gateway]
    B --> C[Auth Service]
    B --> D[Campaign Manager]
    B --> E[Group Scraper]
    C --> F[(Session DB)]
    D --> G[[Redis Queue]]
    G --> H[Account Pool]
    H --> I[Telegram API]
    E --> J[(Group DB)]
    I --> K[Analytics]
    K --> L[(Metrics DB)]
    L --> M[Dashboard]
```

## 🚀 Quick Start
```bash
# Clone with Git
git clone https://github.com/vedant1sharmaok/Tg-promotion-bot.git
cd Tg-promotion-bot

# Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Edit with your credentials

# Initialize database
python -c "from database.db import init_db; init_db()"

# Start the bot
python main.py
```

## ⚙️ Configuration
```ini
# REQUIRED
API_ID=1234567
API_HASH=your_api_hash_here
BOT_TOKEN=123:your_bot_token

# OPTIMAL
ADMIN_IDS=vedant1sharmaok  # Your Telegram ID
PROXY_ENABLED=True
PROXY_LIST=proxy1.com:1080,proxy2.com:1080
MESSAGES_PER_HOUR=500  # Per account
```

## 👨‍💻 Developer Spotlight
<div align="center">
  <a href="https://github.com/vedant1sharmaok">
    <img src="https://avatars.githubusercontent.com/vedant1sharmaok" width="200" style="border-radius:50%; border: 5px solid #00F7FF; box-shadow: 0 0 20px #00F7FF;">
    <h2>Vedant Sharma</h2>
    <p>Lead Developer & Security Architect</p>
  </a>
  
  <div style="display: flex; justify-content: center; gap: 15px; margin: 20px 0;">
    <a href="https://twitter.com/yourhandle">
      <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter">
    </a>
    <a href="https://t.me/yourchannel">
      <img src="https://img.shields.io/badge/Telegram-0088CC?style=for-the-badge&logo=telegram">
    </a>
    <a href="mailto:your@email.com">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail">
    </a>
  </div>
  
  <blockquote style="max-width: 600px; margin: 0 auto; padding: 15px; background: rgba(0,247,255,0.1); border-left: 4px solid #00F7FF; font-style: italic;">
    "Building tools that automate without compromising platform integrity or user experience."
  </blockquote>
</div>

## ⚠️ Critical Guidelines
<div style="background: rgba(255,0,0,0.1); border-left: 5px solid #FF0000; padding: 20px; border-radius: 0 8px 8px 0; margin: 30px 0;">
  <h3 style="color: #FF0000; margin-top: 0;">❗ ESSENTIAL RULES</h3>
  <ul style="padding-left: 20px;">
    <li><strong>STRICTLY FOLLOW</strong> <a href="https://core.telegram.org/api/terms" style="color: #00F7FF;">Telegram's ToS</a></li>
    <li><strong>MINIMUM 30 SECONDS</strong> between messages</li>
    <li><strong>ALWAYS USE PROXIES</strong> for multiple accounts</li>
    <li><strong>DISCLOSE AUTOMATION</strong> in group descriptions</li>
  </ul>
</div>

## 📜 AGPLv3 License
```text
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007

Copyright (C) 2023 Vedant Sharma (vedant1sharmaok)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Additional Terms for Telegram Automation:
1. Must comply with Telegram's Terms of Service
2. Minimum 30-second delay between messages
3. Mandatory proxy use for multiple accounts
4. Commercial use requires written permission

Full license text: https://www.gnu.org/licenses/agpl-3.0.en.html
```

<!-- ANIMATED FOOTER -->
<div align="center">
  <img src="https://github.com/vedant1sharmaok/Tg-promotion-bot/blob/main/assets/footer.gif?raw=true" width="100%">
  <p>© 2023 Tg-Promotion-Bot | Developed with ❤️ by <a href="https://github.com/vedant1sharmaok">Vedant Sharma</a></p>
</div>
```
