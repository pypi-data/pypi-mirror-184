import unittest
from p2p_crypto import Binance
from p2p_crypto import paymentTypes
import random

def test_price_type() -> None:
    binance = Binance()
    for fiat in paymentTypes.keys():
        for payment in paymentTypes[fiat]:
            binance.getPrice(
                fiat=fiat,
                token="USDT",
                payments=[payment],
                merchant=False,
                rows=1,
                operation="SELL"
            )
        
            assert isinstance(binance.prices, list)
            assert isinstance(binance.data, list)
    
def test_price_amount() -> None:
    binance = Binance()
    for fiat in paymentTypes.keys():
        for payment in paymentTypes[fiat]:
            prices = binance.getPrice(
                fiat=fiat,
                token="USDT",
                payments=[payment],
                merchant=False,
                rows=1,
                operation="SELL"
            )

            assert len(prices) == 1