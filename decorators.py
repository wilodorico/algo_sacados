import logging
import time
import memory_profiler


def measure_time(func):
    """Décorateur qui mesure le temps d'exécution d'une fonction."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Fonction '{func.__name__}' a pris {end_time - start_time:.4f} secondes pour s'exécuter.")
        return result

    return wrapper


@memory_profiler.profile
def measure_memory(func):
    """Décorateur pour mesurer la mémoire utilisée par une fonction."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        memory_usage = memory_profiler.memory_usage(-1)[0]  # Récupère la première valeur de mémoire utilisée
        logging.info(f"Fonction '{func.__name__}' a utilisé {memory_usage:.2f} MB de mémoire.")
        return result

    return wrapper
