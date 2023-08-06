from catalyst.api import symbol, order
from catalyst.utils.run_algo import run_algorithm
import pandas as pd


def initialize(context):
    pass


def handle_data(context, data):
    history = data.history(symbol("omg_btc"), ['close'],
                           bar_count=1100,
                           frequency='1T')

    print('\nnow: %s\n%s' % (data.current_dt, history))
    if not hasattr(context, 'i'):
        context.i = 0
    context.i += 1
    print(history)
    #if context.i > 100:
    #    raise Exception('stop')
    #order(symbol("XRP_BTC"), -1)


live = True
if live:
    run_algorithm(initialize=lambda ctx: True,
                  handle_data=handle_data,
                  exchange_name='poloniex',
                  quote_currency='usd',
                  algo_namespace='issue-323',
                  live=live,
                  data_frequency='minute',
                  capital_base=3000,
                  simulate_orders=False,
                  auth_aliases=dict(poloniex='auth3')#poloniex,auth3"
                  #start=pd.to_datetime('2017-09-14', utc=True),
                  #end=pd.to_datetime('2018-08-01', utc=True),
                  )
