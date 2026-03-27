Instrucciones

En este ejercicio, debe implementar algunas reglas de Pac-Man , el clásico juego de arcade de la década de 1980.

Tienes cuatro reglas para implementar, todas relacionadas con los estados del juego.

No se preocupe por cómo se derivan los argumentos, solo concéntrese en combinar los argumentos para obtener el resultado deseado.

Tarea 1.- Definir si Pac-Man se come un fantasma

Defina la función eat_ghost(), que toma dos parámetros ( si Pac-Man tiene una pastilla de energía activa y si Pac-Man está tocando un fantasma ) y devuelve un valor booleano si Pac-Man puede comerse el fantasma. La función debería volver True solo si Pac-Man tiene una pastilla de energía activa y está tocando un fantasma.

 

Tarea 2.- Definir si Pac-Man anota puntos

Defina la función score(), que toma dos parámetros ( si Pac-Man está tocando una bolita de energía y si Pac-Man está tocando un punto ) y devuelve un valor booleano si Pac-Man anotó. La función debería volver True, si Pac-Man está tocando una bolita de energía o un punto.

 

Tarea 3.- Definir si Pac-Man pierde

Defina la función lose(), que toma dos parámetros ( si Pac-Man tiene una pastilla de energía activa y si Pac-Man está tocando un fantasma ) y devuelve un valor booleano si Pac-Man pierde. La función debería volver True, si Pac-Man está tocando un fantasma y no tiene una pastilla de energía activa.


Tarea 4.- Definir si Pac-Man gana

Defina la función win(), que toma tres parámetros ( si Pac-Man se ha comido todos los puntos, si Pac-Man tiene una pastilla de energía activa y si Pac-Man está tocando un fantasma ) y devuelve un valor booleano si Pac-Man gana. La función debería regresar True, si Pac-Man se ha comido todos los puntos y no ha perdido según los parámetros definidos en la parte 3.
