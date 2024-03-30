import hid
from http.server import BaseHTTPRequestHandler, HTTPServer

h = hid.device()
h.open(0x0079, 0x0006)  # TREZOR VendorID/ProductID
data = "00000000,00000000"
class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		
		try:
			d = h.read(64)
			if d:
				print(d)
				mystring = ""
				for digit in d:
					mystring += str('{0:08b}'.format(digit))
					mystring += ","
				mystring = mystring[:-1]
				print(mystring)
				data = mystring
		except IOError as ex:
			print(ex)
			print("You probably don't have the hard-coded device.")
			print("Update the h.open() line in this script with the one")
			print("from the enumeration list output above and try again.")

		self.send_response(200)
		#self.send_header('Content-type','text/html')
		#self.end_headers
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', '*')
		self.send_header('Access-Control-Allow-Headers', '*')
		self.end_headers()
		self.wfile.write(data.encode('utf-8'))
		print("requested!")

httpd = HTTPServer(("localhost",7777),MyServer)

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
h.close()
httpd.server_close()
#
#for device_dict in hid.enumerate():
#    keys = list(device_dict.keys())
#    keys.sort()
#    for key in keys:
#        print("%s : %s" % (key, device_dict[key]))
#    print()

print("Done")
