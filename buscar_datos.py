import unittest

def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        for k, v in value.items():
            if v in args:
                return key
    return None

database = {
    "per1": {
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    "per2": {
        "nombre1": "Elio",
        "apellido1": "Anci"
    },
    "per3": {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    }
}

nombre = input("Ingrese el dato a buscar: ")

resultado = buscar_datos(nombre, **database)
if resultado:
    print(f"La persona se encuentra en la base de datos con el id: {resultado}")
else:
    print("La persona no se encuentra en la base de datos.")


class TestBuscarDatos(unittest.TestCase):
    def test_Pablo(self):
        resultado = buscar_datos("Pablo", **database)
        self.assertEqual (resultado, "per1")

    def test_Ruiz(self):
        resultado = buscar_datos("Ruiz", **database)
        self.assertEqual (resultado, "per1")

    def test_Diego(self):
        resultado = buscar_datos("Diego", **database)
        self.assertEqual (resultado, "per1")

    def test_Picasso(self):
        resultado = buscar_datos("Picasso", **database)
        self.assertEqual (resultado, "per1")

    def test_Elio(self):
        resultado = buscar_datos("Elio", **database)
        self.assertEqual (resultado, "per2")

    def test_Anci(self):
        resultado = buscar_datos("Anci", **database)
        self.assertEqual (resultado, "per2")

    def test_Elias(self):
        resultado = buscar_datos("Elias", **database)
        self.assertEqual (resultado, "per3")

    def test_Luciano(self):
        resultado = buscar_datos("Luciano", **database)
        self.assertEqual (resultado, "per3")

    def test_Marcelo(self):
        resultado = buscar_datos("Marcelo", **database)
        self.assertEqual (resultado, "per3")

    def test_Martin(self):
        resultado = buscar_datos("Martin", **database)
        self.assertEqual (resultado, None)
unittest.main()