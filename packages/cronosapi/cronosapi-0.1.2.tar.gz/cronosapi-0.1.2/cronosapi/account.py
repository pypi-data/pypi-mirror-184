#!/usr/bin/python
# coding: utf8

class Account:
    def __init__(self, api, adress: str):
        self.api = api
        self.adress = adress

    #####################################
    #                                   #
    #          API requests             #
    #                                   #
    #####################################

    def getBalance(self) -> float:
        return self.api.getAccountBalance(self.adress)

    def getEthGetBalance(self) -> str:
        return self.api.getAccountEthGetBalance(self.adress)

    def getTransactionsList(self) -> list:
        return self.api.getAccountTransactionsList(self.adress)

    def getTokenTransfer(self) -> list:
        return self.api.getAccountTokenTransfer(self.adress)

    def getTokenBalance(self, contractAdress: str) -> float:
        return self.api.getAccountTokenBalance(self.adress, contractAdress)

    def getTokenList(self) -> list:
        return self.api.getAccountTokenList(self.adress)

