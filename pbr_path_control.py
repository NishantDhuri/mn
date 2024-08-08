# Practical 5: Configure and Verify Path Control Using PBR
# Network Setup:

# R1 to R2 (Fa0/0 on both routers)
# R2 to R3 (Fa0/1 on both routers)
# R1 to R3 (Fa0/1 on R1 and Fa0/0 on R3)

# Configuration Steps

# Step 1: Set Up Interfaces

# Router 1 (R1):
# R1# configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 192.168.12.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit
# R1(config)# interface Serial0/1
# R1(config-if)# ip address 192.168.13.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Router 2 (R2):
# R2# configure terminal
# R2(config)# interface Serial0/0
# R2(config-if)# ip address 192.168.12.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit
# R2(config)# interface Serial0/1
# R2(config-if)# ip address 192.168.23.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Router 3 (R3):
# R3# configure terminal
# R3(config)# interface Serial0/0
# R3(config-if)# ip address 192.168.23.3 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit
# R3(config)# interface Serial0/1
# R3(config-if)# ip address 192.168.13.3 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# Step 2: Configure Routing

# For simplicity, let's use static routing in this example.

# Router 1 (R1):
# R1# configure terminal
# R1(config)# ip route 192.168.23.0 255.255.255.0 192.168.13.2
# R1(config)# exit

# Router 2 (R2):
# R2# configure terminal
# R2(config)# ip route 192.168.13.0 255.255.255.0 192.168.12.1
# R2(config)# ip route 192.168.23.0 255.255.255.0 192.168.12.1
# R2(config)# exit

# Router 3 (R3):
# R3# configure terminal
# R3(config)# ip route 192.168.12.0 255.255.255.0 192.168.13.2
# R3(config)# exit

# Step 3: Configure Policy-Based Routing (PBR)

# Router 1 (R1):
# Create an Access List:
# R1# configure terminal
# R1(config)# access-list 100 permit 192.168.23.0 0.0.0.255
# R1(config)# exit

# Create a Route Map:
# R1# configure terminal
# R1(config)# route-map PBR-MAP permit 10
# R1(config-route-map)# match ip address 100
# R1(config-route-map)# set ip next-hop 192.168.13.2
# R1(config-route-map)# exit

# Apply the Route Map to the Interface:
# R1# configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip policy route-map PBR-MAP
# R1(config-if)# exit

# Step 4: Verify Configuration
# Verify Policy-Based Routing Configuration on R1:
# R1# show route-map
# R1# show ip policy

# Verify Routing Tables:
# On R2 and R3, check routing tables to ensure routes are being learned properly:
# R2# show ip route
# R3# show ip route

# Verify Traffic Path:

# You can use ping or traceroute from R1 to R3 to ensure that the traffic is following the desired path:
# R1# ping 192.168.23.3
# R1# traceroute 192.168.23.3