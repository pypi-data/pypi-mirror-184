#!/usr/bin/python
# coding: utf8


class Contract:
    def __init__(self, api, address: str):
        self.api = api
        self.contractAddress = address

        self.cataloged = None
        self.decimals = None
        self.name = None
        self.symbol = None
        self.totalSupply = None
        self.type = None

    #####################################
    #                                   #
    #          API requests             #
    #                                   #
    #####################################
    def fetch(self) -> None:
        res = self.api.getToken(self.contractAddress)
        self.cataloged = res['cataloged']
        self.decimals = res['decimals']
        self.name = res['name']
        self.symbol = res['symbol']
        self.totalSupply = res['totalSupply']
        self.type = res['type']

    def getHolders(self) -> list:
        return self.api.getTokenHolders(self.contractAddress)

    def getTotalSupply(self) -> int:
        if not self.totalSupply:
            totalSupply = self.api.getTotalSupply(self.contractAddress)
            self.totalSupply = totalSupply
        return self.totalSupply
