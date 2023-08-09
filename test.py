import unittest
import modelo
import excepciones


class Test(unittest.TestCase):
    def testCuota(self):
        monto = 200000
        cuotas = 36
        tasa_interes = 3.1
        resultado = round(modelo.cuota_mensual(monto, tasa_interes, cuotas),2)
        esperado = 9297.96
        self.assertEqual(resultado, esperado)

    def testInteres(self):
        monto = 200000
        cuotas = 36
        tasa_interes = 3.1
        resultado = round(modelo.interes_total(monto, tasa_interes, cuotas),2)
        esperado = 134726.53
        self.assertEqual(resultado, esperado)

    def testInteres2(self):
        monto = 850000
        cuotas = 24
        tasa_interes = 3.4
        resultado = round(modelo.interes_total(monto, tasa_interes, cuotas),2)
        esperado = 407059.97
        self.assertEqual(resultado, esperado)

    def testNoInteres(self):
        monto = 480000
        tasa = 0
        cuotas = 48
        resultado = round(modelo.interes_total(monto, tasa, cuotas), 2)
        esperado = 0
        self.assertEqual(resultado, esperado)

    def testUsura(self):
        monto = 50000
        tasa = 12.4
        cuotas = 48
        self.assertRaises(excepciones.Usura, modelo.cuota_mensual, monto, tasa, cuotas)

    def testUnaCuota(self):
        monto = 90000
        tasa = 2.4
        cuotas = 1
        resultado = round(modelo.interes_total(monto, tasa, cuotas), 2)
        esperado = 0
        self.assertEqual(resultado, esperado)

    def testNoMonto(self):
        monto = 0
        tasa = 2.4
        cuotas = 0
        self.assertRaises(excepciones.MontoNulo, modelo.cuota_mensual, monto, tasa, cuotas)

    def testCuotasNegativas(self):
        monto = 2
        tasa = 3.1
        cuotas = -2
        self.assertRaises(excepciones.CuotaNegativa, modelo.cuota_mensual, monto, tasa, cuotas)

    def testAmortizacion(self):
        monto = 200000
        cuotas = 36
        tasa_interes = 3.1
        resultado = round()
        self.assertEqual()
