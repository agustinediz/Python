#Applying f-strings to the mortgage code.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_adelanto = 1000.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo >= 0:
    if mes < pago_extra_mes_comienzo and mes > pago_extra_mes_fin:
     saldo = saldo * (1+tasa/12) - pago_mensual
     total_pagado = total_pagado + pago_mensual 
     mes = mes + 1
    elif mes >= pago_extra_mes_comienzo or mes <= pago_extra_mes_fin:
     saldo = saldo * (1+tasa/12) - pago_mensual - pago_adelanto
     total_pagado = total_pagado + pago_mensual + pago_adelanto
     mes = mes + 1
     print("Meses", mes)
     print("Total pagado", round(total_pagado, 2))
     print ("Saldo", round(saldo, 2))
     f"Para llegar a tener {round(saldo, 2)} de saldo tiene que pagar {round(total_pagado, 2)} pesos en {mes} meses"
