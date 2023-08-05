from . import models as _m
from ..base import Client, ModelMixin


class BudaPublic(Client, ModelMixin):
    base_url = 'https://www.buda.com/api/v2/'
    error_keys = ['message']

    def __init__(self,
                 timeout: int=None,
                 host: str=None,
                 return_json: bool=False,
                 max_retries: int=None,
                 backoff_factor: float=None,
                 enable_rate_limit: bool=None):
        # Override base_url
        if host is not None:
            self.base_url = host
        super().__init__(
            timeout, max_retries, backoff_factor, enable_rate_limit,
            return_json=return_json,
        )

    def markets(self):
        data = self.get('markets')
        if self.return_json:
            return data
        return [_m.Market.create_from_json(market)
                for market in data['markets']]

    def market_details(self, market_id: str):
        data = self.get(f'markets/{market_id}')
        if self.return_json:
            return data
        return _m.Market.create_from_json(data['market'])

    def ticker(self, market_id: str):
        data = self.get(f'markets/{market_id}/ticker')
        if self.return_json:
            return data
        return _m.Ticker.create_from_json(data['ticker'])

    def order_book(self, market_id: str):
        data = self.get(f'markets/{market_id}/order_book')
        if self.return_json:
            return data
        return _m.OrderBook.create_from_json(data['order_book'])

    def trades(self,
               market_id: str,
               timestamp: int=None,
               limit: int=None):
        data = self.get(f'markets/{market_id}/trades', params={
            'timestamp': timestamp,
            'limit': limit,
        })
        if self.return_json:
            return data
        return _m.Trades.create_from_json(data['trades'])
