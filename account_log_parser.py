with open('./original/accounting.log', 'r') as auth_log:
    read_account_log = auth_log.read()

replace_symbol = read_account_log.replace("|!|", " ")

with open("./modified/accounting-mod.log", "w") as parse_logs:
    parse_logs.write(replace_symbol)
