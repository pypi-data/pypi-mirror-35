#!/usr/bin/env python

import re
import time
import socket
import configs
import logging
import ipaddress
import getmetadata
from parse import *
from command import *

log = logging.getLogger('dmvpn')
log.setLevel(logging.INFO)

def configure_transit_vnet(section_dict, tunn_addr):
	'''
	WAIT FOR IT

	'''
	configure_crypto_policy(section_dict['role'], section_dict)
	configure_tunnel(section_dict['role'], section_dict, tunn_addr)
	configure_routing(section_dict['role'], section_dict, tunn_addr)
	return section_dict



def configure_crypto_policy(role, section_dict):
	'''
	This functions is reposnible for configuring the router with appropriate Crypto Policy.
	Right now, we will be configuring the general crypto policy (See configs.py variable crypto_policy_general)
	
	The config string is appendedly accordingly with fields from section_dict

	Args:
		ROLE, SECTION_DICT

	Returns:
		None

	'''
	if 'hub' in role:
		vrf_config = configs.hub_vrf_config.format(
				ConnName = section_dict['dmvpn']["ConnectionName"],
				TunnelId = section_dict['dmvpn']["TunnelID"],
				RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"])
			)
		output = cmd_configure(vrf_config)
		log.info("[INFO] [AzureTransitVNET] Configured HUB VRF successfully")
		cmd_execute("send log [INFO] [AzureTransitVNET] Configured HUB VRF successfully")

	crypto_config = configs.crypto_policy_general.format(
			ConnName = section_dict['dmvpn']["ConnectionName"],
			TunnelId = section_dict['dmvpn']["TunnelID"],
			SharedKey = section_dict['dmvpn']["SharedKey"],
			IpsecCipher = section_dict['dmvpn']["IpsecCipher"],
			IpsecAuthentication = section_dict['dmvpn']["IpsecAuthentication"]
		)

	output = cmd_configure(crypto_config)
	log.info('[INFO] [AzureTransitVNET] Configured crypto policy general successfully')
	cmd_execute("send log [INFO] [AzureTransitVNET] Configured crypto policy general successfully")


def configure_tunnel(role, section_dict, tunn_addr):
	cmd = ''
	if 'hub' in role:
		if 'eigrp' in section_dict['dmvpn']["RoutingProtocol"].lower():
			cmd = configs.hub_tunnel_config_eigrp
			cmd = cmd.format(
					TunnelId = section_dict['dmvpn']["TunnelID"],
					TunnelIP = str(tunn_addr),
					RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"]),
					DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
					AuthString = section_dict['dmvpn']["NHRPAuthString"],
					NHRPNetworkId = str(section_dict['dmvpn']["NHRPNetworkId"]),
					TunnelKey = str(section_dict['dmvpn']["TunnelKey"]),
					ConnName = section_dict['dmvpn']["ConnectionName"]
				)
		elif 'bgp' in section_dict['dmvpn']["RoutingProtocol"].lower():
			cmd = configs.hub_tunnel_config_bgp
			cmd = cmd.format(
					TunnelId = section_dict['dmvpn']["TunnelID"],
					TunnelIP = str(tunn_addr),
					DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
					AuthString = section_dict['dmvpn']["NHRPAuthString"],
					NHRPNetworkId = str(section_dict['dmvpn']["NHRPNetworkId"]),
					TunnelKey = str(section_dict['dmvpn']["TunnelKey"]),
					ConnName = section_dict['dmvpn']["ConnectionName"]
				)
	else:
		try:
			hub1_pip = section_dict['hub-1']['pip']
		except KeyError:
			return None
		try:
			hub2_pip = section_dict['hub-2']['pip']
		except (KeyError,TypeError) as e:
			log.info('[ERROR] No HUB-2 dict was found! {}'.format(e))
			hub2_pip = None
		if hub2_pip is not None:
			cmd = configs.spoke_tunnel_config_general
			cmd = cmd.format(
					TunnelId = section_dict['dmvpn']["TunnelID"],
					TunnelIP = str(tunn_addr),
					DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
					AuthString = section_dict['dmvpn']["NHRPAuthString"],
					DMVPNHubTunnelIp1 =  str(section_dict['dmvpn']["DMVPNHubTunnelIp1"]),
					DMVPNHubIp1 = str(hub1_pip),
					DMVPNHubTunnelIp2 =  str(section_dict['dmvpn']["DMVPNHubTunnelIp2"]),
					DMVPNHubIp2 = str(hub2_pip),
					NHRPNetworkId = str(section_dict['dmvpn']["NHRPNetworkId"]),
					TunnelKey = str(section_dict['dmvpn']["TunnelKey"]),
					ConnName = section_dict['dmvpn']["ConnectionName"]
				)
		else:
			cmd = configs.spoke_tunnel_config_general_singlehub
			cmd = cmd.format(
					TunnelId = section_dict['dmvpn']["TunnelID"],
					TunnelIP = str(tunn_addr),
					DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
					AuthString = section_dict['dmvpn']["NHRPAuthString"],
					DMVPNHubTunnelIp1 =  str(section_dict['dmvpn']["DMVPNHubTunnelIp1"]),
					DMVPNHubIp1 = str(hub1_pip),
					NHRPNetworkId = str(section_dict['dmvpn']["NHRPNetworkId"]),
					TunnelKey = str(section_dict['dmvpn']["TunnelKey"]),
					ConnName = section_dict['dmvpn']["ConnectionName"]
				)
	output = cmd_configure(cmd)
	log.info(output)
	cmd_execute("send log [INFO] [AzureTransitVNET] Configured {} tunnel ".format(role))



