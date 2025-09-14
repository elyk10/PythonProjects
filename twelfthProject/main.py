def fibonacci(n):
    if n == 1:
        
        return 0
    elif n ==2:
        
        return 1
    
    value = fibonacci(n-1) + fibonacci(n-2)
    return value

def main():

    print(fibonacci(6))

main()