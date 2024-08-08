# Practical: Simulating VRF with 6 Routers

# # Network Setup:
# Router 1 (R1) and Router 2 (R2): VRF-A and VRF-B (PE Routers)
# Router 3 (R3) and Router 4 (R4): VRF-A and VRF-B (PE Routers)
# Router 5 (R5) and Router 6 (R6): MPLS Core Routers

# Objective:
# Configure VRFs on the PE routers.
# Configure MPLS on the Core routers.
# Establish VRF connectivity between PE routers through MPLS.

# Configuration Steps

# Step 1: Set Up the Network

# 1.1 Configure Router Interfaces:

# Router 1 (R1):
# R1# configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 10.1.1.1 255.255.255.252
# R1(config-if)# clock rate 64000
# R1(config-if)# no shutdown
# R1(config-if)# exit

# R1(config)# interface FastEthernet0/0
# R1(config-if)# ip address 10.1.2.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# R1(config)# interface FastEthernet0/1
# R1(config-if)# ip address 10.1.3.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Router 2 (R2):
# R2# configure terminal
# R2(config)# interface Serial0/0
# R2(config-if)# ip address 10.1.1.2 255.255.255.252
# R2(config-if)# no shutdown
# R2(config-if)# exit

# R2(config)# interface FastEthernet0/0
# R2(config-if)# ip address 10.1.4.1 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# R2(config)# interface FastEthernet0/1
# R2(config-if)# ip address 10.1.5.1 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Router 3 (R3):
# R3# configure terminal
# R3(config)# interface FastEthernet0/0
# R3(config-if)# ip address 10.1.2.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# R3(config)# interface FastEthernet0/1
# R3(config-if)# ip address 10.1.6.1 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# Router 4 (R4):
# R4# configure terminal
# R4(config)# interface FastEthernet0/0
# R4(config-if)# ip address 10.1.3.2 255.255.255.0
# R4(config-if)# no shutdown
# R4(config)# interface FastEthernet0/1
# R4(config-if)# ip address 10.1.7.1 255.255.255.0
# R4(config-if)# no shutdown
# R4(config)# exit

# Router 5 (R5):
# R5# configure terminal
# R5(config)# interface FastEthernet0/0
# R5(config-if)# ip address 10.1.4.2 255.255.255.0
# R5(config-if)# no shutdown
# R5(config)# exit

# Router 6 (R6):
# R6# configure terminal
# R6(config)# interface FastEthernet0/0
# R6(config-if)# ip address 10.1.5.2 255.255.255.0
# R6(config-if)# no shutdown
# R6(config)# exit

# Step 2: Configure MPLS on Core Routers

# On Router 5 (R5):

# Enable MPLS on Interfaces:
# R5# configure terminal
# R5(config)# interface FastEthernet0/0
# R5(config-if)# mpls ip
# R5(config-if)# exit
# R5(config)# mpls label protocol ldp
# R5(config)# exit

# On Router 6 (R6):

# Enable MPLS on Interfaces:
# R6# configure terminal
# R6(config)# interface FastEthernet0/0
# R6(config-if)# mpls ip
# R6(config-if)# exit
# R6(config)# mpls label protocol ldp
# R6(config)# exit
# Step 3: Configure VRF on PE Routers

# On Router 1 (R1):

# Define VRFs:
# R1# configure terminal
# R1(config)# ip vrf VRF-A
# R1(config-vrf)# rd 100:1
# R1(config-vrf)# exit
# R1(config)# ip vrf VRF-B
# R1(config-vrf)# rd 100:2
# R1(config-vrf)# exit

# Assign Interfaces to VRFs:
# R1# configure terminal
# R1(config)# interface FastEthernet0/0
# R1(config-if)# ip vrf forwarding VRF-A
# R1(config-if)# ip address 192.168.1.1 255.255.255.0
# R1(config-if)# exit

# R1(config)# interface FastEthernet0/1
# R1(config-if)# ip vrf forwarding VRF-B
# R1(config-if)# ip address 192.168.2.1 255.255.255.0
# R1(config-if)# exit

# On Router 2 (R2):

# Define VRFs:
# R2# configure terminal
# R2(config)# ip vrf VRF-A
# R2(config-vrf)# rd 200:1
# R2(config-vrf)# exit
# R2(config)# ip vrf VRF-B
# R2(config-vrf)# rd 200:2
# R2(config-vrf)# exit

# Assign Interfaces to VRFs:
# R2# configure terminal
# R2(config)# interface FastEthernet0/1
# R2(config-if)# ip vrf forwarding VRF-A
# R2(config-if)# ip address 192.168.3.1 255.255.255.0
# R2(config-if)# exit

# R2(config)# interface FastEthernet0/0
# R2(config-if)# ip vrf forwarding VRF-B
# R2(config-if)# ip address 192.168.4.1 255.255.255.0
# R2(config-if)# exit

# On Router 3 (R3):

