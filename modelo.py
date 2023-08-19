import excepciones


def cuota_mensual(monto,tasa,cuotas) -> float:
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


def interes_total(monto,tasa,cuotas) -> float:
    valor_cuota = cuota_mensual(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses


def amortizacion(monto, tasa, cuotas) -> list:
    valor_cuota: float = round(cuota_mensual(monto, tasa, cuotas),2)
    saldo: float = monto
    porcentaje_interes: float = tasa/100
    tabla_amortizacion = []
    if cuotas == 1:
        numero_cuota = 1
        porcentaje_interes = 0
        abono_capital = valor_cuota - porcentaje_interes
        fila = [numero_cuota, 0, porcentaje_interes, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes: float = round(porcentaje_interes * saldo,2)
            abono_capital: float = round(valor_cuota - interes,2)
            saldo: float = round(saldo - abono_capital,2)
            if saldo < 0 > -0.1:
                saldo = 0
            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)

    return tabla_amortizacion


def abono_extra(tabla_amortizacion, cuota, abono, interes, valor_cuotas):
    if abono < valor_cuotas:
        raise excepciones.AbonoMuyBajo

    saldo_restante = tabla_amortizacion[cuota-2][1]

    if abono > saldo_restante:
        raise excepciones.AbonoMuyAlto

    porcentaje_interes = interes / 100

    tabla_amortizacion_abono_extra = []

    for i in tabla_amortizacion:
        tabla_amortizacion_abono_extra.append(i)
        if i[0] == cuota-1:
            break

    for j in range (tabla_amortizacion[cuota-1][0], tabla_amortizacion[-1][0]):
        numero_cuota = j
        interes: float = round(porcentaje_interes * saldo_restante, 2)
        if numero_cuota == tabla_amortizacion[cuota-1][0]:
            abono_capital: float = round(abono - interes, 2)
        else:
            abono_capital: float = round(valor_cuotas - interes, 2)
        saldo_restante: float = round(saldo_restante - abono_capital, 2)
        if saldo_restante == 0:
            abono_capital = tabla_amortizacion_abono_extra[-1][1]
        if saldo_restante <= 0:
            saldo_restante = 0
        fila = [numero_cuota, saldo_restante, interes, abono_capital]
        tabla_amortizacion_abono_extra.append(fila)
        if saldo_restante <= 0:
            break
    if tabla_amortizacion_abono_extra[-2][1] < tabla_amortizacion_abono_extra[-2][3]:
        tabla_amortizacion_abono_extra[-1][3] = tabla_amortizacion_abono_extra[-2][1]
    return tabla_amortizacion_abono_extra
