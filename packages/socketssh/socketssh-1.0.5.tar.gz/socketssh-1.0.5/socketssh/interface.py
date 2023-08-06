#!/usr/bin/python
# coding=UTF-8 

'''socketssh shell'''

__author__ = "jiegl"

import sys
import os
import optparse
from socketssh import server, client

def main():

	usage = 'Usage: %prog [options] arg1 arg2 ...'
	
	parser = optparse.OptionParser(usage,version='%prog 1.0.3')

	parser.add_option('-t', '--type', action='store', dest='type', type='string', metavar='xxx', help='specify type of operation required')
	
	server_option = optparse.OptionGroup(parser,'Server Options(Need to fill in the rabbitmq option)')
	server_option.add_option('-l', '--listen_port', action='store', dest='listen_port', type='int', metavar='xxx', help='port that the server listens on.')
	server_option.add_option('-n', '--socket_number', action='store', dest='socket_number', type='int', metavar='xxx', help='port that the server listens on.')
	parser.add_option_group(server_option)
	
	client_option = optparse.OptionGroup(parser,'Client Options')
	client_option.add_option('-H', '--server_host', action='store', dest='server_host', type='string', metavar='xxx', help='connected server host.')
	client_option.add_option('-P', '--server_port', action='store', dest='server_port', type='int', metavar='xxx', help='connected server port.')
	parser.add_option_group(client_option)

	insert_option = optparse.OptionGroup(parser,'Insert Options(Need to fill in the rabbitmq option)')
	insert_option.add_option('-m', '--shell', action='store', dest='shell', type='string', metavar='xxx', help='command that needs to be executed')
	parser.add_option_group(insert_option)

	rabbitmq_option = optparse.OptionGroup(parser,'Rabbitmq Options')
	rabbitmq_option.add_option('-s', '--rabbitmq_host', action='store', dest='rabbitmq_host', type='string', metavar='xxx', help='connected rabbitmq host address')
	rabbitmq_option.add_option('-o', '--rabbitmq_port', action='store', dest='rabbitmq_port', type='int', metavar='xxx', help='connected rabbitmq port')
	rabbitmq_option.add_option('-u', '--rabbitmq_user', action='store', dest='rabbitmq_user', type='string', metavar='xxx', help='connected rabbitmq username')
	rabbitmq_option.add_option('-p', '--rabbitmq_pass', action='store', dest='rabbitmq_pass', type='string', metavar='xxx', help='connected rabbitmq password')
	rabbitmq_option.add_option('-q', '--rabbitmq_queue', action='store', dest='rabbitmq_queue', type='string', metavar='xxx', help='connected rabbitmq queue name')
	parser.add_option_group(rabbitmq_option)

	(options, args) = parser.parse_args() 
	if options.type == None:
		print(parser.usage)        
		exit(0)
	else:

		if options.type == "server":

			if options.listen_port == None and options.socket_number == None and options.rabbitmq_host == None and options.rabbitmq_port == None\
			 and options.rabbitmq_user == None and options.rabbitmq_pass == None and options.rabbitmq_queue == None:
				print(parser.usage)        
				exit(0)

			server_exec(options.listen_port, options.socket_number, options.rabbitmq_host, options.rabbitmq_port, 
				options.rabbitmq_user, options.rabbitmq_pass, options.rabbitmq_queue)

		elif options.type == "client":

			if options.server_host == None and options.server_port == None :
				print(parser.usage)
				exit(0)

			client_exec(options.server_host, options.server_port)

		elif options.type == "insert":

			if options.rabbitmq_host == None and options.rabbitmq_port == None and options.rabbitmq_user == None and options.rabbitmq_pass == None\
				and options.rabbitmq_queue and options.shell == None :
				print(parser.usage)
				exit(0)

			insert_exec(options.rabbitmq_host, options.rabbitmq_port, options.rabbitmq_user, options.rabbitmq_pass, 
				options.rabbitmq_queue, options.shell)


def server_exec(port, socket_number, rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_pass , rabbitmq_queue):

	server_object = server.Server()

	server_object.socket_connect(socket_number, port)

	server_object.rabbit_connect(rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_pass, rabbitmq_queue)

	server_object.socket_start()

def client_exec(host, port):

	client_object = client.Client()

	client_object.socket_connect(host, port)

	client_object.socket_start()

def insert_exec(rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_pass, rabbitmq_queue, shell):

	server_object = server.Server()

	server_object.rabbit_connect(rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_pass, rabbitmq_queue)

	server_object.rabbit_insert(shell)

if __name__ == '__main__':    
	main()
