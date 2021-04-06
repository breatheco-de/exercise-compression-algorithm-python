# Compression Algorithm

<p align="center">
    <img height="300" src="https://raw.githubusercontent.com/breatheco-de/exercise-compression-algorithm-python/master/preview.png" />
</p>

Creemos un algoritmo de compresion ❔
Parece difícil pero es algo que puede hacer casi cualquiera persona.

## 📝 Instrucciones

Crea un algoritmo que dado un string, reemplace las palabras que iguales a las keys del **diccionario de `símbolos` o `symbols` dictionary keys** y las reemplaza con sus valores respectivos en el mismo diccionario.

```python
symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "better": '😅',
    "Although": "🥺"
}
```

Por ejemplo:

| `Although, this is a great implementation of time` | → debería conbertirse en → | `🥺, this is a great 🤯 of time` |
| -------- | ------ | -------- |

El actual proyecto tiene 3 archivos:

| Name | Description |
| -------- | ------ |
| compress.py | Contiene el algoritmo para comprimir el contenido, tiene una función "comprimir" que recibe el texto en bruto y devuelve la versión comprimida del mismo|
| decompress.py | Es muy similar a `compress.py` pero contiene el algoritmo para volver a convertir el contenido de su versión comprimida al contenido original|
| app.py | Este es un archivo de entrada y no es necesario actualizarlo, importa y usa los otros dos archivos|


## 🔢 Paso a paso

1. Tómate el tiempo para comprender el código, abre y lee el archivo `app.py` y sigue el algoritmo con tu mente, revisa los archivos compress.py y decompress.py para comprender dónde debe implementarse su solución.
2. Ejecuta app.py escribiendo `python3 app.py` y comprende su resultado y por qué.
3. Edita compress.py para crear el algoritmo de ** compression **.
4. Prueba tu algoritmo de compression ejecutando app.py nuevamente.
5. Edite decompress.py para crear el algoritmo de ** decompression **.
6. Prueba tu algoritmo de decompresssion ejecutando app.py nuevamente.

## 🌱  Cómo iniciar este proyecto

1. Este proyecto viene con los archivos necesarios para empezar a trabajar, pero tienes dos opciones para empezar:

a) Abrir este link con Gitpod en tu navegador: https://gitpod.io#https://github.com/breatheco-de/exercise-compression-algorithm-python.git

b) Clonar este repositorio localmente en tu computador:
```sh
$ git clone https://github.com/breatheco-de/exercise-compression-algorithm-python.git
````
2. Escribe el siguiente comando en la terminal:
```bash
python3 app.py
```
Deberías obtener una respuesta similar a esta:
```bash
✅No data lost.
document.txt has 824 size, compressed.txt has 768 size, compression of 7% in 0.0003972053527832031 seconds 
````

## 🎯 Métricas

1. Potencia de compresión: el ratio es la relación entre la cantidad sin comprimir y la cantidad comprimida. 
2. Sin pérdida de datos: si comprimimos y descomprimimos document.txt, el resultado debería ser el string de contenido original.

## 🍩🍬🍭 ¿Te sientes seguro?

Añadiendo más palabras al dicionario  de `símbolos, puede conseguir más potencia de compresión.

Intenta volver a hacer el algoritmo para lograr una potencia de compresión superior al 15% sin pérdida de datos sin agregar más palabras.
