import cProfile
import datetime
import sys
import unittest
sys.path.append('../src') 
from q1_time import q1_time

class TestQ1Time(unittest.TestCase):
    def test_q1_time(self):
        """
        Prueba la función q1_time para asegurar que devuelve los resultados esperados.

        Se ejecuta la función q1_time con un archivo de datos de prueba y se verifica que los resultados obtenidos sean correctos.
        Se imprime el tiempo de ejecución de la función utilizando cProfile y se muestran los resultados obtenidos de manera legible.
        Se verifica que los resultados sean del tipo y formato esperados.

        Args:
        - self: referencia al objeto TestCase

        Returns:
        - None
        """

        # Archivo de datos de prueba
        test_file_path = '../data/farmers-protest-tweets-2021-2-4.json'

        # Medir el tiempo de ejecución de q1_time con cProfile
        profiler = cProfile.Profile()
        profiler.enable()

        # Llama a la función q1_time con el archivo de prueba
        results = q1_time(test_file_path)

        profiler.disable()
        profiler.print_stats(sort='cumulative')

        # Imprime los resultados obtenidos de manera legible
        print("Resultados obtenidos:")
        for i, (date, username) in enumerate(results, start=1):
            print(f"{i}. Fecha: {date}, Usuario con más publicaciones: {username}")
        
        # Verifica que el resultado sea una lista
        self.assertIsInstance(results, list)
        
        # Verifica que cada elemento de la lista sea una tupla
        for item in results:
            self.assertIsInstance(item, tuple)
            # Verifica que el primer elemento de la tupla sea de tipo date
            self.assertIsInstance(item[0], datetime.date)
            # Verifica que el segundo elemento de la tupla sea de tipo str
            self.assertIsInstance(item[1], str)
