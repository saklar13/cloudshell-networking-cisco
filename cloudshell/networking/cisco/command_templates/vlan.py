__author__ = 'g8y3e'

from cloudshell.networking.utils import *
from cloudshell.networking.cisco.command_templates.cisco_interface \
    import CiscoInterface, ParametersService, CommandTemplate

class Vlan(CiscoInterface):
    COMMANDS_TEMPLATE = {
        'ip_address': CommandTemplate('ip address {0} {1}', [validateIP, validateIP],
                                      ['Wrong ip address!', 'Wrong ip mask!']),
        'configure_vlan': CommandTemplate('vlan {0}', validateVlanRange, 'Cannot create vlan - wrong vlan number(s)'),
        'exit': CommandTemplate('exit'),
        'state_active': CommandTemplate('state active'),
        'hsrp': CommandTemplate('hsrp {0}', ['[0-9]+'],
                                ['Wrong router protocol id!']),
        'authentication': CommandTemplate('authentication {0}', [r'\w+'],
                                          ['Wrong authentication name!']),
        'ip': CommandTemplate('ip {0}', [validateIP],
                              ['Wrong ip address!']),
        'no_shutdown': CommandTemplate('no shutdown'),
        'preempt': CommandTemplate('preempt'),
        'priority': CommandTemplate('priority {0}', ['[0-9]+'], ['Wrong priority number!']),
        'track': CommandTemplate('track {0} decrement {1}', [r'[0-9]+', r'[0-9]+'],
                                  ['Wrong track number!', 'Wrong track decrement number!'])
    }

    def get_commands_list(self, ordered_parameters_dict):
        prepared_commands = []

        for command, value in ordered_parameters_dict.iteritems():
            if command in Vlan.COMMANDS_TEMPLATE:
                command_template = Vlan.COMMANDS_TEMPLATE[command]
                prepared_commands.append(ParametersService.get_validate_list(command_template, value))

        return prepared_commands




