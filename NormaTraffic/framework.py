#Imports if needed
import sys
import os
import socket
#Functions
def hardcoded_file():
	file = open(ProgLoc+"/PyTgen/configs/"+SysHostname+".py","w")
	file.write("import logging")
	file.write("\nclass Conf(object):")
	file.write("\n\tmaxthreads=15")
	file.write("\n\tloglevel=logging.DEBUG")
	file.write("\n\tssh_commands = ['ls', 'cd', 'cd /etc', 'ps ax', 'date', 'mount', 'free', 'vmstat', 'touch /tmp/tmpfile', 'rm /tmp/tmpfile', 'ls /tmp/tmpfile', 'tail /etc/hosts', 'tail /etc/passwd', 'tail /etc/fstab', 'cat /var/log/messages', 'cat /etc/group', 'cat /etc/mtab']")
	file.write("\n\tftp_put = ['~/files/file%s' % i for i in xrange(0, 9)]")
	file.write("\n\tftp_get = ['~/files/file%s' % i for i in xrange(0, 9)]")
	file.write("\n\tsftp_put = [('~/files/file%s' % i, '/tmp/file%s' % i) for i in xrange(0, 9)]")
	file.write("\n\tsftp_get = [('/media/share/files/file%s' % i, '~/files/tmp/file%s' % i) for i in xrange(0, 9)]")
	file.write("\n\tjobdef=[\n")
	file.close()

def add_more():
	#Ask for confirmation, maybe make a function
	continueAdd = raw_input("Add more traffic? (y/n) => ")
	
	if continueAdd == "n":
		#run the program
		file = open(ProgLoc+"/PyTgen/configs/"+SysHostname+".py","a")
		file.write("]")
		file.close()
		
		print("Program Will Now Start Generating Traffic...")
		
		#Run program
		os.chdir(ProgLoc+"/PyTgen")
		os.system("python run.py")
		
	else:
		file = open(ProgLoc+"/PyTgen/configs/"+SysHostname+".py","a")
		file.write(",\n")
		file.close()
		
def check_hostnameconfigs():
	#This function will check if Hostname.py exist in configs.
	#If no, it will create the file.
	
	print("Program is checking for valid config file...")
	
	exists = os.path.isfile(ProgLoc+"/PyTgen/configs/"+SysHostname+".py")
	
	if exists:
		print("Validation complete")
	else:
		os.chdir(ProgLoc+"/PyTgen/configs/")
		os.system("touch "+SysHostname+".py")
		os.chdir(ProgLoc)

#Introduction
print("====================================")
print("Normal Traffic Generator")
print("Created by Normal Traffic Team")
print("====================================")

#Make program get its current location
ProgLoc = os.getcwd()

#Make program get Hostname
SysHostname = socket.gethostname()

#Config Var
ConfigFile = ProgLoc+"/PyTgen/configs/"+SysHostname+".py"

