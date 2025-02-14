# 1__situação do aluno

nota = float(input('Digite sua nota: '))

if nota >= 6:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')



# 2___idade para votação

idade = int(input('Digite sua idade: '))

if idade >= 16:
    print('Você pode votar')
else:
    print('Você não pode votar')


# 3___nota A, B, C, D ou F

nota = int(input('Digite sua nota: '))

if nota >= 90 and nota <= 100:
    print(' "Parabéns, você tirou A!"')
elif nota >= 80 and nota < 90:
    print('Muito bem, você tirou B.')
elif nota >= 70 and nota < 80:
    print('Bom trabalho, você tirou C')
elif nota >= 60 and nota < 70:
    print('Fique atento, você tirou D')
elif nota >= 0 and nota < 60:
    print('Estude um pouco mais, você tirou F.')
else:
    print('nota invalida.')


# 4___soma dos números

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(f'a soma entre {n1} e {n2} é {n1 + n2}')


# 5___senha correta

s = input('Digite a senha: ')
senha = 'Python123'

while(s != senha):
    s = input('Digite a senha: ')


# 6___números de 1 a 10

contador = 0

while(contador < 10):
    contador += 1

    print(contador)




# 7___ordem crescente 

numbers = [8, 3, 10, 1, 5]

numbers.sort()

print(numbers)




# 8___nomes na tupla

nomes = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')

print(f'primeiro nome {nomes[0]} e último nome {nomes[-1]}')



# 9___dobro


def dobro(number):
    result = number * 2
    print(result)

dobro(9)



# 10___contar letras

nome = 'leo'

def contar_letras(nome):
    contador = 0
    for letra in nome:
        contador += 1
    print(f'{nome} tem {contador} letras')

contar_letras('leonardo')