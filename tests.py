import unittest
from pila import Pila
from cola import Cola

class TestPila(unittest.TestCase):
    """Clase de pruebas unitarias para la clase Pila."""
    
    def setUp(self):
        """Inicializa una nueva pila para cada test."""
        self.pila = Pila()

    def test_pila_vacia_al_crear(self):
        """Prueba que la pila esté vacía al inicializarla."""
        self.assertTrue(self.pila.esta_vacia())

    def test_apilar_elemento(self):
        """Prueba apilar un elemento en la pila."""
        self.pila.apilar(1)
        self.assertFalse(self.pila.esta_vacia())

    def test_desapilar_elemento(self):
        """Prueba desapilar un elemento de la pila."""
        self.pila.apilar(2)
        self.pila.apilar(3)
        top_element = self.pila.desapilar()
        self.assertEqual(top_element, 3)
        self.assertFalse(self.pila.esta_vacia())

    def test_desapilar_hasta_vacia(self):
        """Prueba desapilar todos los elementos hasta que la pila esté vacía."""
        self.pila.apilar(4)
        self.pila.desapilar()
        self.assertTrue(self.pila.esta_vacia())

    # Puedes agregar más pruebas según sea necesario

class TestCola(unittest.TestCase):
    """Clase de pruebas unitarias para la clase Cola."""
    
    def setUp(self):
        """Inicializa una nueva cola para cada test."""
        self.cola = Cola()

    def test_cola_vacia_al_crear(self):
        """Prueba que la cola esté vacía al inicializarla."""
        self.assertTrue(self.cola.esta_vacia())

    def test_encolar_elemento(self):
        """Prueba encolar un elemento en la cola."""
        self.cola.encolar(1)
        self.assertFalse(self.cola.esta_vacia())

    def test_desencolar_elemento(self):
        """Prueba desencolar un elemento de la cola."""
        self.cola.encolar(2)
        self.cola.encolar(3)
        first_element = self.cola.desencolar()
        self.assertEqual(first_element, 2)
        self.assertFalse(self.cola.esta_vacia())

    def test_desencolar_hasta_vacia(self):
        """Prueba desencolar todos los elementos hasta que la cola esté vacía."""
        self.cola.encolar(4)
        self.cola.desencolar()
        self.assertTrue(self.cola.esta_vacia())

    # Puedes agregar más pruebas según sea necesario

if __name__ == '__main__':
    unittest.main()
