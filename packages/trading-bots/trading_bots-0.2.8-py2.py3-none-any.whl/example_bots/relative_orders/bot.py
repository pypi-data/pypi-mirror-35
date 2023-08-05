from collections import namedtuple

from trading_bots.bots import Bot
from trading_bots.contrib.clients import Market, Side
from trading_bots.contrib.clients import buda
from trading_bots.utils import truncate_to


class RelativeOrders(Bot):
    label = 'RelativeOrders'

    def _setup(self, config):
        # Set market
        self.market = Market(config['market'])
        # Set buda trading client
        self.buda = buda.BudaTrading(
            self.market, dry_run=self.dry_run, timeout=self.timeout, logger=self.log, store=self.store)

    def _algorithm(self):
        # Get middle price from spread
        max_bid, min_ask = self.buda.get_spread_details()
        middle_price = (max_bid + min_ask) / 2
        self.log.info(f'Ticker prices:   Bid: {max_bid} | Ask {min_ask} | Middle {middle_price}')
        # Offset prices from middle using configured price multipliers
        prices_config = self.config['prices']
        bid_price = middle_price * prices_config['buy_multiplier']
        ask_price = middle_price * prices_config['sell_multiplier']
        self.log.info(f'Relative prices: Bid {bid_price} | Ask {ask_price}')
        # Cancel open orders
        self.log.info('Closing open orders')
        self.buda.cancel_orders()

        # Get available amounts
        # Adjust bid and ask amounts
        amounts_config = self.config['amounts']
        amount_base = min(amounts_config['max_base'], self.buda.wallets.base.get_available())
        amount_quote = min(amounts_config['max_quote'], self.buda.wallets.quote.get_available())
        self.log.debug(' | '.join([
            'Amounts',
            f'Bid: {amount_quote} {self.market.quote}',
            f'Ask: {amount_base} {self.market.base}'
        ]))

        # Start strategy
        self.log.info('Starting order deployment')
        # Deploy orders
        deploy_list = self.get_deploy_list()
        self.deploy_orders(deploy_list)

    def _abort(self):
        self.log.error('Aborting strategy, cancelling all orders')
        try:
            self.cancel_orders()
        except Exception:
            self.log.exception(f'Failed!, some orders might not be cancelled')
            raise
        else:
            self.log.info(f'All open orders were cancelled')

    def get_deploy_list(self):

        Order = namedtuple('order', 'amount price side')
        deploy_list = []

        # Available is on quote currency when side is sell
        def quote_to_base_amount(_amount, _price):
            quote_amount = _amount / _price
            return self.truncate_amount(quote_amount)

        buy_order_price = self.truncate_price(self.bid_price)
        buy_order_amount = quote_to_base_amount(self.quote_amount, buy_order_price)
        sell_order_price = self.truncate_price(self.ask_price)
        sell_order_amount = self.truncate_amount(self.base_amount)

        if buy_order_amount > self.buda.min_order_amount:
            deploy_list.append(Order(buy_order_amount, buy_order_price, Side.BUY))
        if sell_order_amount > self.buda.min_order_amount:
            deploy_list.append(Order(sell_order_amount, sell_order_price, Side.SELL))
        return deploy_list

    def deploy_orders(self, deploy_list: list):
        self.log.info(f'Deploying {len(deploy_list)} new orders')
        for order in deploy_list:
            self.buda.place_limit_order(
                side=order.side,
                amount=order.amount,
                price=order.price,
            )

    def truncate_amount(self, value):
        return truncate_to(value, self.market.base)

    def truncate_price(self, value):
        return truncate_to(value, self.market.quote)
