def q3_time(file_path: str) -> List[Tuple[str, int]]:
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
    # Paso 1: Se obtienen las listas de usuarios mencionados en cada tweet
    with open(file_path, 'r') as data:
        tweet_mentioned_users = [json.loads(line)['mentionedUsers'] for line in data.readlines()]

    # Paso 2: Se obtiene el username de cada user dentro de cada lista de mentionedUsers, exceptuando las listas vacías (caso None).
    usernames = [user['username'] for obj in tweet_mentioned_users if obj is not None for user in obj]

    # Paso 3: Se retornan los 10 usernames más comunes usando la clase Counter para contar y ordenar.
    return Counter(usernames).most_common(10)
