# Defining Function
def f(x):
    return 2*(x**3) - 4*(x**2) - 24

# Defining derivative of function
def g(x):
    return 6*(x**2) - 8*x

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nAkar Penyelesaian: %0.8f' % x1)
    else:
        print('\nTidak Konvergen.')


# Input Section
x0 = input('Tebakan awal: ')
e = input('Toleransi Eror: ')
N = input('Langkah Maximum: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Tebakan Awal: '))
# e = float(input('Toleransi Eror: '))
# N = int(input('Nilai Maximum: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)
