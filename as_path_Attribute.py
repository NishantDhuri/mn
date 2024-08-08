# Practical: Use the AS_PATH Attribute in a Three-Router Topology
# The AS_PATH attribute is used in BGP (Border Gateway Protocol) to influence the path selection process. We'll set up a BGP configuration with three routers and manipulate the AS_PATH attribute to control the route preferences.

# Step 1: Setting Up the Network in GNS3
# Open GNS3 and create a new project.
# Add three routers (R1, R2, R3) and connect them as follows:
# R1 to R2 (using interface Serial0/0 on R1 and R2)
# R2 to R3 (using interface Serial0/1 on R2 and interface Serial0/0 on R3)
# R1 to R3 (using interface Serial0/1 on R1 and interface Serial0/1 on R3)

# Step 2: Configuring the Routers
# Configure IP addresses on each router:

# Router 1 (R1):
#configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 192.168.12.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit
# R1(config)# interface Serial0/1
# R1(config-if)# ip address 192.168.13.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Router 2 (R2):
# R2(config)# interface Serial0/0
# R2(config-if)# ip address 192.168.12.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit
# R2(config)# interface Serial0/1
# R2(config-if)# ip address 192.168.23.1 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Router 3 (R3):
# R3(config)# interface Serial0/0
# R3(config-if)# ip address 192.168.23.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit
# R3(config)# interface Serial0/1
# R3(config-if)# ip address 192.168.13.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# Step 3: Configuring BGP on Each Router

# Configure BGP on Router 1 (R1):
# R1(config)# router bgp 65001
# R1(config-router)# neighbor 192.168.12.2 remote-as 65002
# R1(config-router)# neighbor 192.168.13.2 remote-as 65003
# R1(config-router)# network 10.1.1.0 mask 255.255.255.0
# R1(config-router)# exit

# Configure BGP on Router 2 (R2):
# R2(config)# router bgp 65002
# R2(config-router)# neighbor 192.168.12.1 remote-as 65001
# R2(config-router)# neighbor 192.168.23.2 remote-as 65003
# R2(config-router)# network 20.1.1.0 mask 255.255.255.0
# R2(config-router)# exit

# Configure BGP on Router 3 (R3):
# R3(config)# router bgp 65003
# R3(config-router)# neighbor 192.168.13.1 remote-as 65001
# R3(config-router)# neighbor 192.168.23.1 remote-as 65002
# R3(config-router)# network 30.1.1.0 mask 255.255.255.0
# R3(config-router)# exit

# Step 4: Manipulating the AS_PATH Attribute

# On Router 2 (R2), create a route-map to prepend the AS path:
# R2(config)# route-map PREPEND-AS permit 10
# R2(config-route-map)# set as-path prepend 65002 65002
# R2(config-route-map)# exit

# Apply the route-map to the neighbor relationship on R2:
# R2(config)# router bgp 65002
# R2(config-router)# neighbor 192.168.12.1 route-map PREPEND-AS out
# R2(config-router)# exit

# Step 5: Verifying the Configuration

# Check the BGP table on Router 1 (R1) to verify the AS_PATH:
# R1# show ip bgp

# Verify the BGP routes on Router 3 (R3):
# R3# show ip bgp  