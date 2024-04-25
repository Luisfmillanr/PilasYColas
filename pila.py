class Pila:
    """
    Clase que implementa una estructura de datos tipo pila (LIFO: Last In, First Out).
    Permite realizar operaciones estándar como apilar, desapilar e inspeccionar si está vacía.
    """

    def __init__(self):
        """
        Inicializa la pila vacía.
        """
        self.elementos = []

    def esta_vacia(self):
        """
        Verifica si la pila está vacía.

        Returns:
            bool: True si la pila está vacía, False de lo contrario.
        """
        return not self.elementos

    def apilar(self, item):
        """
        Añade un elemento al tope de la pila.

        Args:
            item: Elemento a ser añadido a la pila.
        """
        self.elementos.append(item)

    def desapilar(self):
        """
        Remueve y retorna el elemento del tope de la pila.

        Returns:
            El elemento en el tope de la pila.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Desapilar de una pila vacía.")
        return self.elementos.pop()

    def ver_tope(self):
        """
        Retorna el elemento en el tope de la pila sin removerlo.

        Returns:
            El elemento en el tope de la pila.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Ver tope en pila vacía.")
        return self.elementos[-1]

    def imprimir(self):
        """
        Imprime todos los elementos de la pila desde el más reciente al más antiguo.

        Returns:
            str: Representación de la pila como una lista de elementos.
        """
        pila_string = "Pila actual: " + str(self.elementos[::-1])  # Imprime la pila comenzando desde el último apilado
        print(pila_string)
        return pila_string

    def modificar_estructura(self, X):
        """
        Modifica la estructura de la pila eliminando todos los elementos hasta encontrar el valor X.
        El valor X no se elimina de la pila.

        Args:
            X (int): El valor que la función buscará en la pila.

        Returns:
            bool: True si se encontró y procesó el valor X, False de lo contrario.
        """
        temporal = []
        encontrado = self._eliminar_hasta_X(X, temporal)
        if encontrado:
            self._reapilar_elementos_restantes(temporal)
        else:
            print(f"El valor {X} no se encontró en la pila.")
        return encontrado

    def _eliminar_hasta_X(self, X, temporal):
        """
        Elimina los elementos de la pila hasta que se encuentre el valor X.

        Args:
            X (int): El valor a buscar.
            temporal (list): Lista para almacenar temporalmente los elementos desapilados.

        Returns:
            bool: True si se encuentra X, False de lo contrario.
        """
        while self.elementos and self.elementos[-1] != X:
            temporal.append(self.desapilar())
        return bool(self.elementos)  # Retorna True si X fue encontrado, False de lo contrario

    def _reapilar_elementos_restantes(self, temporal):
        """
        Vuelve a apilar los elementos restantes que fueron desapilados
        durante la búsqueda de X en la pila.

        Args:
            temporal (list): Lista de elementos desapilados temporalmente.
        """
        while temporal:
            self.apilar(temporal.pop())



