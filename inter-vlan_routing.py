# Practical 7: Inter-VLAN Routing
# Objective: Configure inter-VLAN routing to enable communication between devices on different VLANs.

# Network Setup:

# Router 1 (R1) (Router for inter-VLAN routing)
# Switch 1 (SW1) (Switch with multiple VLANs)
# Switch 2 (SW2) (Additional switch, if needed)

# VLAN Configuration:

# VLAN 10: 192.168.10.0/24
# VLAN 20: 192.168.20.0/24

# Configuration Steps

# Step 1: Configure VLANs on the Switch

# On Switch 1 (SW1):

# Define VLANs:
# SW1# configure terminal
# SW1(config)# vlan 10
# SW1(config-vlan)# name VLAN10
# SW1(config-vlan)# exit
# SW1(config)# vlan 20
# SW1(config-vlan)# name VLAN20
# SW1(config-vlan)# exit

# Assign VLANs to Interfaces:
# SW1# configure terminal
# SW1(config)# interface 8hernet0/1
# SW1(config-if)# switchport mode access
# SW1(config-if)# switchport access vlan 10
# SW1(config-if)# exit
# SW1(config)# interface FastEthernet0/2
# SW1(config-if)# switchport mode access
# SW1(config-if)# switchport access vlan 20
# SW1(config-if)# exit

# Configure Trunk Port:

# If the router is connected to SW1 via a trunk port:

# SW1# configure terminal
# SW1(config)# interface FastEthernet0/24
# SW1(config-if)# switchport mode trunk
# SW1(config-if)# switchport trunk allowed vlan 10,20
# SW1(config-if)# exit

# Step 2: Configure Router for Inter-VLAN Routing

# On Router 1 (R1):
# Configure Sub-Interfaces for Each VLAN:
# R1# configure terminal
# R1(config)# interface GigabitEthernet0/0.10
# R1(config-if)# encapsulation dot1Q 10
# R1(config-if)# ip address 192.168.10.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# R1(config)# interface GigabitEthernet0/0.20
# R1(config-if)# encapsulation dot1Q 20
# R1(config-if)# ip address 192.168.20.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Note: Adjust the interface name (GigabitEthernet0/0) as needed based on your actual router’s interface.

# Configure Routing:
# If you are using static routing:
# R1(config)# ip route 192.168.10.0 255.255.255.0 Null0
# R1(config)# ip route 192.168.20.0 255.255.255.0 Null0

# For dynamic routing protocols, configure as needed.

# Step 3: Configure IP Addresses on Devices

# On Hosts in VLAN 10:
# Set IP Address:
# Host1> ip 192.168.10.2 255.255.255.0 192.168.10.1

# On Hosts in VLAN 20:
# Set IP Address:
# Host2> ip 192.168.20.2 255.255.255.0 192.168.20.1

# Step 4: Verify Inter-VLAN Routing

# Verify VLAN Configuration on Switch 1:
# SW1# show vlan brief

# Verify Router Configuration:
# R1# show ip interface brief
# R1# show running-config interface GigabitEthernet0/0.10
# R1# show running-config interface GigabitEthernet0/0.20

# Verify Connectivity Between VLANs:

# From a host in VLAN 10, ping a host in VLAN 20
# Host1> ping 192.168.20.2

# From a host in VLAN 20, ping a host in VLAN 10:
# Host2> ping 192.168.10.2
