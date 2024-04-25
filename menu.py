from pila import Pila
from cola import Cola

import sys
sys.path.insert(0, '/ruta/a/tu/directorio/Unir/Python')


def mostrar_menu():
    """
    Muestra las opciones del menú y retorna la elección del usuario.

    Returns:
        int: La opción del menú elegida por el usuario.
    """
    menu_opciones = [
        "Apilar elemento en Pila",
        "Desapilar elemento de Pila",
        "Encolar elemento en Cola",
        "Desencolar elemento de Cola",
        "Modificar estructura Pila",
        "Modificar estructura Cola",
        "Imprimir Pila",
        "Imprimir Cola",
        "Salir"
    ]
    
    print("\nMenú de Operaciones:")
    for i, opcion in enumerate(menu_opciones, 1):
        print(f"{i}. {opcion}")
    
    try:
        seleccion = int(input("Seleccione una opción: "))
        if 1 <= seleccion <= len(menu_opciones):
            return seleccion
        else:
            raise ValueError
    except ValueError:
        print("Por favor, ingrese un número válido correspondiente a las opciones del menú.")
        return mostrar_menu()  # Recursividad para mostrar el menú nuevamente

def obtener_input_numerico(prompt):
    """
    Solicita al usuario un número entero y lo valida.

    Args:
        prompt (str): El mensaje a mostrar al solicitar el input.

    Returns:
        int: El número ingresado por el usuario.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número entero.")

def main():
    """
    Ejecuta el programa principal que interactúa con el usuario para manipular Pilas y Colas.
    """
    pila = Pila()
    cola = Cola()

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            elemento = obtener_input_numerico("Ingrese un valor para apilar: ")
            pila.apilar(elemento)
            print("Valor apilado correctamente.")
        elif opcion == 2:
            if not pila.esta_vacia():
                print("Elemento desapilado:", pila.desapilar())
            else:
                print("La pila está vacía.")
        elif opcion == 3:
            elemento = obtener_input_numerico("Ingrese un valor para encolar: ")
            cola.encolar(elemento)
            print("Valor encolado correctamente.")
        elif opcion == 4:
            if not cola.esta_vacia():
                print("Elemento desencolado:", cola.desencolar())
            else:
                print("La cola está vacía.")
        elif opcion == 5:
            X = obtener_input_numerico("Ingrese el valor X para modificar la Pila: ")
            pila.modificar_estructura(X)
            pila.imprimir()
        elif opcion == 6:
            X = obtener_input_numerico("Ingrese el valor X para modificar la Cola: ")
            cola.modificar_estructura(X)
            cola.imprimir()
        elif opcion == 7:
            pila.imprimir()
        elif opcion == 8:
            cola.imprimir()
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()

