address_code = []
print("Enter 3-address code statements(enter end or END for end or input)")
while(True):
    stmnt = input()
    if (stmnt=='end' or stmnt=='END'):
        break
    else:
        address_code.append(stmnt)
    
print(address_code)