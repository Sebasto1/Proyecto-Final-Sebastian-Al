#Documentacion

Web para el registro de ingreso de ventas y administracion de distribuidores pudiendo crear, eliminar y ver en detalles cada distribuidor
Cada usuario tiene su propio perfil donde puede cambiar su foto, su usuario y mail

Cuenta con multiples apps, una de ellas para el control de usuarios, otra para la seccion de ingreso de ventas y administracion, y otra que funciona como nucleo para que los templates hereden de ellos

###App users

En esta app se encuentra nucleado toda la logica de registro, de inicio de sesion, perfiles y recuperacion de contraseña
Esta app en especial lleva un modulo signals.py donde detecta que se creo un usuario y le asigna un perfil

###App home

En esta app se encuentra el template padre base.html donde heredan todos los otros templates de toda la web

###App activity

Esta app nuclea el registro de ventas y el CRUD de los distribuidores


Cada app tiene sus urls registradas en urls.py, templates heredados y sus respectivos modelos en models.py




@Sebastian Al
