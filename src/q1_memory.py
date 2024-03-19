import json
from collections import Counter
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Encuentra las 10 fechas principales con más tweets y los usuarios más activos en esas fechas.

    Args:
    - file_path (str): Ruta al archivo JSON que contiene los datos de los tweets.

    Returns:
    - List[Tuple[datetime.date, str]]: Una lista de tuplas que contiene la fecha y el usuario más activo para cada una de las 10 fechas principales.
    """
    # Leer el archivo JSON
    with open(file_path, 'r') as f:
        data = [[json.loads(line)['date'].split('T')[0], json.loads(line)['user']['username']] for line in f.readlines()]

    # Validar si hay datos
    if not data:
        return []

    # Obtener las 10 fechas más comunes
    most_common_dates = Counter([d[0] for d in data]).most_common(10)

    # Obtener el usuario más activo por fecha
    most_common_users = []
    for date in most_common_dates:
        users_for_date = [d[1] for d in data if d[0] == date[0]]
        if users_for_date:
            most_common_users.append(Counter(users_for_date).most_common(1)[0][0])
        else:
            # Manejar el caso de una fecha sin usuarios
            most_common_users.append(None)

    # Formatear las fechas
    formatted_dates = [datetime.strptime(date[0], "%Y-%m-%d").date() for date in most_common_dates]

    # Agrupar las fechas y usuarios
    results = list(zip(formatted_dates, most_common_users))

    return results
