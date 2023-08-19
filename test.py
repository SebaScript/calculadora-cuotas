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
        cuotas = 60
        self.assertRaises(excepciones.MontoNulo, modelo.cuota_mensual, monto, tasa, cuotas)

    def testCuotasNegativas(self):
        monto = 2
        tasa = 3.1
        cuotas = -2
        self.assertRaises(excepciones.CuotaNegativa, modelo.cuota_mensual, monto, tasa, cuotas)

    def testAmortizacion(self):
        monto = 200000
        tasa = 3.10
        cuotas = 36
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = tabla[-1]
        self.assertListEqual(resultado, [36, 0, 279.57, 9018.39])

    def testAmortizacion2(self):
        monto = 850000
        tasa = 3.40
        cuotas = 24
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = tabla[-1]
        self.assertListEqual(resultado, [24, 0, 1722.28, 50655.22])

    def testAmortizacionCuotaUnica(self):
        monto = 90000
        tasa = 2.40
        cuotas = 1
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = tabla[-1]
        self.assertListEqual(resultado, [1, 0, 0, 90000])

    def testAmortizacionTasaCero(self):
        monto = 480000
        tasa = 0
        cuotas = 48
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = tabla[-1]
        self.assertListEqual(resultado, [48, 0, 0, 10000])

    def testAmortizacionAbonoExtra(self):
        monto = 200000
        tasa = 3.10
        cuotas = 36
        cuota_abono_extra = 10
        abono_extra = 53000
        valor_cuotas: float = round(modelo.cuota_mensual(monto, tasa, cuotas), 2)
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = modelo.abono_extra(tabla, cuota_abono_extra, abono_extra, tasa, valor_cuotas)
        resultado = resultado[-1]
        self.assertListEqual(resultado, [27, 0, 238.20, 7683.92])

    def testAmortizacionAbonoExtra2(self):
        monto = 850000
        tasa = 3.40
        cuotas = 24
        cuota_abono_extra = 5
        abono_extra = 90000
        valor_cuotas: float = round(modelo.cuota_mensual(monto, tasa, cuotas), 2)
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        resultado = modelo.abono_extra(tabla, cuota_abono_extra, abono_extra, tasa, valor_cuotas)
        resultado = resultado[-1]
        self.assertListEqual(resultado, [23, 0, 1129.65, 33225.06])

    def testAmortizacionAbonoExtraBajo(self):
        monto = 850000
        tasa = 3.40
        cuotas = 24
        cuota_abono_extra = 10
        abono_extra = 45000
        valor_cuotas: float = round(modelo.cuota_mensual(monto, tasa, cuotas), 2)
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        self.assertRaises(excepciones.AbonoMuyBajo, modelo.abono_extra, tabla, cuota_abono_extra, abono_extra, tasa, valor_cuotas)

    def testAmortizacionAbonoExtraSuperior(self):
        monto = 850000
        tasa = 3.40
        cuotas = 24
        cuota_abono_extra = 22
        abono_extra = 180000
        valor_cuotas: float = round(modelo.cuota_mensual(monto, tasa, cuotas), 2)
        tabla = modelo.amortizacion(monto, tasa, cuotas)
        self.assertRaises(excepciones.AbonoMuyAlto, modelo.abono_extra, tabla, cuota_abono_extra, abono_extra, tasa, valor_cuotas)
