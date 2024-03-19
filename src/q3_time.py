import json
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los 10 usuarios más influyentes en función del conteo de menciones (@) en los tweets presentes en el archivo JSON especificado.

    Args:
    - file_path (str): Ruta al archivo JSON que contiene los datos de los tweets.

    Returns:
    - List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 usuarios más influyentes, cada uno con su respectivo conteo de menciones.
    """
    # Inicializar un contador para contar el número de menciones de cada usuario
    user_mentions = Counter()

    # Leer el archivo JSON y procesar los tweets línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            # Obtener el nombre de usuario (username) del tweet
            username = tweet['user']['username']
            # Contar el número de menciones (@) en el contenido del tweet
            mentions_count = tweet['content'].count('@')
            # Actualizar el contador de menciones del usuario
            user_mentions[username] += mentions_count

    # Obtener los 10 usuarios más influyentes con su respectivo conteo de menciones
    top_10_users = user_mentions.most_common(10)

    return top_10_users