#While True, keep in loop
while True:

	#Select whether choose Self Generate or Replay

	print("\n\n")
	print("Select an option to begin with")
	print("1. Self Generated Traffic")	#Will change name
	print("2. Use Scapy")			#Will change name
	print("3. Exit")
	#Input to read INT and Raw_Input to read STR
	startoption = raw_input("Please choose a number (1-3) => ")
	
	#Validation

	#Self Generate Traffic
	if startoption == "1":
		
		hardcoded_file()
		#Run the checks for Hostname.py
		print("\n")
		check_hostnameconfigs()
		
		while True:
			print("\n\n")
			print("====================================")
			print("Welcome to SELF GENERATED TRAFFIC")
			print("====================================")
			print("\n\n")
			print("Protocols:")
			print("1. TCP")
			print("2. UDP")
			
			protocolchoosen = raw_input("Choose a traffic protocol => ")
			
			if protocolchoosen == "1":
				while True:
					print("\n\n")
					print("====================================")
					print("Welcome to SELF GENERATED TRAFFIC")
					print("====================================")
					print("\n\n")
					print("What kind of traffic would you like to generate?")
					print("1. HTTP")
					print("2. FTP")
					print("3. SSH")
					print("4. ICMP")
					print("5. Exit")
					trafficchosen= input("Please choose a number (1-5) => ")
				
					#Going to Options
					#HTTP Traffic
					if trafficchosen == 1:
						print("------------------------------------")
						
						httpStHr = raw_input("State A Starting Hour (00-24) => ")
						httpStMin = raw_input("State A Starting Minute (00-59) => ")
						httpEdHr = raw_input("State A Ending Hour (00-24) => ")
						httpEdMin = raw_input("State A Ending Minute (00-59) => ")
						httpURL = raw_input("URL (Default: https://google.com) => ")
						httpCount = raw_input("How Many HTTP Packets Should Be Sent => ")
						
						if httpStHr == "":
							httpStHr = "00"
						if httpStMin == "":
							httpStMin = "01"
						if httpEdHr == "":
							httpEdHr = "23"
						if httpEdMin == "":
							httpEdMin = "59"
						if httpURL == "":
							httpURL = "https://www.google.com"
						
						
						#Writing into file
						file = open(ConfigFile,"a")
						file.write("\t('http_gen', [("+httpStHr+","+httpStMin+"), ("+httpEdHr+","+httpEdMin+"), (5, 5)], [['"+httpURL+"'],"+httpCount+"])")
						file.close()
						
						add_more()

					#FTP Traffic
					elif trafficchosen == 2:
						print("------------------------------------")
						
						ftpStHr = raw_input("State A Starting Hour (00-24) => ")
						ftpStMin = raw_input("State A Starting Minute (00-59) => ")
						ftpEdHr = raw_input("State A Ending Hour (00-24) => ")
						ftpEdMin = raw_input("State A Ending Minute (00-59) => ")
						ftpHost = raw_input("Target Address => ")
						ftpUser = raw_input("Key In FTP Username => ")
						ftpPass = raw_input("Key In FTP Password => ")
						ftpCount = raw_input("How Many FTP Packets Should Be Sent => ")
						ftpSSL = raw_input("Connect via SSL? (y/n) => ")
						
						if ftpSSL == "y":
							ftpSSL = "True"
						else:
							ftpSSL = "False"
							
						if ftpStHr == "":
							ftpStHr = "00"
						if ftpStMin == "":
							ftpStMin = "01"
						if ftpEdHr == "":
							ftpEdHr = "23"
						if ftpEdMin == "":
							ftpEdMin = "59"
						
						#Writing into file
						file = open(ConfigFile,"a")
						file.write("\t('ftp_gen', [("+ftpStHr+","+ftpStMin+"), ("+ftpEdHr+","+ftpEdMin+"), (5, 5)], ['"+ftpHost+"', '"+ftpUser+"', '"+ftpPass+"', ftp_put, ftp_get, "+ftpCount+", "+ftpSSL+"])")
						file.close()
						
						add_more()
						
						

					#SSH Traffic
					elif trafficchosen == 3:
						print("------------------------------------")
						sshStHr = raw_input("State A Starting Hour (00-24) => ")
						sshStMin = raw_input("State A Starting Minute (00-59) => ")
						sshEdHr = raw_input("State A Ending Hour (00-24) => ")
						sshEdMin = raw_input("State A Ending Minute (00-59) => ")
						sshHost = raw_input("Target Address => ")
						sshUser = raw_input("Key In SSH Username => ")
						sshPass = raw_input("Key In SSH Password => ")
						sshPort = raw_input("Specify Port Number To Be Used => ")
						sshMin = raw_input("Duration Of The Connection Staying Alive (In Minutes) => ")
						
						if sshStHr == "":
							sshStHr = "00"
						if sshStMin == "":
							sshStMin = "01"
						if sshEdHr == "":
							sshEdHr = "23"
						if sshEdMin == "":
							sshEdMin = "59"
						
						#Writing into file
						file = open(ConfigFile,"a")
						file.write("\t('ssh_gen', [("+sshStHr+","+sshStMin+"), ("+sshEdHr+","+sshEdMin+"), (5, 5)], ['"+sshHost+"', "+sshPort+",'"+sshUser+"', '"+sshPass+"', "+sshMin+", ssh_commands])")
						file.close()
						
						add_more()
						
					#ICMP Traffic
					elif trafficchosen == 4:
						print("------------------------------------")
						#Variables for configs py
						icmpStHr = raw_input("State A Starting Hour (00-24) => ")
						icmpStMin = raw_input("State A Starting Minute (00-59) => ")
						icmpEdHr = raw_input("State A Ending Hour (00-24) => ")
						icmpEdMin = raw_input("State A Ending Minute (00-59) => ")
						icmpIp = raw_input("Target Address => ")
						icmpCount = raw_input("How Many ICMP Packets Should Be Sent => ")
						
						if icmpStHr == "":
							icmpStHr = "00"
						if icmpStMin == "":
							icmpStMin = "01"
						if icmpEdHr == "":
							icmpEdHr = "23"
						if icmpEdMin == "":
							icmpEdMin = "59"
						
						#Writing into file
						file = open(ConfigFile,"a")
						file.write("\t('ping_gen', [("+icmpStHr+","+icmpStMin+"), ("+icmpEdHr+","+icmpEdMin+"), (5, 0)], ['"+icmpIp+"', "+icmpCount+"])")
						file.close()
						
						add_more()

					#Exit Option
					elif trafficchosen == 5:
						print("------------------------------------")
						print("Thank you for using this program :)")
						sys.exit()

					#Wrong Option
					else:
						print("------------------------------------")
						print("\nInvalid Option")
						
			elif protocolchoosen == "2":
				#UDP Option
				print("------------------------------------")
				udpAdd = raw_input("Key in the desired IP address => ")
				udpCount = raw_input("Rounds of UDP to be generated => ")
				udpPort = raw_input("Key in UDP Port number => ")
				udpDataLength = raw_input ("Key in Data Length for UDP => ")

				#print("Deploying Traffic")
				os.system("nping -c "+udpCount+" --udp -p "+udpPort+" --data-length "+udpDataLength+" "+udpAdd)
				
			else:
				print("Invalid Option")
		


	#Replay Traffic
	elif startoption == "2":
		#print("\nYou have choosen Option 2")
		print("====================================")
		print("Welcome to TRAFFIC REPLAY")
		print("====================================")
		print("\n\n")
		from scapy.all import *
		from scapy.utils import rdpcap
		import sys
		import subprocess

		filename = raw_input('Enter the name of the pcap file to modify => ')
		#can look into if file exist if
		criteria = raw_input('Enter the criteria Source Ip => ')
		srcip = raw_input('Enter the Source IP to change to => ')
		dstip = raw_input('Enter the Destination IP to change to => ')
		newtime = int(raw_input('Enter the new time in epoch time to change to => '))
		newfile = raw_input('New file name => ')
		pkts=rdpcap(filename)
		pktdump = PcapWriter(newfile, append=True, sync=True)
		for pkt in pkts:
			if pkt[IP].src==criteria:
				pkt.time=newtime
				pkt[IP].src= new_src_ip=srcip
				pkt[IP].dst= new_src_ip=dstip
				pktdump.write(pkt)
			else:
				pktdump.write(pkt)
		print("\n----------------Pcap Replay is Starting------------------")
		loop = raw_input('Enter the number of time you wish to loop the tcpreplay => ')

		subprocess.call('tcprewrite --mtu-trunc --infile='+newfile+' --outfile=output2.pcap', shell=True)
		subprocess.call(['tcpreplay -i eth0 --loop  ' +loop + ' output2.pcap'],shell=True)
		subprocess.call('rm output2.pcap', shell=True)
		subprocess.call('rm '+newfile, shell=True)
		print("------------------------------------")
		print("Program has ended its replay...Exiting")
		pktdump.close()
		sys.exit()
	
	#Exit
	elif startoption == "3":
		print("------------------------------------")
		print("Thank you for using this program :)")
		sys.exit()

	else:
		print("\nOption " + str(startoption) + " is not a valid number. ")
