from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections                                                                   
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCIntf, TCLink
from mininet.log import setLogLevel
import os                                                               

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self, switch_number, host_number ):
        Topo.__init__( self )
        swi = {}
        hos = {}
        switch_number = int(switch_number)
        host_number = int(host_number)
        for x in range(switch_number):
            s = self.addSwitch("s" +str(x+1))
            swi[x+1]= s
        for x in range(host_number):
            h = self.addHost("h" +str(x+1))
            hos[x+1]= h
        for x in range(switch_number):
            for y in range(x):
                self.addLink(swi[x+1],swi[y+1])    
        sph = host_number/switch_number
        sin = swi.keys()
        skey = sin*int(host_number/switch_number)
        tmp = sin[:(host_number%switch_number)]
        skey = skey + tmp
        skey.sort()
        i = 0
        for x in skey:
            self.addLink(swi[x], hos[i+1],bw=((i%2)+1))
            i = i+1

def testTopo(switch_number,host_number):
    topo = MyTopo(switch_number, host_number)
    net = Mininet(topo, link=TCLink, controller=RemoteController)
    net.start()
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6633)
    for x in range(host_number):
        for y in range(host_number):
            if x%2==0 and y%2==1:
                net.nameToNode["h"+str(x+1)].cmd("iptables -A OUTPUT -o h"+str(x+1)+"-eth0 -d 10.0.0."+ str(y+1)+" -j DROP")
    dumpNodeConnections(net.switches)
    CLI(net)

if __name__ == '__main__':
    switch_number = int(raw_input("number of switches : "))
    host_number = int(raw_input("number of hosts : "))
    topos = { 'mytopo': ( lambda: MyTopo( switch_number, host_number) ) }
    setLogLevel('info')
    testTopo(switch_number, host_number)

