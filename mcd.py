"""
Calcula el Máximo Común Divisor (MCD).
"""


class NumeroInvalidoException(Exception):
    """Excepción personalizada para números no válidos."""


class CalculadoraMCD:
    """Clase que calcula el MCD entre dos números naturales."""

    def __init__(self):
        """Inicializa los atributos privados num1 y num2."""
        self._num1 = None
        self._num2 = None

    @property
    def num1(self):
        """Obtiene el valor de num1."""
        return self._num1

    @num1.setter
    def num1(self, valor):
        """Asigna un valor entero positivo a num1."""
        if not isinstance(valor, int) or valor <= 0:
            raise NumeroInvalidoException("El número 1 debe ser un entero positivo.")
        self._num1 = valor

    @property
    def num2(self):
        """Obtiene el valor de num2."""
        return self._num2

    @num2.setter
    def num2(self, valor):
        """Asigna un valor entero positivo a num2."""
        if not isinstance(valor, int) or valor <= 0:
            raise NumeroInvalidoException("El número 2 debe ser un entero positivo.")
        self._num2 = valor

    def calcular_mcd(self):
        """Calcula el MCD de num1 y num2 usando el algoritmo de Euclides."""
        a, b = self._num1, self._num2
        while b != 0:
            a, b = b, a % b
        return a

    def solicitar_numero(self, mensaje):
        """
        Solicita al usuario un número entero positivo con validación.

        Args:
            mensaje (str): El mensaje que se muestra al pedir el número.

        Returns:
            int: Un número entero positivo validado.
        """
        while True:
            try:
                entrada = input(mensaje)
                numero = int(entrada)
                if numero <= 0:
                    raise NumeroInvalidoException("Debe ingresar un número entero positivo.")
                return numero
            except ValueError:
                print("Error: Ingrese un número entero válido.")
            except NumeroInvalidoException as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    calculadora = CalculadoraMCD()

    try:
        calculadora.num1 = calculadora.solicitar_numero(
            "Ingrese el primer número entero positivo: "
        )
        calculadora.num2 = calculadora.solicitar_numero(
            "Ingrese el segundo número entero positivo: "
        )

        resultado_mcd = calculadora.calcular_mcd()

        print(
            f"\nEl Máximo Común Divisor de {calculadora.num1} "
            f"y {calculadora.num2} es: {resultado_mcd}"
        )

    except NumeroInvalidoException as e:
        print(f"Error: {e}")
