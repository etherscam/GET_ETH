import configparser 
import requests
import os
import json
import web3
from web3 import Web3
from time import sleep
import web3
import configparser
import click
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("wallet_sender.ini") 
if not type(config.read("wallet_sender.ini") ):
    print('OOPS')
else:
    print(config.read("wallet_sender.ini"))
try:
    infura = config['SENDER']['INFURA']
    w3 = Web3(Web3.HTTPProvider(infura))
    my_wallet = config['SENDER']['MY_WALLET']#Кошелек для получения эфира#Приватный
    gas_price = int(config['SENDER']['GAS_PRICE'])
    try: 
         with open ("wallets") as f:
            wallets = [line.rstrip() for line in f]    
        with open ("private_keys") as p:
            private_keys = [line.rstrip() for line in p]
            if wallets and private_keys and len(wallets)==len(private_keys):
                summ_eth  = am_eth*len(wallets)
                if click.confirm('Вы хотите отправить %sETH на %s'%(summ_eth,my_wallet), default=True):
                    for i in wallets:
                        d = w3.toChecksumAddress(i)
                        wallets_2.append(d)
                    #am = w3.toWei(am_eth, 'ether')
                    nonce = w3.eth.getTransactionCount(w3.toChecksumAddress(wallet))
                    for i,k in zip(wallets_2,private_keys):
                        try:
                            txn =dict({
                                 'gas': 21000,
                                 'gasPrice': w3.toWei(gas_price,'GWEI'),
                                 'to':my_wallet,
                                 'value': w3.eth.getBalance(i) - w3.fromWei((w3.toWei(gas_price,'gwei')*21000)),
                                 'nonce': nonce,

                            })
                            signed_txn = w3.eth.account.sign_transaction(txn, private_key=k)
                            tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
                            print(tx_hash.hex()) 
                        except:
                            print('OOPS Check:', i)
                    print('Выполнено, Ожидайте...')
    
    except Exception as ex:
        print(ex)
        print('Проверьте наличие файлов wallets и private_keys')
