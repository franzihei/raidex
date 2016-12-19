#!/usr/bin/env python
from __future__ import print_function
from flask import jsonify, request, abort, make_response
from raidex.client import OfferBook



class API(object):

    def __init__(self, client):
        self.client = client

    def get_order_book(self, asset_pair, count=None):
        assert isinstance(asset_pair, tuple)
        assert len(asset_pair) == 2
        
        orderbook = self.client.get_offerbook_by_asset_pair(asset_pair)
        assert isinstance(orderbook, OfferBook)
        bids = [dict(price=order.price, amount=order.amount) for order in list(orderbook.bids.orders)]
        asks = [dict(price=order.price, amount=order.amount) for order in list(orderbook.asks.orders)]
        return jsonify(dict(bids=bids, asks=asks))

    def get_trade_history(self, asset_pair, count):
        raise NotImplementedError

    def limit_order(self, asset_pair, type, num_tokens, price): # returns internal order_id
        raise NotImplementedError

    def market_order(self, asset_pair, type, num_tokens): # returns internal order_id
        raise NotImplementedError

    def get_order_status(self, asset_pair, order_id):
        raise NotImplementedError

    def cancel_order(self, asset_pair, order_id):
        raise NotImplementedError

    def get_available_assets(self):
        raise NotImplementedError
