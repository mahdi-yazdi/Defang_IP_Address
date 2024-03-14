def defang_ip_address(ip:str)->str:
    defanged_ip = ''
    for char in ip:
        if char == '.':
            defanged_ip += '[.]'
        else:
            defanged_ip += char
    return defanged_ip

#Example usage:
ip_address = "192.168.1.1"
defanged_ip = defang_ip_address(ip_address)
print("Original IP:",ip_address)
print("Defanged IP:",defanged_ip)