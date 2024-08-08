# Practical 3: Configuring iBGP and eBGP Sessions, Local Preference, and MED

# Step 1: Setting Up the Network in GNS3

# Open GNS3 and create a new project.

# Add three routers (R1, R2, and R3) and connect them as follows:
# R1 to R2 (using serial interfaces: Serial0/0 on R1 and Serial0/0 on R2)
# R2 to R3 (using serial interfaces: Serial0/1 on R2 and Serial0/0 on R3)
# R3 to R1 (using serial interfaces: Serial0/1 on R3 and Serial0/1 on R1)

# Step 2: Configuring the Routers

# R1 Configuration:
# Access the CLI of Router 1 (R1):
# gns3> connect R1

# Configure the interfaces on R1:
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 192.168.12.1 255.255.255.252
# R1(config-if)# clock rate 64000
# R1(config-if)# no shutdown
# R1(config-if)# exit

# R1(config)# interface Serial0/1
# R1(config-if)# ip address 192.168.13.1 255.255.255.252
# R1(config-if)# clock rate 64000
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Configure BGP on R1:
# R1(config)# router bgp 100
# R1(config-router)# neighbor 192.168.12.2 remote-as 200
# R1(config-router)# neighbor 192.168.13.2 remote-as 300
# R1(config-router)# network 192.168.12.0 mask 255.255.255.252
# R1(config-router)# network 192.168.13.0 mask 255.255.255.252
# R1(config-router)# exit

# R2 Configuration:

# Access the CLI of Router 2 (R2):
# gns3> connect R2

# Configure the interfaces on R2:
# R2(config)# interface Serial0/0
# R2(config-if)# ip address 192.168.12.2 255.255.255.252
# R2(config-if)# no shutdown
# R2(config-if)# exit

# R2(config)# interface Serial0/1
# R2(config-if)# ip address 192.168.23.1 255.255.255.252
# R2(config-if)# clock rate 64000
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Configure BGP on R2:
# R2(config)# router bgp 200
# R2(config-router)# neighbor 192.168.12.1 remote-as 100
# R2(config-router)# neighbor 192.168.23.2 remote-as 300
# R2(config-router)# network 192.168.12.0 mask 255.255.255.252
# R2(config-router)# network 192.168.23.0 mask 255.255.255.252
# R2(config-router)# exit

# R3 Configuration:

# Access the CLI of Router 3 (R3):
# gns3> connect R3

# Configure the interfaces on R3:
# R3(config)# interface Serial0/0
# R3(config-if)# ip address 192.168.23.2 255.255.255.252
# R3(config-if)# no shutdown
# R3(config-if)# exit

# R3(config)# interface Serial0/1
# R3(config-if)# ip address 192.168.13.2 255.255.255.252
# R3(config-if)# no shutdown
# R3(config-if)# exit

# Configure BGP on R3:
# R3(config)# router bgp 300
# R3(config-router)# neighbor 192.168.13.1 remote-as 100
# R3(config-router)# neighbor 192.168.23.1 remote-as 200
# R3(config-router)# network 192.168.13.0 mask 255.255.255.252
# R3(config-router)# network 192.168.23.0 mask 255.255.255.252
# R3(config-router)# exit

# Step 3: Configuring iBGP and eBGP Sessions

# R1 Configuration:

# Configure iBGP with R3:
# R1(config)# router bgp 100
# R1(config-router)# neighbor 192.168.13.2 remote-as 100
# R1(config-router)# exit

# R3 Configuration:

# Configure iBGP with R1:
# R3(config)# router bgp 300
# R3(config-router)# neighbor 192.168.13.1 remote-as 300
# R3(config-router)# exit

# Step 4: Configuring Local Preference

# R1 Configuration:

# Set local preference for routes learned from R2:
# R1(config)# route-map SET_LOCAL_PREF permit 10
# R1(config-route-map)# set local-preference 200
# R1(config-route-map)# exit
# R1(config)# router bgp 100
# R1(config-router)# neighbor 192.168.12.2 route-map SET_LOCAL_PREF in
# R1(config-router)# exit

# Step 5: Configuring MED

# R2 Configuration:

# Set MED for routes advertised to R3:
# R2(config)# route-map SET_MED permit 10
# R2(config-route-map)# set metric 50
# R2(config-route-map)# exit
# R2(config)# router bgp 200
# R2(config-router)# neighbor 192.168.23.2 route-map SET_MED out
# R2(config-router)# exit

# Step 6: Verifying the Configuration

# Verify BGP sessions:
# R1# show ip bgp summary
# R2# show ip bgp summary
# R3# show ip bgp summary

# Verify Local Preference:
# R1# show ip bgp

# Verify MED:
# R3# show ip bgp