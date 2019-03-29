> https://danielmiessler.com/study/tcpdump/

```
ERROR like: tcpdump: Couldn't find user 'tcpdump'
-> reinstall tcpdump  OR  use -Z
```

## host
```
tcpdump host $HOST
tcpdump src $HOST
tcpdump dst $HOST
tcpdump net $HOST_AREA  #1.2.3.0/24
```

## port
```
tcpdump port $PORT
tcpdump portrange $PORT1-$PORT2
```

## protocol
```
tcpdump (tcp|udp|icmp|...)
```

## packet size
```
tcpdump less 32 
tcpdump greater 64 
tcpdump <= 128
```

## r/w file
```
tcpdump [condition] -w $capture_file
tcpdump -r $capture_file
```

## params
```
-i eth0 : Listen on the eth0 interface.
-vv : Verbose output (more v’s gives more output).
-X  : Show the packet’s contents in both hex and ascii.
-XX : Same as -X, but also shows the ethernet header.
-n  : Don't convert host addresses to names.  This can be used to avoid DNS lookups.
-nn : Don't convert protocol and port numbers etc. to names either.
-Z  : user. default: tcpdump

-D : Show the list of available interfaces
-l : Line-readable output (for viewing as you save, or sending to other commands)
-q : Be less verbose (more quiet) with your output.
-t : Give human-readable timestamp output.
-tttt : Give maximally human-readable timestamp output.
-c : Only get x number of packets and then stop.
-s : Define the snaplength (size) of the capture in bytes. Use -s0 to get everything, unless you are intentionally capturing less.
-S : Print absolute sequence numbers.
-e : Get the ethernet header as well.
-q : Show less protocol information.
-E : Decrypt IPSEC traffic by providing an encryption key.
```
