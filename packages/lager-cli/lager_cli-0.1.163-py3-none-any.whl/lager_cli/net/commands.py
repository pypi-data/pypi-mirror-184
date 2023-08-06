"""
    lager.lister.commands

    List commands
"""
import json
import click
from texttable import Texttable
from ..context import get_default_gateway
from ..context import get_impl_path
from ..python.commands import run_python_internal

def channel_num(mux, mapping):
    point = mux['scope_points'][0][1]
    if mux['role'] == 'analog':
        return ord(point) - ord('A') + 1
    if mux['role'] == 'logic':
        return int(point)
    try:
        numeric = int(point, 10)
        return numeric
    except ValueError:
        return ord(point) - ord('A') + 1

def get_nets(ctx, gateway):
    session = ctx.obj.session
    resp = session.all_muxes(gateway)
    resp.raise_for_status()
    return resp.json()['muxes']


def display_nets(muxes, netname):
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't'])
    table.set_cols_align(['l', 'r', 'r'])
    table.add_row(['name', 'type', 'channel'])
    for mux in muxes:
        for mapping in mux['mappings']:
            if netname is None or netname == mapping['net']:
                channel = channel_num(mux, mapping)
                table.add_row([mapping['net'], mux['role'], channel])

    click.echo(table.draw())

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
def net(ctx, gateway, dut):
    """
        Active nets for a given DUT
    """
    gateway = gateway or dut
    if ctx.invoked_subcommand is not None:
        return

    if gateway is None:
        gateway = get_default_gateway(ctx)

    muxes = get_nets(ctx, gateway)

    display_nets(muxes, None)

def validate_net(ctx, muxes, netname, role):
    for mux in muxes:
        if mux['role'] != role:
            continue
        for mapping in mux['mappings']:
            if mapping['net'] == netname:
                return mapping
    raise click.UsageError(f'{role.title()} net with name `{netname}` not found!', ctx=ctx)

@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--clear', is_flag=True, default=False, required=False, help='Clear the associated mux')
@click.argument('NETNAME')
def mux(ctx, gateway, dut, mcu, clear, netname):
    """
        Activate a Net
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)
    session = ctx.obj.session

    data = {
        'action': 'mux',
        'mcu': mcu,
        'params': {
            'clear': clear,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()


@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.argument('NETNAME')
def show(ctx, gateway, dut, netname):
    """
        Show the available nets which match a given name
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    muxes = get_nets(ctx, gateway)
    display_nets(muxes, netname)

