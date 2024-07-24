import threading
import time

def print_numbers():
    print("print_numbers")

def print_letters():
    print("print_letters")

# Creazione dei thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Avvio dei thread
t1.start()
# Attesa della terminazione dei thread
t1.join()

t2.start()
t2.join()

print("Threading completato.")