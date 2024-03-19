import json
from collections import Counter
from emoji import emoji_list
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los 10 emojis más utilizados en los tweets presentes en el archivo JSON especificado,
    junto con su respectivo conteo de ocurrencias.

    Args:
    - file_path (str): Ruta al archivo JSON que contiene los datos de los tweets.

    Returns:
    - List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 emojis más utilizados, cada una con su respectivo conteo de ocurrencias.
    """
    # Se inicializa un contador para contar la frecuencia de cada emoji
    emoji_counts = Counter()

    # Leer el archivo JSON y procesar los tweets línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            tweet_content = json.loads(line)['content']
            # Obtengo los emojis presentes en el contenido del tweet
            emojis_in_tweet = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            # Actualizo el contador de emojis con la frecuencia de cada emoji en el tweet
            emoji_counts.update(emojis_in_tweet)

    # Se obtienen los 10 emojis más utilizados con su respectivo conteo
    top_10_emojis = emoji_counts.most_common(10)

    return top_10_emojis
