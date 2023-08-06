import os
import json
from lager.pcb.net import Net, NetType

def net_setup(*args, **kwargs):
    pass

def net_teardown(*args, **kwargs):
    pass

def disable_net(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.disable() 

def enable_net(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.enable() 

def main():
    command = json.loads(os.environ['LAGER_COMMAND_DATA'])
    if command['action'] == 'disable_net':
        disable_net(**command['params'])
    elif command['action'] == 'enable_net':
        enable_net(**command['params'])            
    else:
        pass

if __name__ == '__main__':
    main()