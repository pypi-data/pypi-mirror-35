from . import constants as _c
from .client_auth import KrakenAuth
from .client_public import KrakenPublic

__all__ = [
    'Kraken',
]


class Kraken(object):
    # Enum Types
    Currency = _c.Currency
    Symbol = _c.Symbol
    # Clients
    Auth = KrakenAuth
    Public = KrakenPublic
