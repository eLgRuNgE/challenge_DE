import memory_profiler
import sys
import unittest
sys.path.append('../src') 
from q3_memory import q3_memory

class TestQ3Memory(unittest.TestCase):
    def test_q3_memory(self):
        """
        Prueba la función q3_memory para asegurar que devuelve los resultados esperados.

        Se ejecuta la función q3_memory con un archivo de datos de prueba y se verifica que los resultados obtenidos sean correctos.
        Se mide el uso de memoria de la función utilizando memory-profiler y se verifica que los resultados sean del tipo y formato esperados.

        Args:
        - self: referencia al objeto TestCase

        Returns:
        - None
        """

        # Archivo de datos de prueba
        test_file_path = '../data/farmers-protest-tweets-2021-2-4.json'

        # Medir el uso de memoria de q3_memory con memory-profiler
        mem_usage = memory_profiler.memory_usage((q3_memory, (test_file_path,)))

        # Imprimir el uso de memoria
        print(f"Uso de memoria de q3_memory: {max(mem_usage)} MB")

        # Llama a la función q3_memory con el archivo de prueba
        results = q3_memory(test_file_path)

        # Imprime los resultados obtenidos de manera legible
        print("Top 10 usuarios más influyentes:")
        for i, (user, count) in enumerate(results, start=1):
            print(f"{i}. Usuario: {user}, @s: {count}")
        
        # Verifica que el resultado sea una lista
        self.assertIsInstance(results, list)
        
        # Verifica que cada elemento de la lista sea una tupla
        for item in results:
            self.assertIsInstance(item, tuple)
            # Verifica que el primer elemento de la tupla sea de tipo str
            self.assertIsInstance(item[0], str)
            # Verifica que el segundo elemento de la tupla sea de tipo int
            self.assertIsInstance(item[1], int)

if __name__ == '__main__':
    unittest.main()
