def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num%i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric() and int(num)>0, "Solo se pueden ingresar Numeros Positivos"
    # assert int(num)>0, "Solo puedes ingresar numeros positivos"
    print(divisors(int(num)))
    print("termino el programa")
    
if __name__ == "__main__":
    run()