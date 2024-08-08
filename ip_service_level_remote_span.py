# Practical 6: Simulate IP SLA and Remote SPAN Using Available Devices
# Network Setup:

# Router 1 (R1) (Core Router)
# Router 2 (R2) (Distribution Router)
# Router 3 (R3) (Access Router)
# Switch 1 (SW1) (Access Switch)
# Switch 2 (SW2) (Distribution Switch)

# Configuration Steps

# Step 1: Set Up the Network

# 1.1 Configure Routers:

# Router 1 (R1):
# R1# configure terminal
# R1(config)# interface Serial0/0
# R1(config-if)# ip address 10.1.1.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit
# R1(config)# interface Serial0/1
# R1(config-if)# ip address 10.1.2.1 255.255.255.0
# R1(config-if)# no shutdown
# R1(config-if)# exit

# Router 2 (R2):
# R2# configure terminal
# R2(config)# interface Serial0/0
# R2(config-if)# ip address 10.1.1.2 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit
# R2(config)# interface Serial0/1
# R2(config-if)# ip address 10.1.3.1 255.255.255.0
# R2(config-if)# no shutdown
# R2(config-if)# exit

# Router 3 (R3):
# R3# configure terminal
# R3(config)# interface Serial0/0
# R3(config-if)# ip address 10.1.3.2 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit
# R3(config)# interface Serial0/1
# R3(config-if)# ip address 10.1.4.1 255.255.255.0
# R3(config-if)# no shutdown
# R3(config-if)# exit

# 1.2 Configure Switches:

# Switch 1 (SW1):
# Assign VLANs and Configure Ports:
# SW1# configure terminal
# SW1(config)# vlan 10
# SW1(config-vlan)# name Access_VLAN
# SW1(config-vlan)# exit
# SW1(config)# interface Serial0/1
# SW1(config-if)# switchport mode access
# SW1(config-if)# switchport access vlan 10
# SW1(config-if)# exit

# Switch 2 (SW2):
# Assign VLANs and Configure Ports:
# SW2# configure terminal
# SW2(config)# vlan 20
# SW2(config-vlan)# name Distribution_VLAN
# SW2(config-vlan)# exit
# SW2(config)# interface Serial0/1
# SW2(config-if)# switchport mode access
# SW2(config-if)# switchport access vlan 20
# SW2(config-if)# exit

# Step 2: Configure IP SLA

# On Router 1 (R1):
# Configure IP SLA Monitoring:
# R1# configure terminal
# R1(config)# ip sla 1
# R1(config-ip-sla)# icmp-echo 10.1.3.2
# R1(config-ip-sla)# timeout 1000
# R1(config-ip-sla)# frequency 10
# R1(config-ip-sla)# exit

# (if ip sla not work then use sla monitor)
# R1# configure terminal
# R1(config)# sla monitor 1
# R1(config-sla-monitor)# type echo protocol ipIcmpEcho 10.1.3.2
# R1(config-sla-monitor)# frequency 10
# R1(config-sla-monitor)# exit


# Schedule IP SLA:
# R1# configure terminal
# R1(config)# ip sla schedule 1 life forever start-time now (sla monitor schedule 1 life forever start-time now)
# R1(config)# exit

# Verify IP SLA:
# R1# show ip sla statistics (show sla monitor statistics)

# Step 3: Configure Remote SPAN (RSPAN)

# Since RSPAN is typically supported on more advanced switches, you can simulate a similar function using port mirroring concepts on your available Ethernet switches.

# On Switch 1 (SW1):
# Set up Port Mirroring:
# SW1# configure terminal
# SW1(config)# monitor session 1 source interface Serial0/1
# SW1(config)# monitor session 1 destination interface Serial0/2
# SW1(config)# exit

# On Switch 2 (SW2):
# Set up Port Mirroring:
# SW2# configure terminal
# SW2(config)# monitor session 1 source vlan 10
# SW2(config)# monitor session 1 destination interface Serial0/1
# SW2(config)# exit

# Step 4: Verify Configuration

# Verify IP SLA on R1:
# R1# show ip sla statistics (show sla monitor statistics)

# Verify Port Mirroring:
# On SW1 and SW2, you can use the following command to verify the configuration of the monitoring sessions:
# SW1# show monitor session 1
# SW2# show monitor session 1