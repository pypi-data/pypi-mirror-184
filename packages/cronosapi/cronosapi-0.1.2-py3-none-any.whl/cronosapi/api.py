#!/usr/bin/python
# coding: utf8

import requests

from .account import Account
from .contract import Contract

class Api:
    def __init__(self):
        self.url = 'https://cronos.crypto.org/explorer/api'

    def get(self, request_url):
        r = requests.get(self.url + '?' + request_url).json()

        return r['result']

    def getAccount(self, address: str) -> Account:
        account = Account(self, address)

        return account

    def getContract(self, address: str) -> Contract:
        contract = Contract(self, address)

        return contract

    #####################################
    #                                   #
    #              Account              #
    #                                   #
    #####################################
    def getAccountBalance(self, address: str) -> float:
        res = self.get('module=account&action=balance&address=' + address)
        return float(res) / pow(10, 18)

    def getAccountEthGetBalance(self, address: str) -> str:
        res = self.get('module=account&action=eth_get_balance&address=' + address)
        return res

    def getAccountTransactionsList(self, address: str) -> list:
        res = self.get('module=account&action=txlist&address=' + address)
        return res

    def getAccountTokenTransfer(self, address: str) -> list:
        res = self.get('module=account&action=tokentx&address=' + address)
        return res

    def getAccountTokenBalance(self, address: str, contractAddress: str) -> float:
        res = self.get('module=account&action=tokenbalance&address=%s&contractaddress=%s' % (address, contractAddress))
        return float(res)

    def getAccountTokenList(self, address: str) -> list:
        res = self.get('module=account&action=tokenlist&address=%s' % address)
        return list(res)

    #####################################
    #                                   #
    #               Logs                #
    #                                   #
    #####################################
    def getLogs(self, fromBlock: str, toBlock: str, address: str, firstTopic: str):
        return self.get('module=logs&action=getLogs&fromBlock=%s&toBlock=%s&address=%s&topic0=%s' % (fromBlock, toBlock, address, firstTopic))

    #####################################
    #                                   #
    #               Token               #
    #                                   #
    #####################################
    def getToken(self, contractAddress: str) -> list:
        res = self.get('module=token&action=getToken&contractaddress=%s' % contractAddress)
        return res

    def getTokenHolders(self, contractAddress: str) -> list:
        res = self.get('module=token&action=getTokenHolders&contractaddress=%s' % contractAddress)
        return res

    #####################################
    #                                   #
    #               Stats               #
    #                                   #
    #####################################
    def getTotalSupply(self, contractAddress: str) -> int:
        res = self.get('module=stats&action=tokensupply&contractaddress=%s' % contractAddress)
        return int(res)

    def getCoinPrice(self) -> list:
        res = self.get('module=stats&action=coinprice')

        res['coin_btc'] = float(res['coin_btc'])
        res['coin_btc_timestamp'] = int(res['coin_btc_timestamp'])
        res['coin_usd'] = float(res['coin_usd'])
        res['coin_usd_timestamp'] = int(res['coin_usd_timestamp'])

        return res

    def getCoinPriceBtc(self) -> float:
        return self.getCoinPrice()['coin_btc']

    def getCoinPriceUsd(self) -> float:
        return self.getCoinPrice()['coin_usd']

    #####################################
    #                                   #
    #               Block               #
    #                                   #
    #####################################

    #####################################
    #                                   #
    #             Contract              #
    #                                   #
    #####################################

    #####################################
    #                                   #
    #             Transaction           #
    #                                   #
    #####################################
