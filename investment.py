    amount = float(input('enter amount: '))
    inrate = float(input('enter interest rate: '))
    period = float(input('enter period: '))
    value = 0
    year = 1                                                                    
    while year <= period:
        value = amount + inrate * amount
        print('year {} Rs.{:.2f} '.format(year,value))
        year = year + 1
