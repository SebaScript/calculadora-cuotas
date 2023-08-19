import modelo

print("Sistema de calculo de cuotas y amortizacion para compras a crédito.\n")
print("Por favor, ingrese los valores para calcular el valor de la cuota, "
      "los intereses totales a pagar y el plan de amortización.\n")

monto = float(input("Monto total: "))
tasa = float(input("Tasa mensual: "))
cuotas = int(input("Cantidad de cuotas: "))

valor_cuota = round(modelo.cuota_mensual(monto, tasa, cuotas),2)
intereses_totales = round(modelo.interes_total(monto, tasa, cuotas),2)
plan_amortizacion = modelo.amortizacion(monto, tasa, cuotas)

print(f"\nEl valor de cada cuota será de: ${valor_cuota}\n")
print(f"Los intereses totales a pagar serán de: ${intereses_totales}\n")
print(f"Plan de amortización: \n")
print(" #  | saldo | interés |abono capital|")
for i in plan_amortizacion:
    print(i)

print("\nPor favor, ingrese los valores para calcular el efecto de un abono extra en el plan de amortización\n")
cuota = int(input("Ingrese la cuota en la que desea hacer el abono extra: "))
abono_extra = float(input("Ingrese el monto del abono extra: "))
amortizacion_abono_extra = modelo.abono_extra(plan_amortizacion, cuota, abono_extra, tasa, valor_cuota)

print("\nEl nuevo plan de amortización despues del abono extra es: \n")
print(" #  | saldo | interés |abono capital|")
for i in amortizacion_abono_extra:
    print(i)
