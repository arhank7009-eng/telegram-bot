8# ==========================================
# TELEGRAM AUTO RESELLER BOT
# FULL API + AUTO KEY VERSION
# RENDER + GITHUB READY
# ==========================================

from telebot import TeleBot, types
from flask import Flask
from threading import Thread
import requests
import os

# ==========================================
# KEEP ALIVE FOR RENDER
# ==========================================

app = Flask('')

@app.route('/')
def home():
    return "Bot Running Successfully"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==========================================
# BOT CONFIG
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN") or "8697358234:AAHWxt4t7g6Jf-otiiDC1tU4yQUFnEiyPD4"

ADMIN_ID = 7762997996

UPI_ID = "8795734376@ybl"

bot = TeleBot(BOT_TOKEN)

# ==========================================
# API CONFIG
# ==========================================

API_URL = "https://adminpanels.shop/api/reseller_v1.php"

API_KEY = "973a75c41668a85a7f8c920b574d7930"
# ==========================================
# PRODUCTS
# ==========================================

products = {

    "PRIME HOOK FF NONROOT": {
        "pid": "48",

        "durations": {
            "1 Day Nonroot": 70,
            "3 Days Nonroot": 130,
            "7 Days Nonroot": 280,
            "10 Days Nonroot": 410
        },

        "keys": {
            "1 Day Nonroot": [
                "PRIME-1D-001",
                "PRIME-1D-002"
            ],

            "3 Days Nonroot": [
                "PRIME-3D-001"
            ],

            "7 Days Nonroot": [
                "PRIME-7D-001"
            ],

            "10 Days Nonroot": [
                "PRIME-10D-001"
            ]
        }
    },

    "DRIPCLIENT NONROOT FF": {
        "pid": "62",

        "durations": {
            "1 Day NONROOT": 80,
            "3 Days NONROOT": 150,
            "7 Days NONROOT": 270,
            "15 Days NONROOT": 650,
            "30 Days NONROOT": 1200
        },

        "keys": {
            "1 Day NONROOT": [
                "DRIP-1D-001"
            ],

            "3 Days NONROOT": [
                "DRIP-3D-001"
            ],

            "7 Days NONROOT": [
                "DRIP-7D-001"
            ],

            "15 Days NONROOT": [
                "DRIP-15D-001"
            ],

            "30 Days NONROOT": [
                "DRIP-30D-001"
            ]
        }
    },

    "HG CHEATS FF ROOT + NONROOT": {
        "pid": "65",

        "durations": {
            "1 Day Root + Nonroot": 100,
            "7 Days Root + Nonroot": 350,
            "10 Days Root + Nonroot": 550,
            "30 Days Root + Nonroot": 1300
        },

        "keys": {
            "1 Day Root + Nonroot": [
                "HG-1D-001"
            ],

            "7 Days Root + Nonroot": [
                "HG-7D-001"
            ],

            "10 Days Root + Nonroot": [
                "HG-10D-001"
            ],

            "30 Days Root + Nonroot": [
                "HG-30D-001"
            ]
        }
    },

    "PATO TEAM FF NONROOT + ROOT": {
        "pid": "54",

        "durations": {
            "3 Days Safe + Brutal": 150,
            "7 Days Normal": 320,
            "7 Days Brutal": 450,
            "15 Days": 700,
            "30 Days": 1400
        },

        "keys": {
            "3 Days Safe + Brutal": [
                "PATO-3D-001"
            ],

            "7 Days Normal": [
                "PATO-7D-001"
            ],

            "7 Days Brutal": [
                "PATO-BRUTAL-001"
            ],

            "15 Days": [
                "PATO-15D-001"
            ],

            "30 Days": [
                "PATO-30D-001"
            ]
        }
    },

    "BR MOD FF ROOT + VPHONE": {
        "pid": "67",

        "durations": {
            "1 Day": 100,
            "7 Days": 350,
            "15 Days": 700,
            "30 Days": 1500
        },

        "keys": {
            "1 Day": [
                "BRROOT-1D-001"
            ],

            "7 Days": [
                "BRROOT-7D-001"
            ],

            "15 Days": [
                "BRROOT-15D-001"
            ],

            "30 Days": [
                "BRROOT-30D-001"
            ]
        }
    },

    "BR MOD FF PC VERSION": {
        "pid": "49",

        "durations": {
            "1 Day PC Aim Silent": 120,
            "1 Day PC Bypass Silent": 150,
            "10 Days PC Aim Silent": 700,
            "10 Days PC Bypass Silent": 850,
            "30 Days PC Aim Silent": 1800,
            "30 Days PC Bypass Silent": 2200
        },

        "keys": {
            "1 Day PC Aim Silent": [
                "BRMOD-1D-001"
            ],

            "1 Day PC Bypass Silent": [
                "BRMOD-BYPASS-001"
            ],

            "10 Days PC Aim Silent": [
                "BRMOD-10D-001"
            ],

            "10 Days PC Bypass Silent": [
                "BRMOD-10DB-001"
            ],

            "30 Days PC Aim Silent": [
                "BRMOD-30D-001"
            ],

            "30 Days PC Bypass Silent": [
                "BRMOD-30DB-001"
            ]
        }
    },

    "DRIPCLIENT 8BP NONROOT": {
        "pid": "59",

        "durations": {
            "1 Day": 90,
            "7 Days": 350,
            "30 Days": 1100
        },

        "keys": {
            "1 Day": [
                "8BP-1D-001"
            ],

            "7 Days": [
                "8BP-7D-001"
            ],

            "30 Days": [
                "8BP-30D-001"
            ]
        }
    },

    "DRIPCLIENT FF PC AIMKILL": {
        "pid": "44",

        "durations": {
            "1 Day PC AIMKILL": 150,
            "7 Days PC AIMKILL": 700,
            "15 Days PC AIMKILL": 1200,
            "30 Days PC AIMKILL": 2200
        },

        "keys": {
            "1 Day PC AIMKILL": [
                "AIMKILL-1D-001"
            ],

            "7 Days PC AIMKILL": [
                "AIMKILL-7D-001"
            ],

            "15 Days PC AIMKILL": [
                "AIMKILL-15D-001"
            ],

            "30 Days PC AIMKILL": [
                "AIMKILL-30D-001"
            ]
        }
    },

    "DRIPCLIENT ROOT FF": {
        "pid": "63",

        "durations": {
            "1 Day ROOT": 100,
            "7 Days ROOT": 450,
            "30 Days ROOT": 1400
        },

        "keys": {
            "1 Day ROOT": [
                "ROOT-1D-001"
            ],

            "7 Days ROOT": [
                "ROOT-7D-001"
            ],

            "30 Days ROOT": [
                "ROOT-30D-001"
            ]
        }
    },

    "IOS FF PANEL ALL": {
        "pid": "58",

        "durations": {
            "1 Day FluoRite FF": 250,
            "7 Days FluoRite FF": 900,
            "30 Days FluoRite FF": 2500
        },

        "keys": {
            "1 Day FluoRite FF": [
                "IOS-1D-001"
            ],

            "7 Days FluoRite FF": [
                "IOS-7D-001"
            ],

            "30 Days FluoRite FF": [
                "IOS-30D-001"
            ]
        }
    },

    "XYZ CHEATS FF ROOT + VPHONE": {
        "pid": "66",

        "durations": {
            "3 Days": 200,
            "7 Days": 500,
            "15 Days": 900,
            "30 Days": 1800
        },

        "keys": {
            "3 Days": [
                "XYZ-3D-001"
            ],

            "7 Days": [
                "XYZ-7D-001"
            ],

            "15 Days": [
                "XYZ-15D-001"
            ],

            "30 Days": [
                "XYZ-30D-001"
            ]
        }
    }
}
# ==========================================
# START COMMAND
# ==========================================

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        types.KeyboardButton("🛒 Buy Product")
    )

    bot.send_message(
        message.chat.id,
        """
🔥 AUTO RESELLER BOT

✅ Auto Product Buy
✅ Instant Key Delivery
✅ 24/7 Active

Select Option Below
""",
        reply_markup=markup
    )

