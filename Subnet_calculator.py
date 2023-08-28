import ipaddress


def subnet_calculator(ip, subnet_mask):
    # Parse the user input IP and subnet mask
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    print(f"IP Address: {network.network_address}")
    print(f"Subnet Mask: {network.netmask}")
    print(f"Number of Subnets: {len(list(network.subnets()))}")

    print("\nSubnet Details:")
    for subnet in network.subnets():
        print(f"Subnet: {subnet}")
        print(f"Network Address: {subnet.network_address}")
        print(f"Broadcast Address: {subnet.broadcast_address}")
        print(f"Usable Host IP Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
        print(f"Number of Usable Hosts: {subnet.num_addresses - 2}")
        print()


if __name__ == "__main__":
    ip = input("Enter an IP address: ")
    subnet_mask = input("Enter a subnet mask: ")

    subnet_calculator(ip, subnet_mask)