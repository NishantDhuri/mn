# Practical: Configure SLA Tracking and Path Control with Three Routers

# Step 1: Setting Up the Network in GNS3

# Open GNS3 and create a new project.
# Add three routers (R1, R2, R3) and connect them as follows:
# R1 to R2 (using serial interfaces: Serial0/0 on R1 and Serial0/0 on R2)
# R1 to R3 (using serial interfaces: Serial0/1 on R1 and Serial0/0 on R3)

# Step 2: Configuring the Routers

# Access the CLI of Router 1 (R1):
# gns3> connect R1

# Configure the interfaces on R1:
# configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 192.168.1.1 255.255.255.252
# R1(config-if)# clock rate 64000
# R1(config-if)# no shutdown
# R1(config-if)# exit

# R1(config)# interface Serial0/1
# R1(config-if)# ip address 192.168.2.1 255.255.255.252
# R1(config-if)# clock rate 64000
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Access the CLI of Router 2 (R2):
# gns3> connect R2

# Configure the interfaces on R2:

# R2(config)# interface Serial0/0
# R2(config-if)# ip address 192.168.1.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Access the CLI of Router 3 (R3):
# gns3> connect R3

# Configure the interfaces on R3:
# R3(config)# interface Serial0/0
# R3(config-if)# ip address 192.168.2.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# Step 3: Configuring IP SLA on R1


# Create an IP SLA operation to monitor the connection to R2:
# R1(config)# ip sla 1 (if not worked then "ip sla monitor 1")
# R1(config-ip-sla)# icmp-echo 192.168.1.2 (type echo protocol ipIcmpEcho 192.168.1.2)
# R1(config-ip-sla-echo)# frequency 10
# R1(config-ip-sla-echo)# exit

# Create an IP SLA operation to monitor the connection to R3:
# R1(config)# ip sla 2 (if not worked then "ip sla monitor 2")
# R1(config-ip-sla)# icmp-echo 192.168.2.2 (type echo protocol ipIcmpEcho 192.168.2.2)
# R1(config-ip-sla-echo)# frequency 10
# R1(config-ip-sla-echo)# exit


# Schedule the SLA operations:
# R1(config)# ip sla schedule 1 life forever start-time now  (ip sla monitor schedule 1 start-time now life forever)
# R1(config)# ip sla schedule 2 life forever start-time now  (ip sla monitor schedule 2 start-time now life forever)


# Step 4: Configuring Track Objects on R1
# Create track objects to monitor the IP SLA operations:
# R1(config)# track 1 ip sla 1 reachability (track 1 rtr 1 reachability)
# R1(config)# track 2 ip sla 2 reachability (track 2 rtr 2 reachability)

# Step 5: Configuring Path Control on R1
# Configure static routes that depend on the track objects:
# R1(config)# ip route 10.1.1.0 255.255.255.0 192.168.1.2 track 1
# R1(config)# ip route 10.1.1.0 255.255.255.0 192.168.2.2 track 2


# Add a backup static route:
# R1(config)# ip route 10.1.1.0 255.255.255.0 192.168.3.2 2


# Step 6: Verifying the Configuration
# Verify the IP SLA configuration:

# R1# show ip sla configuration (show ip sla monitor configuration)

# Verify the track objects:
# R1# show track 1
# R1# show track 2

# Verify the routing table:
# R1# show ip route