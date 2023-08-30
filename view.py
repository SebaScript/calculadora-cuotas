from model import CalcPayment


class Menu:
    print("Sistema de calculo de cuotas y amortizacion para compras a crédito.\n")
    print("Por favor, ingrese los valores para calcular el valor de la cuota, "
          "los intereses totales a pagar y el plan de amortización.\n")

    amount = float(input("Monto total: "))
    interest_rate = float(input("Tasa mensual: "))
    number_of_payments = int(input("Cantidad de cuotas: "))

    calc = CalcPayment(amount, interest_rate, number_of_payments)

    payment_value = round(calc.calc_monthly_payment(), 2)
    total_interests = round(calc.calc_total_interest(), 2)
    amortization = calc.amortization()

    print(f"\nEl valor de cada cuota será de: ${payment_value}\n")
    print(f"Los intereses totales a pagar serán de: ${total_interests}\n")
    print(f"Plan de amortización: \n")
    print(" #  | saldo | interés |abono capital|")
    for i in amortization:
        print(i)

    print("\nPor favor, ingrese los valores para calcular el efecto de un abono extra en el plan de amortización\n")
    installment_of_extra_payment = int(input("Ingrese la cuota en la que desea hacer el abono extra: "))
    extra_payment = float(input("Ingrese el monto del abono extra: "))
    amortization_with_extra_payment = calc.calc_extra_payment(extra_payment, installment_of_extra_payment)

    print("\nEl nuevo plan de amortización despues del abono extra es: \n")
    print(" #  | saldo | interés |abono capital|")
    for payment in amortization_with_extra_payment:
        print(payment)


menu = Menu()
