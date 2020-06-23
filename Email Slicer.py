email = input("E-mail: ")

username, domain = email.split('@')

domain = domain.split('.')[0]

print(f"Usuário: {username}")
print(f"Domínio: {domain}")
