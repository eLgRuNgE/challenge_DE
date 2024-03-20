import json
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Esta función procesa un archivo JSON que contiene registros de tweets y devuelve las 10 fechas más comunes junto con el usuario más activo para cada fecha.

    Args:
        file_path (str): La ruta del archivo JSON que contiene los registros de tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Una lista de tuplas, donde cada tupla contiene una fecha y el usuario más activo para esa fecha.

    Raises:
        FileNotFoundError: Si el archivo especificado en file_path no se encuentra.
    """
    # Paso 1: Obtención de los datos de fecha y usuario
    tweets_dates_users = []
    with open(file_path, 'r') as data:
        for line in data.readlines():
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            tweets_dates_users.append((tweet_date, username))

    # Paso 2: Determinación de las fechas más comunes
    date_counts = {}
    for tweet_date, _ in tweets_dates_users:
        if tweet_date in date_counts:
            date_counts[tweet_date] += 1
        else:
            date_counts[tweet_date] = 1
    most_common_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Paso 3: Obtención del usuario más activo para cada fecha más común
    most_common_users = []
    for date, _ in most_common_dates:
        user_counts = {}
        for tweet_date, username in tweets_dates_users:
            if tweet_date == date:
                if username in user_counts:
                    user_counts[username] += 1
                else:
                    user_counts[username] = 1
        most_common_user = max(user_counts, key=user_counts.get)
        most_common_users.append(most_common_user)

    # Paso 4: Formateo de las fechas y agrupación con los usuarios
    result = [(datetime.strptime(date[0], "%Y-%m-%d").date(), user)
                for date, user in zip(most_common_dates, most_common_users)]

    # Paso 5: Retorno de resultados
    return result