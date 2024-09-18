def binario_a_decimal(binario):
    decimal = 0
    # Recorremos cada dígito del número binario
    for i, digito in enumerate(reversed(binario)):
        if digito == '1':
            decimal += 2 ** i
    return decimal

# Ejemplo de uso
print(binario_a_decimal('1010'))  # Resultado esperado: 10
