import math

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def calcular_precio(total: int, porcentaje_descuento: int):
    descuento = (total * porcentaje_descuento) / 100
    precio_final = total - descuento
    return math.trunc(precio_final)


@app.route('/ejercicioUno', methods=['GET', 'POST'])
def ejercicioUno():
    if request.method == 'POST':
        # Procesar los datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        ctadTarrosPintura = int(request.form['ctadTarrosPintura'])

        precioTarroPintura = 9000

        if 18 <= edad <= 30:
            precioTotal = ctadTarrosPintura * precioTarroPintura
            dcto = 15
            precioDctoTotal = calcular_precio(precioTotal, dcto)
            montoDcto = precioTotal - precioDctoTotal

            mensajeNombre = f'Nombre del cliente: {nombre}.'
            mensajeTotalSinDcto = f'Total sin descuento: {precioTotal}.'
            mensajeMontoDcto = f'El descuento es de: {montoDcto}.'
            mensajeTotalPagar = f'El total a pagar es de: {precioDctoTotal}.'
            return render_template('ejercicioUno.html', mensajeNombre=mensajeNombre, mensajeTotalSinDcto=mensajeTotalSinDcto, mensajeMontoDcto=mensajeMontoDcto, mensajeTotalPagar=mensajeTotalPagar)
        elif edad > 30:
            precioTotal = ctadTarrosPintura * precioTarroPintura
            dcto = 25
            precioDctoTotal = calcular_precio(precioTotal, dcto)
            montoDcto = precioTotal - precioDctoTotal

            mensajeNombre = f'Nombre del cliente: {nombre}.'
            mensajeTotalSinDcto = f'Total sin descuento: {precioTotal}.'
            mensajeMontoDcto = f'El descuento es de: {montoDcto}.'
            mensajeTotalPagar = f'El total a pagar es de: {precioDctoTotal}.'
            return render_template('ejercicioUno.html', mensajeNombre=mensajeNombre, mensajeTotalSinDcto=mensajeTotalSinDcto, mensajeMontoDcto=mensajeMontoDcto, mensajeTotalPagar=mensajeTotalPagar)
        else:
            precioTotal = ctadTarrosPintura * precioTarroPintura
            dcto = 0
            precioDctoTotal = calcular_precio(precioTotal, dcto)
            montoDcto = precioTotal - precioDctoTotal

            mensajeNombre = f'Nombre del cliente: {nombre}.'
            mensajeTotalSinDcto = f'Total sin descuento: {precioTotal}.'
            mensajeMontoDcto = f'El descuento es de: {montoDcto}.'
            mensajeTotalPagar = f'El total a pagar es de: {precioDctoTotal}.'
            return render_template('ejercicioUno.html', mensajeNombre=mensajeNombre, mensajeTotalSinDcto=mensajeTotalSinDcto, mensajeMontoDcto=mensajeMontoDcto, mensajeTotalPagar=mensajeTotalPagar)
    return render_template('ejercicioUno.html')


@app.route('/ejercicioDos', methods=['GET', 'POST'])
def ejercicio_dos():
    userUno = {
        "nombre": "juan",
        "contrasena" : "admin"
    }

    userDos = {
        "nombre": "pepe",
        "contrasena" : "user"
    }

    if request.method == 'POST':
        # Procesar los datos del formulario
        user = request.form['nombre']
        clave = str(request.form['clave'])

        if user == userUno["nombre"] and clave == userUno["contrasena"]:
            mensajeBienvenida = f'Bienvenido administrador {userUno["nombre"]}.'
            return render_template('ejercicioDos.html', mensajeBienvenida=mensajeBienvenida)
        elif user == userDos["nombre"] and clave == userDos["contrasena"]:
            mensajeBienvenida = f'Bienvenido user {userDos["nombre"]}.'
            return render_template('ejercicioDos.html', mensajeBienvenida=mensajeBienvenida)
        else:
            mensajeBienvenida = f'Usuario o contraseña incorrectos.'
            return render_template('ejercicioDos.html', mensajeBienvenida=mensajeBienvenida)

    return render_template('ejercicioDos.html')


if __name__ == '__main__':
    app.run()