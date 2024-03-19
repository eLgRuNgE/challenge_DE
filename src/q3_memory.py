import json
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra el top 10 histórico de usuarios más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos.

    Args:
    - file_path (str): Ruta al archivo JSON que contiene los datos de los tweets.

    Returns:
    - List[Tuple[str, int]]: Una lista de tuplas que contiene el top 10 de usuarios más influyentes, cada uno con su respectivo conteo de menciones.
    """
    # Inicializar un contador para almacenar el conteo de menciones de cada usuario
    user_mentions = Counter()

    # Leer el archivo JSON y procesar los tweets línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            # Obtener el nombre de usuario del tweet
            username = tweet['user']['username']
            # Contar las menciones (@) en el contenido del tweet
            mentions_count = tweet['content'].count('@')
            # Actualizar el contador de menciones para el usuario
            user_mentions[username] += mentions_count

    # Obtener los top 10 usuarios más influyentes con su respectivo conteo de menciones
    top_users = user_mentions.most_common(10)

    return top_users
