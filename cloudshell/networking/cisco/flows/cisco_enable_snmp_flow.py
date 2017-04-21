#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.networking.cisco.command_actions.enable_disable_snmp_actions import EnableDisableSnmpActions

from cloudshell.devices.flows.cli_action_flows import EnableSnmpFlow


class CiscoEnableSnmpFlow(EnableSnmpFlow):
    def __init__(self, cli_handler, logger):
        """
        Enable snmp flow
        :param cli_handler:
        :param logger:
        :return:
        """
        super(CiscoEnableSnmpFlow, self).__init__(cli_handler, logger)
        self._cli_handler = cli_handler

    def _execute_flow(self, snmp_parameters):
        snmp_community = snmp_parameters.snmp_community

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as session:
            snmp_actions = EnableDisableSnmpActions(session, self._logger)
            current_snmp_config = snmp_actions.get_current_snmp_communities(session)

            if snmp_community not in current_snmp_config:
                snmp_actions.enable_snmp(snmp_community)
            else:
                self._logger.debug("SNMP Community '{}' already configured".format(snmp_community))
