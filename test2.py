from pybit import usdt_perpetual, inverse_perpetual



#API Ignat
session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='jkVW1Q7h6GvTawBHIT',
    api_secret='I0gX1MLecoi8SlyCIIUEWo315VrWD2bs6moL'
)
session_unauth = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com"
)

print(session_auth.get_wallet_balance()['result']['USDT']['equity'])






#session_auth = usdt_perpetual.HTTP(
#    endpoint="https://api.bybit.com",
#    api_key='H9X78xMQgIP5yDSyok',
#    api_secret='YeQTC5zNr7PvHcmjwkJVBFywPnie9pdLe0cw'
#)
#session_unauth = inverse_perpetual.HTTP(
#    endpoint="https://api.bybit.com"
#)
#
#print(session_auth.get_wallet_balance()['result']['USDT']['equity'])


print(len(str(0.0564)))
print(round(0.2, 3))
#session_auth = usdt_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com",
#    api_key='gw90bhuJCb29ZaeDU9',
#    api_secret='KwqbUpaV1CyCv9CLcSiRHcbzv6S1bgxogAsb'
#)
#session_unauth = inverse_perpetual.HTTP(
#    endpoint="https://api-testnet.bybit.com"
#)
#
#print(session_auth.get_wallet_balance()['result']['USDT']['equity'])