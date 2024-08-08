# Practical: Simulating MPLS Environment with 3 Routers
# Network Setup:

# Router 1 (R1): Provider Edge (PE) Router
# Router 2 (R2): Provider Core Router
# Router 3 (R3): Provider Edge (PE) Router

# Objective:
# Configure MPLS on the routers.
# Set up LDP for label distribution.
# Verify MPLS operations.
# Configuration Steps

# Step 1: Set Up the Network

# 1.1 Configure Router Interfaces:

# Router 1 (R1):
# R1# configure terminal
# R1(config)# interface FastEthernet0/0
# R1(config-if)# ip address 10.1.1.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit
# R1(config)# interface FastEthernet0/1
# R1(config-if)# ip address 10.1.2.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Router 2 (R2):
# R2# configure terminal
# R2(config)# interface FastEthernet0/0
# R2(config-if)# ip address 10.1.1.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit
# R2(config)# interface FastEthernet0/1
# R2(config-if)# ip address 10.1.3.1 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Router 3 (R3):
# R3# configure terminal
# R3(config)# interface FastEthernet0/0
# R3(config-if)# ip address 10.1.3.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit
# R3(config)# interface FastEthernet0/1
# R3(config-if)# ip address 10.1.2.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config)# exit

# Step 2: Configure MPLS

# On Router 1 (R1):

# Enable MPLS on Interfaces:
# R1# configure terminal
# R1(config)# interface FastEthernet0/0
# R1(config-if)# mpls ip
# R1(config-if)# exit
# R1(config)# interface FastEthernet0/1
# R1(config-if)# mpls ip
# R1(config-if)# exit

# Enable MPLS LDP:
# R1# configure terminal
# R1(config)# mpls label protocol ldp
# R1(config)# exit

# On Router 2 (R2):

# Enable MPLS on Interfaces:
# R2# configure terminal
# R2(config)# interface FastEthernet0/0
# R2(config-if)# mpls ip
# R2(config-if)# exit
# R2(config)# interface FastEthernet0/1
# R2(config-if)# mpls ip
# R2(config-if)# exit

# Enable MPLS LDP:
# R2# configure terminal
# R2(config)# mpls label protocol ldp
# R2(config)# exit

# On Router 3 (R3):

# Enable MPLS on Interfaces:
# R3# configure terminal
# R3(config)# interface FastEthernet0/0
# R3(config-if)# mpls ip
# R3(config-if)# exit
# R3(config)# interface FastEthernet0/1
# R3(config-if)# mpls ip
# R3(config-if)# exit

# Enable MPLS LDP:
# R3# configure terminal
# R3(config)# mpls label protocol ldp
# R3(config)# exit

# Step 3: Verify MPLS Configuration

# Verify MPLS Label Distribution:

# On Router 1 (R1):
# R1# show mpls ldp neighbor
# R1# show mpls forwarding-table

# On Router 2 (R2):
# R2# show mpls ldp neighbor
# R2# show mpls forwarding-table

# On Router 3 (R3):
# R3# show mpls ldp neighbor
# R3# show mpls forwarding-table

# Verify MPLS Configuration End-to-End:

# From Router 1 (R1), ping a destination address in the MPLS network:
# R1# ping 10.1.3.2

# From Router 3 (R3), ping a destination address in the MPLS network:
# R3# ping 10.1.1.1
