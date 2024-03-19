import unittest
import datetime
from q1_memory import q1_memory
from memory_profiler import profile

class TestQ1Memory(unittest.TestCase):
    @profile
    def test_q1_memory(self):
        """
        Prueba la función q1_memory para asegurar que devuelve los resultados esperados y mide correctamente el uso de memoria.

        Se ejecuta la función q1_memory con un archivo de datos de prueba y se verifica que los resultados obtenidos sean correctos.
        Se mide el uso de memoria de la función y se verifica que sea mayor que cero.

        Args:
        - self: referencia al objeto TestCase

        Returns:
        - None
        """

        # Archivo de datos de prueba
        test_file_path = '../data/farmers-protest-tweets-2021-2-4.json'

        # Ejecutar q1_memory y medir el uso de memoria
        result = q1_memory(test_file_path)

        # Imprimir los resultados obtenidos
        print("Resultados obtenidos:")
        for i, (date, username) in enumerate(result, start=1):
            print(f"{i}. Fecha: {date}, Usuario con más publicaciones: {username}")

        # Verificar que el resultado sea una lista
        self.assertIsInstance(result, list)

        # Verificar que cada elemento de la lista sea una tupla
        for item in result:
            self.assertIsInstance(item, tuple)
            # Verificar que el primer elemento de la tupla sea de tipo date
            self.assertIsInstance(item[0], datetime.date)
            # Verificar que el segundo elemento de la tupla sea de tipo str
            self.assertIsInstance(item[1], str)

if __name__ == '__main__':
    unittest.main()
