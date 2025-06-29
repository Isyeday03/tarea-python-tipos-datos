"""
Programa: Calculadora de Índice de Masa Corporal (IMC)
Autor: Edwin Armijos
Fecha: 28/6/2025
Descripción: Este programa calcula el Índice de Masa Corporal (IMC) de una persona
             basándose en su peso y estatura, y proporciona una interpretación
             del resultado según los estándares de la OMS.
"""


def calcular_imc(peso_kg, estatura_metros):
    """
    Calcula el Índice de Masa Corporal (IMC)

    Args:
        peso_kg (float): Peso de la persona en kilogramos
        estatura_metros (float): Estatura de la persona en metros

    Returns:
        float: Valor del IMC calculado
    """
    imc = peso_kg / (estatura_metros ** 2)
    return imc


def interpretar_imc(valor_imc):
    """
    Interpreta el valor del IMC según los estándares de la OMS

    Args:
        valor_imc (float): Valor del IMC a interpretar

    Returns:
        str: Interpretación del IMC
    """
    if valor_imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= valor_imc < 25.0:
        return "Peso normal"
    elif 25.0 <= valor_imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidad"


def validar_entrada_numerica(mensaje, valor_minimo=0):
    """
    Valida que la entrada del usuario sea un número válido

    Args:
        mensaje (str): Mensaje a mostrar al usuario
        valor_minimo (float): Valor mínimo permitido

    Returns:
        float: Valor numérico válido ingresado por el usuario
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor > valor_minimo:
                return valor
            else:
                print(f"Error: El valor debe ser mayor que {valor_minimo}")
        except ValueError:
            print("Error: Por favor ingrese un número válido")


def main():
    """
    Función principal que ejecuta el programa
    """
    # Variables de tipo string para mensajes y presentación
    titulo_programa = "=== CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC) ==="
    linea_separadora = "=" * 50

    # Mostrar título del programa
    print(linea_separadora)
    print(titulo_programa)
    print(linea_separadora)
    print()

    # Variable de tipo boolean para controlar el bucle del programa
    continuar_programa = True

    while continuar_programa:
        # Solicitar datos al usuario con validación
        print("Por favor, ingrese los siguientes datos:")

        # Variables de tipo float para almacenar peso y estatura
        peso_usuario = validar_entrada_numerica("Peso en kilogramos: ", 0)
        estatura_usuario = validar_entrada_numerica("Estatura en metros (ej: 1.75): ", 0)

        # Calcular el IMC
        imc_calculado = calcular_imc(peso_usuario, estatura_usuario)

        # Obtener la interpretación del IMC
        interpretacion_imc = interpretar_imc(imc_calculado)

        # Mostrar los resultados
        print("\n" + "=" * 30)
        print("RESULTADOS:")
        print("=" * 30)
        print(f"Peso: {peso_usuario} kg")
        print(f"Estatura: {estatura_usuario} m")
        print(f"IMC: {imc_calculado:.2f}")  # Formato con 2 decimales
        print(f"Interpretación: {interpretacion_imc}")
        print("=" * 30)

        # Mostrar información adicional según el resultado
        if interpretacion_imc == "Peso normal":
            mensaje_adicional = "¡Felicidades! Su peso se encuentra en el rango saludable."
        elif interpretacion_imc == "Bajo peso":
            mensaje_adicional = "Considere consultar con un profesional de la salud."
        else:
            mensaje_adicional = "Se recomienda mantener una alimentación balanceada y ejercicio regular."

        print(f"\nNota: {mensaje_adicional}")

        # Preguntar si desea calcular otro IMC
        print("\n¿Desea calcular otro IMC? (s/n): ", end="")
        respuesta_usuario = input().lower().strip()

        # Variable boolean para determinar si continuar
        continuar_programa = respuesta_usuario in ['s', 'si', 'sí', 'y', 'yes']

        if continuar_programa:
            print("\n" + "=" * 50)
        else:
            print("\n¡Gracias por usar la calculadora de IMC!")
            print("¡Hasta luego!")


# Verificar si el script se ejecuta directamente
if __name__ == "__main__":
    main()