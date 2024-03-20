import json
from collections import Counter
from datetime import datetime
from emoji import emoji_list
from typing import List, Tuple

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Esta función procesa un archivo JSON que contiene registros de tweets y devuelve los 10 emojis más utilizados,
    junto con su respectivo conteo de ocurrencias.

    Args:
        file_path (str): La ruta del archivo JSON que contiene los datos de los tweets.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 emojis más utilizados,
        cada una con su respectivo conteo de ocurrencias.

    Raises:
        FileNotFoundError: Si el archivo especificado en file_path no se encuentra.
    """

    # Inicialización del contador de emojis
    emoji_counter = Counter()

    # Lectura del archivo JSON y procesamiento de los tweets
    with open(file_path, 'r') as data:
        for line in data:
            tweet_content = json.loads(line)['content']

            # Obtención de los emojis de cada línea
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]

            # Actualización del contador de emojis
            emoji_counter.update(tweet_emojis)

    # Devolución de los 10 emojis más utilizados
    return emoji_counter.most_common(10)
