with open('./original/accounting.log', 'r') as auth_log:
    read_account_log = auth_log.read()

print(read_account_log.replace("|!|", " "))
