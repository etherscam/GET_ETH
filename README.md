# GET_ETH

sudo apt-get update

git clone https://github.com/etherscam/GET_ETH.git

chmod +x GET_ETH/APP_INSTALL

cd GET_ETH

Заполните файл wallets (кошельки без пробелов/кавычек/запятых)

0x123

0x777

nano wallets

Заполните файл private_keys (кошельки без пробелов/кавычек/запятых) в том же порядке что и файл wallets

123(для 0x123)

777(для 0x777)

nano private_keys

Заполните файл wallet_sender.ini

nano wallet_sender.ini 

Запустите

python3 GET.py
