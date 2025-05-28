# Fridge-Door-Alert

ESP32とリードスイッチを使って冷蔵庫や冷凍庫のドアが1分以上開きっぱなしの場合に、LINEに通知するIoTシステムです。  
開発環境はMicroPython、通知はLINE Messaging APIを使用しています。

---

## 必要なもの
- ESP32
- リードスイッチ ×2（冷蔵庫・冷凍庫用）
- ジャンパーワイヤー、ブレッドボード等
- LINE公式アカウント（Messaging APIのチャネルアクセストークン・ユーザーID）

---

## セットアップ手順

1. **MicroPythonのファームウェアをESP32へ書き込む**

2. **回路を作成**  
    - リードスイッチの片方をESP32のGPIO12・GPIO13などに接続
    - もう一方はGNDへ

3. **config.pyを作成**  
    プロジェクトのルートに`config.py`を配置し、APIトークンやWi-Fi情報などを管理します。  

    ```python
    # config.py
    LINE_API_URL = "https://api.line.me/v2/bot/message/push"
    ACCESS_TOKEN = "YOUR_CHANNEL_ACCESS_TOKEN"  # Messaging APIのアクセストークン
    USER_ID = "YOUR_USER_ID"                   # Messaging APIのユーザーID
    SSID = "your_wifi_ssid"
    PASSWORD = "your_wifi_password"
    FRIDGE_PIN = 12     # 冷蔵庫で使うリードスイッチのピン番号
    FREEZER_PIN = 13    # 冷凍庫
    ```

4. **ファイルのアップロード**  
    VSCodeの拡張機能Pymakrを使って`boot.py`、`config.py`、`main.py`をESP32にアップロードします。

---

