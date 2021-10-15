# Defining Function
def f(x):
    return 2*x**3 - 4*x**2 - 24

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.5f and f(x2) = %0.5f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nAkar Penyelesaian : %0.5f' % x2)


# Input Section
x0 = input('Dugaan awal: ')
x1 = input('Duganaan akhir: ')
e = input('Toleransi Eror: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('dugaan awal: '))
# x1 = float(input('dugaan akhir: '))
# e = float(input('Toleransi Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)
