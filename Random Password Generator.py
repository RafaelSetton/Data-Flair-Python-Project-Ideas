from random import choice
from pyperclip import copy

all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&@?"


def generate(numero_de_caracteres=10):
    senha = ''
    while len(senha) < numero_de_caracteres:
        senha += choice(all_chars)
    copy(senha)
    return senha


print(generate())
