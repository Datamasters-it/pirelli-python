import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)

# Creazione dei processi
if __name__=='__main__':
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # Avvio dei processi
    p1.start()
    p2.start()

    # Attesa della terminazione dei processi
    p1.join()
    p2.join()

    print("Multiprocessing completato.")