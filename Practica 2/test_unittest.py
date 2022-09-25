### MASTER DE PROGRAMACIÓN AVANZADA EN PYTHON
### ASIGNATURA. BUENAS PRÁCTICAS CON PYTHON
### ACTIVIDAD LECCION 2. DESARROLLO DE CÓDIGO GUIADO POR PRUEBAS
### AUTOR: JESÚS GUTIÉRREZ CONTRERAS
#############################################################################################



######################################## UNITTEST ###########################################

import unittest
import funciones

class PruebasTestUnitarias (unittest.TestCase):

    def test_multiplica_numeros(self):
        self.assertEqual(funciones.multiplica_numeros(8,5),40)

    def test_numero_primo(self):
        self.assertEqual(funciones.numero_primo(7),True)
                
    def test_longitud_palabra(self):
        self.assertEqual(funciones.longitud_palabra("python"),6)

    def test_comprueba_arroba_email(self):
        self.assertNotEqual(funciones.comprueba_arroba_email("email@test.com"),-1)

    def test_comprobar_DNI(self):
        self.assertEqual(funciones.comprobar_DNI(52922687),"D")


if __name__ == "__main":
    unittest.main()