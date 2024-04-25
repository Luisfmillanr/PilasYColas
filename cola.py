from collections import deque

class Cola:
    """
    Clase que implementa una estructura de datos tipo cola (FIFO: First In, First Out).
    Permite realizar operaciones estándar como encolar, desencolar e inspeccionar si está vacía.
    """

    def __init__(self):
        """
        Inicializa la cola vacía utilizando 'deque' para una gestión eficiente de los elementos.
        """
        self.elementos = deque()

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si la cola está vacía, False de lo contrario.
        """
        return not self.elementos

    def encolar(self, item):
        """
        Añade un elemento al final de la cola.

        Args:
            item: Elemento a ser añadido a la cola.
        """
        self.elementos.append(item)

    def desencolar(self):
        """
        Remueve y retorna el elemento al frente de la cola.

        Returns:
            El elemento al frente de la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Desencolar de una cola vacía.")
        return self.elementos.popleft()

    def ver_primero(self):
        """
        Retorna el elemento al frente de la cola sin removerlo.

        Returns:
            El elemento al frente de la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Ver primero en cola vacía.")
        return self.elementos[0]

    def imprimir(self):
        """
        Imprime todos los elementos en la cola desde el primer elemento encolado hasta el último.
        
        Returns:
            str: Representación de la cola como una lista de elementos.
        """
        cola_string = "Cola actual: " + str(list(self.elementos))
        print(cola_string)
        return cola_string

    def modificar_estructura(self, X):
        """
        Modifica la estructura de la cola eliminando todos los elementos hasta encontrar el valor X.
        El valor X no se elimina de la cola.

        Args:
            X (int): El valor que la función buscará en la cola.

        Returns:
            bool: True si se encontró y procesó el valor X, False de lo contrario.
        """
        encontrado = self._eliminar_hasta_X(X)
        if encontrado:
            self._reencolar_elementos_restantes()
        else:
            print(f"El valor {X} no se encontró en la cola.")
        return encontrado

    def _eliminar_hasta_X(self, X):
        """
        Elimina los elementos de la cola hasta que se encuentre el valor X.

        Args:
            X (int): El valor a buscar.

        Returns:
            bool: True si se encuentra X, False de lo contrario.
        """
        for _ in range(len(self.elementos)):
            elemento = self.desencolar()
            if elemento == X:
                self.encolar(elemento)
                return True
        return False

    def _reencolar_elementos_restantes(self):
        """
        Vuelve a encolar los elementos restantes que fueron desencolados
        durante la búsqueda de X en la cola.
        """
        elementos_restantes = list(self.elementos)
        self.elementos.clear()
        for elemento in elementos_restantes:
            self.encolar(elemento)


