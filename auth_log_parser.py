with open('./original/auth.log', 'r') as auth_log:
    read_auth_log = auth_log.read()

replace_symbol = read_auth_log.replace("|!|", " ")

with open("./modified/auth-mod.log", "w") as parse_logs:
    parse_logs.write(replace_symbol)
