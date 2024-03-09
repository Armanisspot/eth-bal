import requests
from telegram.ext import Updater, CommandHandler

# Замените YOUR_ETHEREUM_ADDRESS на адрес вашего кошелька Ethereum
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"

def get_eth_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_wei = int(response.json()['result'])
        balance_eth = balance_wei / 10**18  # Переводим баланс из wei в ether
        return balance_eth
    else:
        return "Ошибка при получении баланса"

# Функция-обработчик команды /balance
def balance(update, context):
    eth_address = "YOUR_ETHEREUM_ADDRESS"
    balance = get_eth_balance(eth_address)
    if isinstance(balance, float):
        update.message.reply_text(f"Баланс кошелька {eth_address}: {balance} ETH")
    else:
        update.message.reply_text(balance)

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /balance
    dp.add_handler(CommandHandler("balance", balance))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
