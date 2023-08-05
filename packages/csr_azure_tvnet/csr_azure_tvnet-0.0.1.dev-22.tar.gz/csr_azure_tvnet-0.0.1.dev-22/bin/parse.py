#!/usr/bin/env python

'''
Cisco Copyright 2018
Author: Vamsi Kalapala <vakalapa@cisco.com>

FILENAME: PARSE.PY

'''



import time
import random
import string
import logging
import ipaddress
from azurestorage import azsto

log = logging.getLogger('dmvpn')
log.setLevel(logging.INFO)

def parse_decoded_custom_data(filename, keyword = 'AzureTransitVnet'):

	section_dict = {}
	section_flag = False
	try:
		with open(filename) as filecontents:
			for line in filecontents:
				if 'section:' in line:
					if keyword in line:
						section_flag = True
					else:
						section_flag = False

				if section_flag:
					split_line = line.split(' ')
					if len(split_line) == 2:
						section_dict[split_line[0].strip()] = split_line[1].strip()
					else:
						log.info('[ERROR] command parsing failed for %s' % str(split_line))
	except IOError as e:
		log.info('[ERROR] %s' % e)
		return False
	log.info(section_dict)
	return section_dict

def write_all_files(section_dict, file_list = ['spoke', 'hub-1', 'hub-2', 'dmvpn']):
	storage_object = section_dict['storage_object']

	if 'hub-1' in section_dict['role']:
		file_list = ['spoke', 'hub-1', 'dmvpn']
	elif 'hub-2' in section_dict['role']:
		file_list = ['spoke', 'hub-2', 'dmvpn']
	elif 'spoke' in section_dict['role']:
		file_list = ['spoke']

	for file_content in file_list:
		try:
			file_contents = section_dict[file_content]
			file_name = section_dict['file_names'][file_content]
			log.info('[INFO] Savings contents for {} in {} with {}'.format(file_content, file_name, str(file_contents)))
			storage_object.write_file_contents(section_dict['file_share'],section_dict['folder'],file_name,file_contents)
		except KeyError:
			log.info('[ERROR] counld not save file for {}'.format(file_content))


def get_all_files(section_dict, file_list = ['spoke', 'hub-1', 'hub-2', 'dmvpn']):
	storage_object = section_dict['storage_object']
	hub_1_flag = False
	if 'hub' in section_dict['role']:
		hub_1_flag = True
	elif 'spoke' in section_dict['role']:
		hub_one_file = storage_object.file_exists(section_dict['file_share'],section_dict['folder'],section_dict['file_names']['hub-1'])
		hub_two_file = storage_object.file_exists(section_dict['file_share'],section_dict['folder'],section_dict['file_names']['hub-2'])
		if hub_one_file and not hub_two_file:
			file_list = ['spoke', 'hub-1', 'dmvpn']
			section_dict['hub-2'] = {'pip': '255.255.255.254', 'nbma': '1.1.1.2'}
		elif not hub_one_file and hub_two_file:
			file_list = ['spoke', 'hub-2', 'dmvpn']
			section_dict['hub-1'] = {'pip': '255.255.255.254', 'nbma': '1.1.1.1'}
	for file_content in file_list:
		status = False
		tries = 0
		while not status:
			log.info('{} {} {}'.format(section_dict['file_share'],section_dict['folder'],section_dict['file_names'][file_content]))
			status, contents = storage_object.get_file_contents_json(section_dict['file_share'],section_dict['folder'],section_dict['file_names'][file_content])
			if status:
				log.info('[INFO] Retrived file contents for {}: {}'.format(file_content, str(contents)))
			else:
				if hub_1_flag:
					break
				log.info('[ERROR] Error while retrieving {}. Try num: {}'.format(file_content,str(tries)))
				time.sleep(50)
				tries += 1
		if contents:
			section_dict[file_content] = contents
	return section_dict

def random_string(choice='int'):
	validcharacters = string.ascii_lowercase + string.digits
	if choice == 'int':
		validcharacters = string.digits
	return ''.join(random.choice(validcharacters) for _ in range(8))

def setup_file_dict(section_dict):
	section_dict['folder'] = 'config'
	section_dict['file_names'] = {'hub-1' : 'hub1.json', 'hub-2' : 'hub2.json','spoke' : 'spokes.json','dmvpn' : 'dmvpn.json'}
	try:
		file_share = section_dict['transitvnetname']
		section_dict['file_share'] = file_share
	except KeyError:
		file_share = 'new'
		section_dict['file_share'] = file_share
	
	return section_dict

def setup_default_dict(section_dict):

	try:
		if section_dict['dmvpn'] is None:
			section_dict['dmvpn'] = {}
	except KeyError:
		section_dict['dmvpn'] = {}

	try:
		DMVPNTunnelIpCidrStr = section_dict['DMVPNTunnelIpCidr']
	except KeyError:
		DMVPNTunnelIpCidrStr = '1.1.1.0/24'
	try:
		DMVPNTunnelIpCidrStr = section_dict['dmvpn']['DMVPNTunnelIpCidr']
	except KeyError:
		pass

	DMVPNTunnelIpCidr = ipaddress.IPv4Network(DMVPNTunnelIpCidrStr.decode('utf-8'))
	section_dict['DMVPNTunnelIpCidr'] = DMVPNTunnelIpCidr	

	default_dict = {
		"ConnectionName" : "tvnet",
		"RoutingProtocol" : "EIGRP",
		"TunnelID" : 11,
		"TunnelKey" : 012210,
		"SharedKey" : 'ciscokey',
		"IpsecCipher" : "esp-aes",
		"IpsecAuthentication" : "esp-sha-hmac",
		"RoutingProtocolASN" : 64512,
		"NHRPAuthString" : 'cisco',
		"NHRPNetworkId" : 1024
	}

	for key,value in default_dict.items():
		try:
			section_dict[key]
			section_dict['dmvpn'][key] = section_dict[key]
		except KeyError:
			try:
				section_dict['dmvpn'][key]
				section_dict[key] = section_dict['dmvpn'][key]
			except KeyError:
				section_dict[key] = value
				section_dict['dmvpn'][key] = value
	
	tunnel_addressing_dict = {	
		"DMVPNTunnelIpCidr" : DMVPNTunnelIpCidr,
		"DMVPNHubTunnelIp1" : DMVPNTunnelIpCidr.network_address + 1,
		"DMVPNHubTunnelIp2" : DMVPNTunnelIpCidr.network_address + 2,
		"DMVPNTunnelIpMask" : DMVPNTunnelIpCidr.netmask,
		"DMVPNTunnelIpNetworkNum" : DMVPNTunnelIpCidr.network_address,
		"DMVPNTunnelIpHostMask" : DMVPNTunnelIpCidr.hostmask,
		"DMVPNTunnelIpPrefixLen" : DMVPNTunnelIpCidr.prefixlen
	}

	for key,value in tunnel_addressing_dict.items():
		section_dict[key] = value
		section_dict['dmvpn'][key] = value

	'''
	try:
		section_dict['strgacctname'] = os.environ['AZURE_STORAGE_NAME']
		section_dict['strgacckey'] = os.environ['AZURE_STORAGE_KEY']
	except KeyError as e:
		log.error('[INFO] Couldnot find env variable %s' % e)
		#return None'''

	return section_dict


if __name__ == '__main__': # pragma: no cover
	parse_decoded_custom_data('sampledecodedCustomData')