# Define VRFs:
# R3# configure terminal
# R3(config)# ip vrf VRF-A
# R3(config-vrf)# rd 300:1
# R3(config-vrf)# exit
# R3(config)# ip vrf VRF-B
# R3(config-vrf)# rd 300:2
# R3(config-vrf)# exit

# Assign Interfaces to VRFs:
# R3# configure terminal
# R3(config)# interface FastEthernet0/0
# R3(config-if)# ip vrf forwarding VRF-A
# R3(config-if)# ip address 192.168.5.1 255.255.255.0
# R3(config-if)# exit

# R3(config)# interface FastEthernet0/1
# R3(config-if)# ip vrf forwarding VRF-B
# R3(config-if)# ip address 192.168.6.1 255.255.255.0
# R3(config-if)# exit

# On Router 4 (R4):

# Define VRFs:
# R4# configure terminal
# R4(config)# ip vrf VRF-A
# R4(config-vrf)# rd 400:1
# R4(config-vrf)# exit
# R4(config)# ip vrf VRF-B
# R4(config-vrf)# rd 400:2
# R4(config-vrf)# exit

# Assign Interfaces to VRFs:
# R4# configure terminal
# R4(config)# interface FastEthernet0/0
# R4(config-if)# ip vrf forwarding VRF-A
# R4(config-if)# ip address 192.168.7.1 255.255.255.0
# R4(config-if)# exit

# R4(config)# interface FastEthernet0/1
# R4(config-if)# ip vrf forwarding VRF-B
# R4(config-if)# ip address 192.168.8.1 255.255.255.0
# R4(config-if)# exit

# Step 4: Configure Routing

# On Router 1 (R1):

# Configure BGP for VRF-A and VRF-B:
# R1# configure terminal
# R1(config)# router bgp 100
# R1(config-router)# address-family ipv4 vrf VRF-A
# R1(config-router-af)# neighbor 10.1.1.2 remote-as 200
# R1(config-router-af)# network 192.168.1.0 mask 255.255.255.0
# R1(config-router-af)# exit
# R1(config-router)# address-family ipv4 vrf VRF-B
# R1(config-router-af)# neighbor 10.1.1.2 remote-as 200
# R1(config-router-af)# network 192.168.2.0 mask 255.255.255.0
# R1(config-router-af)# exit

# On Router 2 (R2):

# Configure BGP for VRF-A and VRF-B:
# R2# configure terminal
# R2(config)# router bgp 200
# R2(config-router)# address-family ipv4 vrf VRF-A
# R2(config-router-af)# neighbor 10.1.1.1 remote-as 100
# R2(config-router-af)# network 192.168.3.0 mask 255.255.255.0
# R2(config-router-af)# exit
# R2(config-router)# address-family ipv4 vrf VRF-B
# R2(config-router-af)# neighbor 10.1.1.1 remote-as 100
# R2(config-router-af)# network 192.168.4.0 mask 255.255.255.0
# R2(config-router-af)# exit

# On Router 3 (R3):

# Configure BGP for VRF-A and VRF-B:
# R3# configure terminal
# R3(config)# router bgp 300
# R3(config-router)# address-family ipv4 vrf VRF-A
# R3(config-router-af)# neighbor 10.1.2.1 remote-as 100
# R3(config-router-af)# network 192.168.5.0 mask 255.255.255.0
# R3(config-router-af)# exit
# R3(config-router)# address-family ipv4 vrf VRF-B
# R3(config-router-af)# neighbor 10.1.2.1 remote-as 100
# R3(config-router-af)# network 192.168.6.0 mask 255.255.255.0
# R3(config-router-af)# exit

# On Router 4 (R4):

# Configure BGP for VRF-A and VRF-B:
# R4# configure terminal
# R4(config)# router bgp 400
# R4(config-router)# address-family ipv4 vrf VRF-A
# R4(config-router-af)# neighbor 10.1.3.1 remote-as 100
# R4(config-router-af)# network 192.168.7.0 mask 255.255.255.0
# R4(config-router-af)# exit
# R4(config-router)# address-family ipv4 vrf VRF-B
# R4(config-router-af)# neighbor 10.1.3.1 remote-as 100
# R4(config-router-af)# network 192.168.8.0 mask 255.255.255.0
# R4(config-router-af)# exit

# Step 5: Verify the Configuration

# Check VRF Configuration and Routing:

# On Router 1 (R1):
# R1# show ip vrf
# R1# show ip route vrf VRF-A
# R1# show ip route vrf VRF-B

# On Router 2 (R2):
# R2# show ip vrf
# R2# show ip route vrf VRF-A
# R2# show ip route vrf VRF-B

# On Router 3 (R3):
# R3# show ip vrf
# R3# show ip route vrf VRF-A
# R3# show ip route vrf VRF-B

# On Router 4 (R4):
# R4# show ip vrf
# R4# show ip route vrf VRF-A
# R4# show ip route vrf VRF-B

# Ping Tests:

# From Router 1 (R1), ping an address in VRF-A on Router 3 (R3) and VRF-B on Router 4 (R4).

# From Router 2 (R2), ping an address in VRF-A on Router 4 (R4) and VRF-B on Router 3 (R3).