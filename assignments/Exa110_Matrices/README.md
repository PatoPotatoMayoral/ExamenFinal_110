![Tec de Monterrey](../../images/logotecmty.png)
# Multuplica matriz por constante

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():  
  pass

if __name__ == '__main__':
    main()
```

<h3>Multiplica matriz por constante</h3>
Desarrolla la función leer_matriz para leer la matriz, la cual recibe el número de renglones (num_ren). 
En la función se deberán pedir los renglones, cada renglon que se solicita tiene el siguiente formato: 
12-5-1, es decir cada uno de los números va separado por un "-". La función debe regresar la matriz con los números en string. <br>

Desarrolla la función convierte_matriz_enteros para convertir los numeros (string) a enteros, la función recibe como parámetro de entrada la matriz con los datos y regresa la matriz ya con los números enteros (int) <br>

Desarrolla la función multiplica_constante que recibe una matriz de enteros y una constante, la función debe regresar la matriz con cada uno de sus elementos multiplicado por la constante <br>

El programa deberá:<br>
1.- Solicitar la cantidad de renglones<br>
2.- Solicitar la constante<br>
3.- Llamar la función leer_matriz  (el usuario ingresa los renglones correspondientes)<br>
4.- Llamar a la función convierte_matriz_enteros <br>
5.- Imprimir la matriz de enteros "print (matriz)" <br>
6.- Llamar a la función multiplica_constante <br>
7.- Imprimir la matriz con cada uno de los elementos multiplicado por la constante  "print (matriz)" <br>



Entrada <br>
Número de renglones de la matriz <br>
Constante (por la cual será multiplicado cada elemento de la matriz)<br>
Los datos de la matriz que son renglones separados por un "-" <br>

Salida<br>
Una matriz con los enteros ingresados<br>
Una matriz con sus elementos multiplicados por la constante<br>

Ejemplo1 de ejecución del programa:<br>
```
3   <--- cantidad de renglones o filas 
2   <--- constante 
3-4-5  <--- cada uno de los renglones
5-6-4
2-10-9        
[[3, 4, 5], [5, 6, 4], [2, 10, 9]]   <--- Matriz con los números enteros
[[6, 8, 10], [10, 12, 8], [4, 20, 18]]  <--- Matriz con los números multiplicados por la constante (2) 
```

Ejemplo2 de ejecución del programa:<br>
```
2
5
6-7-5-4
9-8-10-11
[[6, 7, 5, 4], [9, 8, 10, 11]]
[[30, 35, 25, 20], [45, 40, 50, 55]]
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.
NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

