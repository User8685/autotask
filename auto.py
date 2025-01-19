import webbrowser
import time

# Función para leer palabras desde la wordlist
def read_wordlist(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'.")
        return []

# Función para abrir los enlaces en el navegador
def open_links(wordlist, delay=5):
    try:
        for word in wordlist:
            url = f"https://www.bing.com/search?q={word}"
            print(f"Abrir: {url}")
            
            # Abrir el enlace en el navegador predeterminado
            webbrowser.open(url)
            
            # Esperar el tiempo definido antes de abrir el siguiente enlace
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario. Saliendo...")

# Parámetros principales
if __name__ == '__main__':
    # Nombre del archivo de la wordlist
    wordlist_file = "wordlist.txt"
    
    # Leer la wordlist
    wordlist = read_wordlist(wordlist_file)
    
    # Si la wordlist no está vacía, comenzar a abrir enlaces
    if wordlist:
        print("Iniciando apertura de enlaces. Presiona Ctrl+C para detener.")
        open_links(wordlist, delay=5)  # Cambia delay a 10 si deseas un mayor intervalo
    else:
        print("No hay palabras para procesar. Verifica tu wordlist.")