# ==========================================
# BUY PRODUCT BUTTON
# ==========================================

@bot.message_handler(func=lambda m: m.text == "🛒 Buy Product")
def buy_product(message):

    markup = types.InlineKeyboardMarkup()

    for product in products:

        markup.add(
            types.InlineKeyboardButton(
                text=product,
                callback_data=f"product|{product}"
            )
        )

    bot.send_message(
        message.chat.id,
        "📦 Select Product",
        reply_markup=markup
    )
# ==========================================
# CALLBACKS
# ==========================================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    data = call.data.split("|")

    # PRODUCT SELECT
    if data[0] == "product":

        product_name = data[1]

        markup = types.InlineKeyboardMarkup()

        for duration, price in products[product_name]["durations"].items():

            btn = types.InlineKeyboardButton(
                text=f"{duration} - ₹{price}",
                callback_data=f"buy|{product_name}|{duration}"
            )

            markup.add(btn)

        bot.edit_message_text(
            text=f"📦 Select Duration For\n\n{product_name}",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # BUY PRODUCT
    elif data[0] == "buy":

        product_name = data[1]
        duration = data[2]

        price = products[product_name]["durations"][duration]

        markup = types.InlineKeyboardMarkup()

        pay_btn = types.InlineKeyboardButton(
            text="✅ I Paid",
            callback_data=f"paid|{product_name}|{duration}"
        )

        markup.add(pay_btn)

        bot.edit_message_text(
            text=
            f"💸 Payment Details\n\n"
            f"📦 Product: {product_name}\n"
            f"⏳ Duration: {duration}\n"
            f"💰 Price: ₹{price}\n\n"
            f"🪙 UPI ID: yourupi@paytm\n\n"
            f"Payment karne ke baad niche button dabao 👇",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # PAYMENT DONE
    if data[0] == "paid":

        product_name = data[1]
        duration = data[2]

        bot.answer_callback_query(
            callback_query_id=call.id,
            text="✅ Payment Submitted"
        )

        bot.send_message(
            call.message.chat.id,
            f"✅ Payment Request Submitted\n\n"
            f"📦 Product: {product_name}\n"
            f"⏳ Duration: {duration}\n\n"
            f"Admin payment verify karega."
        )

        caption = f"""
✅ PAYMENT SUCCESSFUL

📦 Product:
{product_name}

⌛ Duration:
{duration}

🔑 YOUR KEY:
{key}

📨 API RESPONSE:
{result}

⚠️ Do Not Share Your Key
"""

QR_FILE_ID = "AgACAgUAAxkBAAM..."

bot.send_photo(
    chat_id=call.message.chat.id,
    photo=QR_FILE_ID,
    caption=caption,
    reply_markup=markup
)

# =================================
# AFTER PAYMENT
# =================================
if data[0] == "paid":
# =================================
# AFTER PAYMENT
# =================================
if data[0] == "paid":
    product_name = data[1]

    duration = data[2]

    pid = products[product_name]["pid"]

    # =================================
    # API BUY REQUEST
    # =================================

    payload = {
        "api_key": API_KEY,
        "action": "buy",
        "product_id": pid,
        "duration": duration
    }
        try:

            response = requests.post(
                API_URL,
                data=payload
            )

            result = response.text

        except Exception as e:

            bot.send_message(
                call.message.chat.id,
                f"❌ API ERROR\n\n{e}"
            )

            return

        # ==================================
        # GET KEY
        # ==================================

        available_keys = products[product_name]["keys"][duration]

        if len(available_keys) == 0:

            bot.send_message(
                call.message.chat.id,
                "❌ Product Out Of Stock"
            )

            return

        key = available_keys.pop(0)

        # ==================================
        # SEND TO USER
        # ==================================

        bot.send_message(
            call.message.chat.id,
            f"""
✅ PAYMENT SUCCESSFUL

📦 Product:
{product_name}

⏳ Duration:
{duration}

🔑 YOUR KEY:

{key}

📨 API RESPONSE:

{result}

⚠️ Do Not Share Your Key
"""
        )

        # ==================================
        # ADMIN LOG
        # ==================================

        bot.send_message(
            ADMIN_ID,
            f"""
🛒 NEW ORDER

👤 USER:
{call.from_user.id}

📦 PRODUCT:
{product_name}

⏳ DURATION:
{duration}

🔑 KEY:
{key}

📨 API:
{result}
"""
        )
@bot.message_handler(content_types=['photo'])
def get_file_id(message):

    file_id = message.photo[-1].file_id

    bot.reply_to(message, file_id)
# ==========================================
# RUN BOT
# ==========================================

keep_alive()
print("Bot Started Successfully")

bot.infinity_polling(skip_pending=True)
