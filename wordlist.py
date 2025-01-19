import random

# Función para generar palabras aleatorias
def generate_random_word():
    length = random.randint(3, 10)  # Longitud aleatoria entre 3 y 10 caracteres
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

# Función para generar la wordlist
def create_wordlist(filename, num_words=1000):
    with open(filename, 'w') as file:
        for _ in range(num_words):
            word = generate_random_word()
            file.write(word + '\n')
    print(f"Wordlist generada con {num_words} palabras en '{filename}'.")

# Parámetros
if __name__ == '__main__':
    filename = "wordlist.txt"
    num_words = random.randint(1000, 2000)  # Número aleatorio entre 1000 y 2000
    create_wordlist(filename, num_words)
