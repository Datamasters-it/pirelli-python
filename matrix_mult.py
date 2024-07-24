import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing


def duration(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start}")
        return result
    return wrapper

# Funzione di supporto per creare una matrice casuale
def create_random_matrix(rows, cols):
    import random
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def multiply_row(row, matrix_b):
    result = []
    for j in range(len(matrix_b[0])):
        dot_product = 0
        for i in range(len(row)):
            dot_product += row[i] * matrix_b[i][j]
        result.append(dot_product)
    return result


def multiply_matrices_without_threads(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    
    # Inizializza la matrice risultato
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Esegue la moltiplicazione
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

@duration
def parallel_matrix_multiply(matrix_a, matrix_b):
    # possiamo usare multiprocessing.cpu_count() per smistare sul numero disponibile di CPU
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = [executor.submit(multiply_row, row, matrix_b) for row in matrix_a]
        result = []
        for future in as_completed(futures):
            result.append(future.result())
    return result



# Esempio di utilizzo
if __name__ == '__main__':
    # Crea due matrici di esempio
    '''
    a = [
        [10, 20, 30],
        [20, 30, 40],
        [30, 40, 50]
    ]
    b = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    '''
    
    a = create_random_matrix(1000, 1000)
    b = create_random_matrix(1000, 1000)

    # Esegui la moltiplicazione sequenziale
    start = time.time()
    # result_1 = multiply_matrices_without_threads(a, b)
    end = time.time()

    print(f"WITHOUT THREADS -> {end-start} seconds")

    # Esegui la moltiplicazione parallela
    start = time.time()
    result_2 = parallel_matrix_multiply(a, b)
    end = time.time()

    # print("Dimensioni del risultato:", len(result), "x", len(result[0]))

    # print(result)
    print(f"WITH THREADS -> {end-start} seconds")