#!/usr/bin/env python3

'''
This is a tiny DNS demonstrator to dynamicaly respond from a A query to an IP address.

Usage example:
    python3 ./dns-ipy.py &
    nslookup -port=5053 -type=A 1.2.3.4.foo.bar 127.0.0.1
    > Address: 1.2.3.4

Author:  Yannick Gaudin
Contact: vahempio@gmail.com
License: MIT
'''

from time import sleep
try:
  from dnslib import A
  from dnslib import QTYPE, RR
  from dnslib.server import DNSServer
except ImportError:
  print("Please install dnslib with \"pip3 install dnslib\"")
  exit(-1)

class Replier:
  def resolve(self, request, handler):
    reply = request.reply()

    # Only answer to type 'A'
    if request.q.qtype != QTYPE.A:
      return reply

    try:
      # Extract the IP addr
      result_ip=str(request.q.qname).split('.')[0].replace('-','.')
      reply.add_answer( RR(request.q.qname, rdata=A(result_ip) ))
    except:
      print("Wrong IP format:"+str(request.q.qname))
      pass

    return reply

replier = Replier()
dns_servers = [
  DNSServer(replier, port=5053, address='0.0.0.0', tcp=True),
  DNSServer(replier, port=5053, address='0.0.0.0', tcp=False),
]

if __name__ == '__main__':
  for s in dns_servers:
    s.start_thread()

  try:
    while True:
      sleep(1)
  except KeyboardInterrupt:
    pass
  finally:
    for s in dns_servers:
      s.stop()