def configure_routing(role, section_dict, tunn_addr):

	if 'eigrp' in section_dict['dmvpn']["RoutingProtocol"].lower():
		if 'hub' in role:
			cmd = configs.routing_eigrp_vrf
			cmd = cmd.format(
						RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"]),
						ConnName = section_dict['dmvpn']["ConnectionName"],
						DMVPNTunnelIpNetworkNum = str(section_dict['dmvpn']["DMVPNTunnelIpNetworkNum"]),
						DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
						TunnelId = section_dict['dmvpn']["TunnelID"],
						TunnelIP = str(tunn_addr)
					)
		else:			
			cmd = configs.routing_eigrp
			cmd = cmd.format(
						RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"]),
						DMVPNTunnelIpNetworkNum = str(section_dict['dmvpn']["DMVPNTunnelIpNetworkNum"]),
						DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
						TunnelId = section_dict['dmvpn']["TunnelID"],
						TunnelIP = str(tunn_addr)
					)
	elif 'bgp' in section_dict['dmvpn']["RoutingProtocol"].lower():
		if 'hub' in role:
			cmd = configs.routing_bgp_vrf
			cmd = cmd.format(
						RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"]),
						ConnName = section_dict['dmvpn']["ConnectionName"],
						DMVPNTunnelIpNetworkNum = str(section_dict['dmvpn']["DMVPNTunnelIpNetworkNum"]),
						DMVPNTunnelIpPrefixLen = str(section_dict['dmvpn']["DMVPNTunnelIpPrefixLen"]),
						DMVPNTunnelIpMask = str(section_dict['dmvpn']["DMVPNTunnelIpMask"]),
						TunnelId = section_dict['dmvpn']["TunnelID"],
						TunnelIP = str(tunn_addr)
					)
		else:					
			cmd = configs.routing_bgp
			cmd = cmd.format(
						RoutingProtocolASN = str(section_dict['dmvpn']["RoutingProtocolASN"]),
						DMVPNTunnelIpNetworkNum = str(section_dict['dmvpn']["DMVPNTunnelIpNetworkNum"]),
						DMVPNHubTunnelIp1 = str(section_dict['dmvpn']["DMVPNHubTunnelIp1"]),
						DMVPNHubTunnelIp2 = str(section_dict['dmvpn']["DMVPNHubTunnelIp2"]),
						TunnelIP = str(tunn_addr)
					)
	
	output = cmd_configure(cmd)
	print(output)
	cmd_execute("send log [INFO] [AzureTransitVNET] Configured {} {} routing.".format(
			role,
			section_dict['dmvpn']["RoutingProtocol"].lower()
		))


def parse_sh_run():
	'''
	Get running config from CSR.
	'''
	output = cmd_execute('show run')
	print(output)

def get_interfaces():
	output = cmd_execute('sh ip int br')
	print(output)
	regex = r"GigabitEthernet\d+"
	interfaces = re.findall(regex, output)
	return interfaces

def configure_get_interfaces():
	configure_interface_dhcp()
	interface_dict = get_interfaces_ips()
	print(interface_dict)

def get_interfaces_ips():
	interfaces = get_interfaces()
	interface_dict = {}
	for interface in interfaces:
		print('[INFO] Working on {} interface'.format(interface))
		output = cmd_execute('sh int {} | inc Internet address is'.format(interface))
		if '/' not in output:
			time.sleep(10)
			output = cmd_execute('sh int {} | inc Internet address is'.format(interface))
		print(output)
		output = output.replace('Internet address is' , '')
		output = output.replace(' ' , '')
		output = output.replace('\n' , '')
		obj = ipaddress.IPv4Interface(u'{}'.format(output))
		interface_dict[interface]= obj
	return interface_dict

def configure_interface_dhcp():
	interfaces = get_interfaces()
	for interface in interfaces:
		output = cmd_configure('''int {}
no shu
ip addr dhcp'''.format(interface))
		print(output)

def setup_dmvpn_dict(section_dict):
	param_list = ['TunnelKey', 'RoutingProtocol', 'transitvnetname']
	dmvpn_dict = {}
	for param in param_list:
		dmvpn_dict[param] = section_dict[param]
	return dmvpn_dict