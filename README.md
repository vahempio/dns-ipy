# DNS-IPy

## Short brief
This is a tiny DNS demonstrator to dynamicaly respond from a A query to an IP address.

Usage example:
```sh
$ python3 ./dns-ipy.py &
$ nslookup -port=5053 1-2-3-4.foo.bar 127.0.0.1
```
And the answer will be: 1.2.3.4

## Long brief
This DNSserver will parse your A request, and create an answer with the IP address contained inside the request. This is the process used by Plesk to convert an URL into a local IP: useful to use a valid https certificate on a local server.

The valid format of the request is the following:
- A-B-C-D.subdomain.domain.tld (where A,B,C,D are [0:255] digits of the IPv4 address)
- request type A
The answer will be: A.B.C.D

Launch the python script to start a DNSserver on the 5053 port (UDP+TCP) and query the server with:
```sh
$ nslookup -port=5053 -type=A 1-2-3-4.foo.bar 127.0.0.1
Server:		127.0.0.1
Address:	127.0.0.1#5053

Name:	1-2-3-4.foo.bar
Address: 1.2.3.4
```

## Docker
Start with:
```sh
docker run -it -p 5053:5053/udp vahempio/dns-ipy
```

## Docker-compose
docker-compose.yml example:
```sh
version: "2"

services:
  dns-ipy:
    image: vahempio/dns-ipy
    restart: on-failure
    ports:
      - "53:5053/tcp"
      - "53:5053/udp"

    # For logs:
    stdin_open: true
    tty: true
```

