import numpy as np


targets = [
    'AAPL',
    'AMD',
    'NFLX',
]


def handle_data(ctx, data):
    print('run handledata')

    print('## symbols')
    assets = [
        symbol(a)
        for a in targets
    ]

    target = np.random.choice(assets)
    print('choice', target)

    print('## history')
    dat = data.history(symbol('AAPL'), 'price', 5, '1d')
    #print(dat)
    dat = data.history(symbol('AAPL'), ['close', 'open', 'high', 'close', 'volume'], 1, 'minute')
    #print(dat)
    dat = data.history(symbol('AAPL'), 'price', 1, 'minute')
    print(dat)

    print('## current')
    dat = data.current(assets, 'price')
    print(dat)

    print('## open')
    orders = get_open_orders()
    print(sum([len(s) for _, s in orders.items()]), 'opens')
    for order_asset, asset_orders in orders.items():
        for o in asset_orders:
            print('cancel', order_asset.symbol, o.id)
            cancel_order(o)

    for asset in assets:
        if asset == target:
            if data.can_trade(asset):
                print('buy {}'.format(asset))
                order_target_percent(asset, 0.3)
        else:
            if data.can_trade(asset):
                print('sell {}'.format(asset))
                order_target_percent(asset, 0)


def initialize(context):
    print('run initialize')
    from pylivetrader.misc.security_list import SecurityListSet

    set_asset_restrictions(SecurityListSet(get_datetime, context.asset_finder).restrict_leveraged_etfs)

    set_long_only()

    # set_max_order_count(100, on_error='log')

    schedule_function(
        run_on_market_open,
        date_rules.every_day(),
        time_rules.market_open(minutes=1)
    )

    schedule_function(
        before_market_close,
        date_rules.every_day(),
        time_rules.market_close(minutes=5)
    )


def run_on_market_open(context, data):

    print('run#on_market_open')


def before_market_close(context, data):
    print("run#before_market_close")
