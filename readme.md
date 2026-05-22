# Laboratorio de Testing

## Primera Parte - pytest, selenium

En esta ocacion realizamos un entorno de pruebas el cual estara documetnado a traves de la herramienta de reportes proporcionada por pytest, para ello en nuestra carpeta reports, encontramos los reportes generados en HTML, para este primer ejercicio, encontramos el reporte en el documento [Reporte_Selenium](./reports/report.html)

Cada uno de los test se encuentran declarados en la carpeta tests, mas especificamente en [Test_Selenium](./tests/test_search.py)

Los test estan relacionados en primer lugar a la comprension de como un test es aplicado a la valoracion de ciertos elementos dentro del aplicativo, este test valida la informacion del titulo del aplicativo [saucedemo](https://www.saucedemo.com/) 

El segundo test hace referencia a la validacion de un usuario y su correcto ingreso y redireccionamiento al index del aplicativo, la prueba del correcto funcionamiento esta en el reporte anteriormente mencionado, sin embargo a contiunuacion se presenta una imagen con el resultado 

![reporte de testeo](./img/image-1.png)

Estas pruebas se realizan en un entorno controlado en Chrome gracias a pytest

## Segunda parte - Cypress

En lo que respecta a cypress en cierto modo podemos decir que hace lo mismo que selenium, realiza pruebas automatizadas de software en aplicativos web, al ser entornos web, podemos identificar rapidamente que esta fundamentado en JavaScript, para iniciar, es necesario generar el entorno que nos permita ejecutar JS es por esto que inicializamos npm, posteriormente realizamos la instalacion de cypress, todo esto lo hacemos con los siguientes comandos:

`npm init -y`
`npm install cypress --save-dev`

ahora inicalizarmeos cypress con el comando `npx cypress open`, una vez inicializado cypress veremos la siguiente pantalla

![imagen cypress apenas se inicia el servicio](./img/Cypress.png)

luego de esto nos pregunta que tipo de test realizarmos, en nuestro caso como estamos testeando el comportamiento de un usuario real de extremo a extremo (E2E), escogeremos dicha opcion.

![seleccion tipo de test](./img/e2e_cypress.png)

y por ultimo nos solicitar el motor de busqueda/browser que deseemos usar, en mi caso usare Chrome

![seleccion browser](./img/browser_cypress.png)

al inicializar el test veremos que en Chrome el aplicativo perteneciente al servicio cypress fundamenta 4 moculos, nosotros para la realizacionde los respectivos tests, usaremso los 'Specs' que en palabras sencillas son los tests personalizables, como se muestra en la imagen anterior.

En nuestro caso se realizaron 2 tests el primero relacionado al login el cual se encuentra en [test_login](./cypress/e2e/login.cy.js) este test basicamente captura cada uno de los elementos establecidos en la interfaz del login y en cada campo establece elementos previamente estipulados, adicionalmente realiza el submit respectivo y en caso tal de ser redireccionado al index del aplicativo en cuestion, el test es aprobado.

![test aprobado](./img/test-cypress-ok.png)

el otro test simplemente es el test por defecto que la creacionde un nuevo spect el cual es aprobado cuando se visita la pagina de ejemplo de cypress.

## Tercera parte - JMeter

A pesar de que en el taller original se establecia Load Runner como herramienta para la simulacion de muchos usuarios accesdiendo al aplicativo, este tiene una capa algo limitada, buscando en internet encontramos una alternativa que permite realizar la misma practica y es mas amigable con los usuarios que hasta ahora estan empezando en el mundo del teasting y esta es JMeter, para mas informacion [JMeter](https://jmeter.apache.org/)

Realizamos la descarga del software, dentro de la carpeta del software entramos en el directorio 'bin' y ejecutamos el archivo 'jmeter.bat' y una vez corriendo, el programa se vera algo asi.

![Jmeter](./img/Jmeter_Interface.png)

ahora realizaremos nuestro primer test con 10 usuarios a la pagina [sourcedemo.com](https://www.saucedemo.com)

En Jmeter se usa el concepto de Thread Group, el cual representa la cantidad e usuarios simultaneos que la pagina testeada soportara, para crear estos grupso iremos la siguiente opcion:

![creation thread group](./img/Jmeter_add_thread.png)

Una vez creado el grupo, realizamos la configuracion del grupo, en donde lanzaremso peticiones HTTP referentes a la visita del sitio en cuestion.

![configuracion del thread group](./img/Jmeter_conf_test.png)

ahora mencionaremos a que pagina visitaremos a traves de las peticiones HTTP 

adicionalmente necesitamos ciertas pestañas donde visualizar los resultados arrojados al momento de hacer el test, estos elementos seran 