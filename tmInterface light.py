# not working

from tminterface.interface import TMInterface
from tminterface.client import run_client


def on_registered(iface: TMInterface) -> None:
    print(f'Registered to {iface.server_name}')


def on_run_step(iface: TMInterface, _time: int):
    if _time == 1000:
        iface.set_input_state(right=True, accelerate=True, brake=True)


def main():
    server_name = 'TMInterface0'
    print(f'Connecting to {server_name}...')
    iface = run_client(on_registered=on_registered)
    iface.register_callback(on_run_step)


if __name__ == '__main__':
    main()
