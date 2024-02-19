import random 
import string


def password(len_pass):
    ascii_option = string.ascii_letters
    number_option = string.digits
    caractercs_option = string.punctuation
    
    option= ascii_option + number_option + caractercs_option
    
    senha = ""
    
    for i in range(0,len_pass):
        creation = random.choice(option)
        senha = senha + creation
    return senha 

digit = input("Digite quantos digitos sua senha tera ? ")

if digit.isdigit():
    digit = int(digit)
else:
    print("Entrada inválida")
    quit()
    
response = password(len_pass= digit)
print(f'Senha gerada: \n{response}')