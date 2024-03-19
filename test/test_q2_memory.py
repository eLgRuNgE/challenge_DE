import memory_profiler
import sys
import unittest
sys.path.append('../src') 
from q2_memory import q2_memory

class TestQ2Memory(unittest.TestCase):
    def test_q2_memory(self):
        """
        Prueba la función q2_memory para asegurar que devuelve los resultados esperados.

        Se ejecuta la función q2_memory con un archivo de datos de prueba y se verifica que los resultados obtenidos sean correctos.
        Se imprime el uso de memoria durante la ejecución de la función utilizando memory-profiler.
        Se verifica que los resultados sean del tipo y formato esperados.

        Args:
        - self: referencia al objeto TestCase

        Returns:
        - None
        """

        # Archivo de datos de prueba
        test_file_path = '../data/farmers-protest-tweets-2021-2-4.json'

        # Medir el uso de memoria de q3_memory con memory-profiler
        mem_usage = memory_profiler.memory_usage((q2_memory, (test_file_path,)))

        # Imprimir el uso de memoria
        print(f"Uso de memoria de q2_memory: {max(mem_usage)} MB")

        # Llama a la función q2_memory con el archivo de prueba
        results = q2_memory(test_file_path)

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
