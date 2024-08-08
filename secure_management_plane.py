# Practical 4: Secure the Management Plane
# Securing the management plane involves ensuring that access to network devices is restricted and protected against unauthorized access. This typically includes securing access via SSH, using access control lists (ACLs), and enabling logging and monitoring.

# Step 1: Setting Up the Network in GNS3

# Open GNS3 and create a new project.
# Add three routers (R1, R2, R3) and connect them as follows:
# R1 to R2 via a serial link.
# R2 to R3 via another serial link.
# Connect R1 to a PC for management purposes.

# Step 2: Configuring Basic Security on Router 1 (R1)
# Access the CLI of Router 1 (R1):
# gns3> connect R1

# Set Up a Local User Account:
# R1(config)# username admin privilege 15 secret admin_password

# Enable SSH on the Router:
# R1(config)# ip domain-name example.com
# R1(config)# crypto key generate rsa
# The name for the keys will be: R1.example.com
# How many bits in the modulus [512]: 1024
# R1(config)# ip ssh version 2

# Configure VTY Lines to Use Local Authentication and SSH:
# R1(config)# line vty 0 4
# R1(config-line)# login local
# R1(config-line)# transport input ssh
# R1(config-line)# exit

# Set Up an Enable Secret Password:
# R1(config)# enable secret enable_password
# Step 3: Configuring Access Control Lists (ACLs) to Restrict Management Access

# Create an ACL to Permit Only a Specific IP Range:
# R1(config)# access-list 10 permit 192.168.1.0 0.0.0.255

# Apply the ACL to the VTY Lines:
# R1(config)# line vty 0 4
# R1(config-line)# access-class 10 in
# R1(config-line)# exit

# Step 4: Configuring AAA Radius Authentication

# Define the Radius Server:
# R1(config)# radius-server host 192.168.1.100 auth-port 1645 acct-port 1646 key radius_secret

# Configure AAA Authentication:
# R1(config)# aaa new-model
# R1(config)# aaa authentication login default group radius local
# R1(config)# aaa authentication login console group radius local

# Configure AAA Authorization:
# R1(config)# aaa authorization exec default group radius local
# R1(config)# aaa authorization commands 15 default group radius local

# Configure AAA Accounting:
# R1(config)# aaa accounting exec default start-stop group radius
# R1(config)# aaa accounting commands 15 default start-stop group radius

# Step 5: Configuring Logging and Monitoring

# Enable Logging to a Local Buffer:
# R1(config)# logging buffered 4096

# Set the Logging Level:
# R1(config)# logging console informational

# (Optional) Configure Logging to a Remote Syslog Server:
# R1(config)# logging host 192.168.1.100
# R1(config)# logging trap informational

# Step 6: Verifying the Configuration

# Verify SSH Configuration:
# R1# show ip ssh

# Verify ACL Configuration:
# R1# show access-lists 10

# Verify VTY Line Configuration:
# R1# show running-config | section line vty

# Check the Logging Status:
# R1# show logging

