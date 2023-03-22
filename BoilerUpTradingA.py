import math
import statistics
from typing import Dict, List

import numpy as np
import pandas as pd

from datamodel import Order, OrderDepth, TradingState

####################### OUR TRADING ALGORITHM: DELETE WHEN SUBMITTING######################
    # For each product (BANANAS and PEARLS), calculate the average selling price over the past three days.
    # Determine a fair value for each product, based on the average selling price from 3 csv files over 3 days depicting of the sale price for each product
    # Retrieve the order depths for each product.
    # For BANANAS:
    # If there are any SELL orders, sort them by price and select the lowest price.
    # If the lowest ask (SELL order) is lower than the fair value, send a BUY order at that price with the same quantity. Expect the order to trade with the SELL order.
    # If there are any BUY orders, sort them by price and select the highest price.
    # If the highest bid (BUY order) is higher than the fair value, send a SELL order at that price with the same quantity. Expect the order to trade with the BUY order.
    # For PEARLS:
    # If there are any SELL orders, sort them by price and select the lowest price.
    # If the lowest ask (SELL order) is lower than the fair value, send a BUY order at that price with the same quantity. Expect the order to trade with the SELL order.
    # If there are any BUY orders, sort them by price and select the highest price.
    # If the highest bid (BUY order) is higher than the fair value, send a SELL order at that price with the same quantity. Expect the order to trade with the BUY order.
    # Repeat steps 3-5 as often as desired, updating the fair value for each product as necessary based on changing market conditions.

class Trader:
    banana_value = 0
    pearl_value = 0

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        order_depth_banana: OrderDepth = state.order_depths['BANANAS']
        order_depth_pearl: OrderDepth = state.order_depths['PEARLS']

        day1 = pd.read_csv('trades_round_1_day_-1_nn.csv')
        day2 = pd.read_csv('trades_round_1_day_-2_nn.csv')
        day0 = pd.read_csv('trades_round_1_day_0_nn.csv')

        filt_day0_banana = day0[(day0['Symbol'] == 'Banana') & (day0['quantity'] == 1)]
        print(filt_day0_banana)

if __name__ == '__main__':
    pass
    # uncomment when ready
    # Trader().run() # need to pass in an attribute in run that represents state to run the code