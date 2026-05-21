# Laboratorio de Testing

## Primera Parte - pytest, selenium

En esta ocacion realizamos un entorno de pruebas el cual estara documetnado a traves de la herramienta de reportes proporcionada por pytest, para ello en nuestra carpeta reports, encontramos los reportes generados en HTML, para este primer ejercicio, encontramos el reporte en el documento [Reporte_Selenium](./reports/report.html)

Cada uno de los test se encuentran declarados en la carpeta tests, mas especificamente en [Test_Selenium](./tests/test_search.py)

Los test estan relacionados en primer lugar a la comprension de como un test es aplicado a la valoracion de ciertos elementos dentro del aplicativo, este test valida la informacion del titulo del aplicativo [saucedemo](https://www.saucedemo.com/) 

El segundo test hace referencia a la validacion de un usuario y su correcto ingreso y redireccionamiento al index del aplicativo, la prueba del correcto funcionamiento esta en el reporte anteriormente mencionado, sin embargo a contiunuacion se presenta una imagen con el resultado 

![alt text](./img/image-1.png)

Estas pruebas se realizan en un entorno controlado en Chrome gracias a pytest

## Segunda parte - Cypress