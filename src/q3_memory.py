import json
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Esta función procesa un archivo JSON que contiene registros de tweets y devuelve los 10 nombres de usuario
    más mencionados en los tweets, junto con la frecuencia de menciones de cada uno.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los datos de los tweets.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 nombres de usuario más mencionados,
        junto con la frecuencia de menciones de cada uno.

    Raises:
        FileNotFoundError: Si el archivo especificado en file_path no se encuentra.
    """
    # Paso 1: Se procesa el archivo línea por línea
    user_counter = Counter()

    with open(file_path, 'r') as data:
        for line in data:
            tweet_data = json.loads(line)
            mentioned_users = tweet_data.get('mentionedUsers')
            if mentioned_users:
                user_counter.update(user['username'] for user in mentioned_users)

    # Paso 2: Se retornan los 10 usernames más comunes
    return user_counter.most_common(10)