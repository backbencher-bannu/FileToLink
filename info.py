import os
# Bot information
API_ID = os.getenv('API_ID', "26339634")
API_HASH = os.getenv('API_HASH', "e0318ca1a4652f9348844203de8f491b")
BOT_TOKEN = os.getenv('BOT_TOKEN', "7361998653:AAEpt3jH-FpJMJR7ILSeem7mH4SgIr9k8uA")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = os.getenv("BIN_CHANNEL", "-1002185509993") #Log Channel
URL = os.getenv("URL", "mongodb+srv://harishkumargorinta:P6ak9kZKvx33Jx3@movies24.ng58m.mongodb.net/?retryWrites=true&w=majority&appName=Movies24") #App URL not MongoDB URL