@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.argument('NETNAME')
def disable(ctx, gateway, dut, mcu, netname):
    """
        Disable Net
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'disable_net',
        'mcu': mcu,
        'params': {
            'netname': netname,
        }
    }
    run_python_internal(
        ctx,
        get_impl_path('enable_disable.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )    

@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.argument('NETNAME')
def enable(ctx, gateway, dut, mcu, netname):
    """
        Disable Net
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'enable_net',
        'mcu': mcu,
        'params': {
            'netname': netname,
        }
    }
    run_python_internal(
        ctx,
        get_impl_path('enable_disable.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    ) 

@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--voltdiv', help='Volts per division')
@click.option('--timediv', help='Time per division')
@click.option('--voltoffset', help='Voltage offset')
@click.option('--timeoffset', help='Time offset')
@click.argument('NETNAME')
def trace(ctx, gateway, dut, mcu, voltdiv, timediv, voltoffset, timeoffset, netname):
    """
        Trace options
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trace',
        'mcu': mcu,
        'params': {
            'voltdiv': voltdiv,
            'timediv': timediv,
            'voltoffset': voltoffset,
            'timeoffset': timeoffset,
            'netname': netname,
        }
    }
    run_python_internal(
        ctx,
        get_impl_path('trace.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )


@net.group()
def trigger():
    pass


MODE_CHOICES = click.Choice(('normal', 'auto', 'single'))
COUPLING_CHOICES = click.Choice(('dc', 'ac', 'low_freq_rej', 'high_freq_rej'))

@trigger.command()
@click.pass_context
@click.argument('NETNAME')
@click.option('--mcu', required=False)
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mode', default='normal', type=MODE_CHOICES, help='Trigger mode', show_default=True)
@click.option('--coupling', default='dc', type=COUPLING_CHOICES, help='Coupling mode', show_default=True)
@click.option('--source', required=False, help='Trigger source', metavar='NET')
@click.option('--slope', type=click.Choice(('rising', 'falling', 'both')), help='Trigger slope')
@click.option('--level', type=click.FLOAT, help='Trigger level')
def edge(ctx, netname, mcu, gateway, dut, mode, coupling, source, slope, level):
    """
    Set edge trigger
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trigger_edge',
        'mcu': mcu,
        'params': {
            'netname': netname,
            'mode': mode,
            'coupling': coupling,
            'source': source,
            'slope': slope,
            'level': level,
        }
    }

    run_python_internal(
        ctx,
        get_impl_path('trigger.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )


@trigger.command()
@click.pass_context
@click.argument('NETNAME')
@click.option('--mcu', required=False)
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mode', default='normal', type=MODE_CHOICES, help='Trigger mode', show_default=True)
@click.option('--coupling', default='dc', type=COUPLING_CHOICES, help='Coupling mode', show_default=True)
@click.option('--source', required=False, help='Trigger source', metavar='NET')
@click.option('--level', type=click.FLOAT, help='Trigger level')
@click.option('--trigger-on', type=click.Choice(('gt', 'lt', 'gtlt')), help='Trigger on')
@click.option('--upper', type=click.FLOAT, help='upper width')
@click.option('--lower', type=click.FLOAT, help='lower width')
def pulse(ctx, netname, mcu, gateway, dut, mode, coupling, source, level, trigger_on, upper, lower):
    """
    Set pulse trigger
    """

    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trigger_pulse',
        'mcu': mcu,
        'params': {
            'netname': netname,
            'mode': mode,
            'coupling': coupling,
            'source': source,
            'level': level,
            'trigger_on': trigger_on,
            'upper': upper,
            'lower': lower,
        }
    }

    run_python_internal(
        ctx,
        get_impl_path('trigger.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )    

@trigger.command()
@click.pass_context
@click.argument('NETNAME')
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--mode', default='normal', type=MODE_CHOICES, help='Trigger mode, e.g. Normal, Automatic, or Single Shot', show_default=True)
@click.option('--coupling', default='dc', type=COUPLING_CHOICES, help='Coupling mode', show_default=True)
@click.option('--source-scl', required=False, help='Trigger source', metavar='NET')
@click.option('--source-sda', required=False, help='Trigger source', metavar='NET')
@click.option('--level-scl', type=click.FLOAT, help='Trigger scl level')
@click.option('--level-sda', type=click.FLOAT, help='Trigger sda level')
@click.option('--trigger-on', type=click.Choice(('start', 'restart', 'stop', 'nack', 'address', 'data', 'addr_data')), help='Trigger on')
@click.option('--address', type=click.INT, help='Address value to trigger on in ADDRESS mode')
@click.option('--addr-width', type=click.Choice(('7', '8', '9', '10')), help='Address width in bits')
@click.option('--data', type=click.INT, help='Data value to trigger on in DATA mode')
@click.option('--data-width', type=click.Choice(('1', '2', '3', '4', '5')), help='Data width in bytes')
@click.option('--direction', type=click.Choice(('write', 'read', 'rw')), help='Direction to trigger on')
def i2c(ctx, netname, gateway, dut, mcu, mode, coupling, source_scl, level_scl, source_sda, level_sda, trigger_on, address, addr_width, data, data_width, direction):
    """
    Set I2C trigger
    """
    if addr_width !=None:
        addr_width = int(addr_width)
    if data_width !=None:
        data_width = int(data_width)
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trigger_i2c',
        'mcu': mcu,
        'params': {
            'netname': netname,
            'mode': mode,
            'coupling': coupling,
            'source_scl': source_scl,
            'source_sda': source_sda,
            'level_scl': level_scl,
            'level_sda': level_sda,
            'trigger_on': trigger_on,
            'address': address,
            'addr_width': addr_width,
            'data': data,
            'data_width': data_width,
            'direction': direction
        }
    }

    run_python_internal(
        ctx,
        get_impl_path('trigger.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )    

@trigger.command()
@click.pass_context
@click.argument('NETNAME')
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--mode', default='normal', type=MODE_CHOICES, help='Trigger mode, e.g. Normal, Automatic, or Single Shot', show_default=True)
@click.option('--coupling', default='dc', type=COUPLING_CHOICES, help='Coupling mode', show_default=True)
@click.option('--source', required=True, help='Trigger source', metavar='NET')
@click.option('--level', default=1.5, type=click.FLOAT, help='Trigger level')
@click.option('--trigger-on', default='start', type=click.Choice(('start', 'error', 'cerror', 'data')), help='Trigger on')
@click.option('--parity', default='none', type=click.Choice(('even', 'odd', 'none')), help='Data trigger parity')
@click.option('--stop-bits', default='1', type=click.Choice(('1', '1.5', '2')), help='Data trigger stop bits')
@click.option('--baud', default=115_200, type=click.INT, help='Data trigger baud')
@click.option('--data-width', type=click.INT, help='Data trigger data width in bits')
@click.option('--data', type=click.INT, help='Data trigger data')
def uart(ctx, netname, gateway, dut, mcu, mode, coupling, source, level, trigger_on, parity, stop_bits, baud, data_width, data):
    """
    Set UART trigger
    """
    if stop_bits !=None:
        stop_bits = float(stop_bits)
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trigger_uart',
        'mcu': mcu,
        'params': {
            'netname': netname,
            'mode': mode,
            'coupling': coupling,
            'source': source,
            'level': level,
            'trigger_on': trigger_on,
            'parity': parity,
            'stop_bits': stop_bits,
            'baud': baud,
            'data_width': data_width,
            'data': data,
        }
    }

    run_python_internal(
        ctx,
        get_impl_path('trigger.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    )

@trigger.command()
@click.pass_context
@click.argument('NETNAME')
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--mode', default='normal', type=MODE_CHOICES, help='Trigger mode, e.g. Normal, Automatic, or Single Shot', show_default=True)
@click.option('--coupling', default='dc', type=COUPLING_CHOICES, help='Coupling mode', show_default=True)
@click.option('--source-mosi-miso', required=False, help='Trigger master/slave data source', metavar='NET')
@click.option('--source-sck', required=False, help='Trigger clock source', metavar='NET')
@click.option('--source-cs', required=False, help='Trigger chip select source', metavar='NET')
@click.option('--level-mosi-miso', type=click.FLOAT, help='Trigger mosi/miso level')
@click.option('--level-sck', type=click.FLOAT, help='Trigger sck level')
@click.option('--level-cs', type=click.FLOAT, help='Trigger cs level')
@click.option('--data', type=click.INT, help='Trigger data value')
@click.option('--data-width', type=click.INT, help='Data width in bits')
@click.option('--clk-slope', type=click.Choice(('positive', 'negative')), help='Slope of clock edge to sample data')
@click.option('--trigger-on', type=click.Choice(('timeout', 'cs')), help='Trigger on')
@click.option('--cs-idle', type=click.Choice(('high', 'low')), help='CS Idle type')
@click.option('--timeout', type=click.FLOAT, help='Timeout length')
def spi(ctx, netname, gateway, dut, mcu, mode, coupling, source_mosi_miso, source_sck, source_cs, level_mosi_miso, level_sck, level_cs, data, data_width, clk_slope, trigger_on, cs_idle, timeout):
    """
    Set SPI trigger
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    data = {
        'action': 'trigger_spi',
        'mcu': mcu,
        'params': {
            'netname': netname,
            'mode': mode,
            'coupling': coupling,
            'source_mosi_miso': source_mosi_miso,
            'source_sck': source_sck,
            'source_cs': source_cs,
            'level_mosi_miso': level_mosi_miso,
            'level_sck': level_sck,
            'level_cs': level_cs,
            'data': data,
            'data_width': data_width,
            'clk_slope': clk_slope,
            'trigger_on': trigger_on,            
            'cs_idle': cs_idle,
            'timeout': timeout
        }
    }

    run_python_internal(
        ctx,
        get_impl_path('trigger.py'),
        dut,
        image='',
        env=(f'LAGER_COMMAND_DATA={json.dumps(data)}',),
        passenv=(),
        kill=False,
        download=(),
        allow_overwrite=False,
        signum='SIGTERM',
        timeout=0,
        detach=False,
        port=(),
        org=None,
        args=(),
    ) 



@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--vavg', is_flag=True, default=False, help='Average voltage')
@click.option('--freq', is_flag=True, default=False, help='Signal Frequency')
@click.argument('NETNAME')
def measure(ctx, gateway, dut, mcu, vavg, freq, netname):
    """
        Measure voltage or frequency
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    session = ctx.obj.session

    data = {
        'action': 'measure',
        'mcu': mcu,
        'params': {
            'vavg': vavg,
            'freq': freq,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()


@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--set-a', help='Set (x,y) location of cursor a')
@click.option('--set-b', help='Set (x,y) location of cursor b')
@click.option('--set-ax', help='Set (x) location of cursor a')
@click.option('--set-bx', help='Set (x) location of cursor b')
@click.option('--set-ay', help='Set (y) location of cursor a')
@click.option('--set-by', help='Set (y) location of cursor b')
@click.option('--move-a', help='Move cursor a from current position by (delta x, delta y)')
@click.option('--move-b')
@click.option('--move-ax')
@click.option('--move-bx')
@click.option('--move-ay')
@click.option('--move-by')
@click.option('--a-values', is_flag=True, default=False)
@click.option('--b-values', is_flag=True, default=False)
@click.argument('NETNAME')
def cursor(ctx, gateway, dut, mcu, set_a, set_b, set_ax, set_bx, set_ay, set_by, move_a, move_b, move_ax, move_bx, move_ay, move_by, a_values, b_values, netname):
    """
        Adjust the scope's cursor
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    session = ctx.obj.session

    data = {
        'action': 'cursor',
        'mcu': mcu,
        'params': {
            'set_a': set_a,
            'set_b': set_b,
            'set_ax': set_ax,
            'set_bx': set_bx,
            'set_ay': set_ay,
            'set_by': set_by,
            'move_a': move_a,
            'move_b': move_b,
            'move_ax': move_ax,
            'move_bx': move_bx,
            'move_ay': move_ay,
            'move_by': move_by,
            'a_values': a_values,
            'b_values': b_values,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()

@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--soc')
@click.option('--full')
@click.option('--empty')
@click.option('--curr-limit')
@click.option('--capacity')
@click.argument('NETNAME')
def battery(ctx, gateway, dut, mcu, soc, full, empty, curr_limit, capacity, netname):
    """
        Control the battery simulator
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    session = ctx.obj.session

    data = {
        'action': 'battery',
        'mcu': mcu,
        'params': {
            'soc': soc,
            'full': full,
            'empty': empty,
            'curr_limit': curr_limit,
            'capacity': capacity,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()


@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--max-settings', is_flag=True, default=False)
@click.option('--voltage')
@click.option('--current')
@click.argument('NETNAME')
def supply(ctx, gateway, dut, mcu, max_settings, voltage, current, netname):
    """
        Control the power supply
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    session = ctx.obj.session

    data = {
        'action': 'supply',
        'mcu': mcu,
        'params': {
            'max_settings': max_settings,
            'voltage': voltage,
            'current': current,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()


@net.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False)
@click.option('--max-settings', is_flag=True, default=False)
@click.option('--voltage')
@click.option('--resistance')
@click.option('--current')
@click.option('--power')
@click.argument('NETNAME')
def eload(ctx, gateway, dut, mcu, max_settings, voltage, resistance, current, power, netname):
    """
        Control the electronic load
    """
    gateway = gateway or dut
    if gateway is None:
        gateway = get_default_gateway(ctx)

    session = ctx.obj.session

    data = {
        'action': 'eload',
        'mcu': mcu,
        'params': {
            'max_settings': max_settings,
            'voltage': voltage,
            'resistance': resistance,
            'current': current,
            'power': power,
            'netname': netname,
        }
    }
    session.net_action(gateway, data).json()
