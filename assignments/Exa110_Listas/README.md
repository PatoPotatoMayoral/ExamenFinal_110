![Tec de Monterrey](../../images/logotecmty.png)
# Listas, potencias
### Tema Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  pass

if __name__ == '__main__':
    main()
```

Escribe un programa que primero lea la cantidad de elementos que vas a ingresar en la lista y después acepte cada uno de los elementos. Todos los datos que se ingresan deben ser números enteros y meterlos en una lista. 
Si la cantidad de elementos es cero o menor, se debe mostrar el mensaje de "Error".

Posteriormente, el programa debe revisar la lista, y para cada uno de los valores pares que encuentre debe elvarlos al cuadrado y para los números impares los debe elevar al cubo. 

## Entrada
Un número entero que representa la cantidad de valores que tiene la lista, asi como cada uno de los valores de la lista.

## Salida
Una lista con los valores elevados a la potencia respectiva (según el requerimiento)
## Ejemplo1 de ejecución del programa:
### Entrada
```
0
```
### Salida
```
Error
```

## Ejemplo2 de ejecución del programa:
### Entrada
```
3
2
3
4
```
### Salida
```
[4, 27, 16]
```

No uses letreros para pedir los datos. 

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
