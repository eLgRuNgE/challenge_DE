import cProfile
import sys
import unittest
sys.path.append('../src') 
from q2_time import q2_time

class TestQ2Time(unittest.TestCase):
    def test_q2_time(self):
        """
        Prueba la función q2_time para asegurar que devuelve los resultados esperados.

        Se ejecuta la función q2_time con un archivo de datos de prueba y se verifica que los resultados obtenidos sean correctos.
        Se imprime el tiempo de ejecución de la función utilizando cProfile y se muestran los resultados obtenidos de manera legible.
        Se verifica que los resultados sean del tipo y formato esperados.

        Args:
        - self: referencia al objeto TestCase

        Returns:
        - None
        """

        # Archivo de datos de prueba
        test_file_path = '../data/farmers-protest-tweets-2021-2-4.json'

        # Medir el tiempo de ejecución de q2_time con cProfile
        profiler = cProfile.Profile()
        profiler.enable()

        # Llama a la función q2_time con el archivo de prueba
        results = q2_time(test_file_path)

        profiler.disable()
        profiler.print_stats(sort='cumulative')

        # Imprime los resultados obtenidos de manera legible
        print("Resultados obtenidos:")
        for i, (emoji, count) in enumerate(results, start=1):
            print(f"{i}. Emoji: {emoji}, Conteo: {count}")
        
        # Verifica que el resultado sea una lista
        self.assertIsInstance(results, list)
        
        # Verifica que cada elemento de la lista sea una tupla
        for item in results:
            self.assertIsInstance(item, tuple)
            # Verifica que el primer elemento de la tupla sea de tipo str (emoji)
            self.assertIsInstance(item[0], str)
            # Verifica que el segundo elemento de la tupla sea de tipo int (conteo)
            self.assertIsInstance(item[1], int)

if __name__ == '__main__':
    unittest.main()
