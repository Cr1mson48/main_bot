from pybit import usdt_perpetual, inverse_perpetual
from time import sleep


ws_linear = usdt_perpetual.WebSocket(
    test=True,
    api_key="EVAhEFgFhuZPscVO7o",
    api_secret="DDxcvmZlyFuQuAinjDvePQUguaiWT8LuZvH2",
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)
def handle_message(msg):
    print(msg)



ws_linear.execution_stream(
    handle_message
)
while True:
    sleep(1)