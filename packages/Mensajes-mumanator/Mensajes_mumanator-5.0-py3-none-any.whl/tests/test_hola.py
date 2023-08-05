# import Saludos este es para importar todo el script
# from Saludos import saludar si tenemos más definiciones podemos agregarlas con comas
# from Saludos import saludar, Saludo
# from Saludos import * para importar todas las funciones o clases del módulo

import unittest
import numpy as np
from Mensajes.hola.Saludos import generar_array

class PruebasHola(unittest.TestCase):
    def test_generar_array(self):
        np.testing.assert_array_equal(
            np.array([0,1,2,3,4,5]),
            generar_array(6)
        )



# from Mensajes.hola.Saludos import *
# from Mensajes.adios.despedida import *

# Saludos.saludar()
# saludar()
# Saludo()

# despedir()
# Despedida()

