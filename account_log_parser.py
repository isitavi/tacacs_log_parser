with open('./original/accounting.log', 'r') as auth_log:
    read_auth_log = auth_log.read()

print(read_auth_log.replace("|!|", " "))
