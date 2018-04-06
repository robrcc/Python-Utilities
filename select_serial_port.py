# list_serial_ports code from Thomas - https://stackoverflow.com/a/14224477
import sys
import glob
import serial
from checknumbers import *


def list_serial_ports():
	""" Lists serial port names

		:raises EnvironmentError:
			On unsupported or unknown platforms
		:returns:
			A list of the serial ports available on the system
	"""
	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this excludes your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty[A-Za-z]*')
	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')
	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result


# Port selection menu, returns string of port name or empty string
def choose_serial_port():
	
	choice = ""
	
	while choice != "X":
		ports = list_serial_ports()
		
		print("Available serial ports:")
		for x in range(len(ports)):
			print("[%d] %s" % (x, ports[x]))
		print("[X] Exit")
		
		choice = input("Select port: ")
		
		if choice == "x" or choice == "X":
			print("No port chosen.")
			return ""
		elif isInt(choice) and int(choice) in range(len(ports)):
			return ports[int(choice)]
		else:
			print("Invalid choice.")


# Port speed selection menu, returns int of port speed or zero if none
def choose_port_speed():
	speeds = [1200,2400,4800,9600,19200,38400,57600,115200]
	
	choice = ""
	
	while choice != "X":
		print("Available port speeds:")
		for x in range(len(speeds)):
			print("[%d] %d" % (x, speeds[x]))
		print("[X] Exit")
		
		choice = input("Select port [ENTER for 9600]: ")
		
		if choice == "x" or choice == "X":
			print("No speed chosen.")
			return 0
		elif choice == "":
			return 9600
		elif isInt(choice) and int(choice) in range(len(speeds)):
			return speeds[int(choice)]
		else:
			print("Invalid choice.")	
	

def main():
	p = choose_serial_port()
	s = choose_port_speed()
	print("Port:", p)
	print("Speed:", s)


main()