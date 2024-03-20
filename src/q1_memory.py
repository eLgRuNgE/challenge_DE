import json
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Esta función analiza un archivo JSON que contiene registros de tweets y devuelve las 10 fechas
    más comunes junto con el usuario más activo para cada fecha.

    Args:
        file_path (str): La ruta del archivo JSON que contiene los registros de tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Una lista de tuplas, donde cada tupla contiene una fecha
        y el usuario más activo para esa fecha.

    Raises:
        FileNotFoundError: Si no se encuentra el archivo especificado en file_path.
    """

    # Paso 1: Lectura del archivo JSON
    dates_dict = defaultdict(lambda: defaultdict(int))

    # Paso 2: Procesamiento de los datos
    with open(file_path, 'r') as data:
        for line_data in data:
            tweet = json.loads(line_data)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']

            # Actualización del contador de tweets por usuario y fecha
            dates_dict[tweet_date][username] += 1

    # Paso 3: Determinación de las fechas más comunes
    top_dates = sorted(dates_dict.keys(), key=lambda x: sum(dates_dict[x].values()), reverse=True)[:10]

    # Paso 4: Obtención del usuario más activo por fecha
    top_users = [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]

    # Paso 5: Formateo de las fechas
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]

    # Paso 6: Agrupación de las fechas y usuarios
    result = list(zip(top_dates, top_users))

    return result