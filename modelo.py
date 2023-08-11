import excepciones


def cuota_mensual(monto,tasa,cuotas):
    p = tasa/100
    if monto == 0:
        raise excepciones.MontoNulo
    elif tasa*12 > 100:
        raise excepciones.Usura
    elif cuotas <= 0:
        raise excepciones.CuotaNegativa
    elif cuotas == 1:
        return monto
    elif tasa == 0:
        return monto/cuotas
    else:
        return (monto * p)/(1 - (1 + p)**(-cuotas))


def interes_total(monto,tasa,cuotas):
    valor_cuota = cuota_mensual(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses


def amortizacion(monto, tasa, cuotas):
    valor_cuota = cuota_mensual(monto, tasa, cuotas)
    print(valor_cuota)
    saldo = monto
    interes_total=tasa/100
    tabla_amortizacion = [["Cuota", "Saldo", "Pago interés", "Abono capital"], ["#", valor_cuota, tasa, monto]]
    if cuotas == 1:
        numero_cuota = 1
        interes_total = 0
        abono_capital = round(valor_cuota - interes_total, 2)
        fila = [numero_cuota, saldo, interes_total, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes = round(interes_total * saldo, 2)
            abono_capital = round(valor_cuota - interes,2)
            saldo = round(saldo - abono_capital,2)

            fila = [numero_cuota, saldo, interes, abono_capital]
            if fila[1] < 0:
                fila[1] = 0
            tabla_amortizacion.append(fila)
            print(fila)

    return tabla_amortizacion


monto = 200000
cuotas = 36
tasa_interes = 3.10

print(amortizacion(monto, tasa_interes, cuotas))
