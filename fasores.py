import numpy as np

def fasor_to_scalar(mode,x=0,y=0):
    
    if(mode == 3):    
        real = x * np.cos(y*np.pi/180)
        imag = x * np.sin(y*np.pi/180)   
        return(f"{real} + j {imag}")
        
        
    print("x∠y\n")
    
    x = float(input("x = "))
    y = float(input("y = "))
    
    real = x * np.cos(y*np.pi/180)
    imag = x * np.sin(y*np.pi/180)
    
    if(mode == 1):       
        print(f"{real} + j {imag}")
        
    if(mode == 2):
        return complex(real, imag)
        
def scalar_to_fasor(mode, x=0, y=0):
    if(mode == 3):
        mod = np.sqrt(x**2 + y**2)
        ang = np.arctan(y/x) * 180/np.pi
        return f"{mod} ∠ {ang}°"
        
    print("x + j * y\n")
    
    x = float(input("x = "))
    y = float(input("y = "))
    
    mod = np.sqrt(x**2 + y**2)
    ang = np.arctan(y/x) * 180/np.pi
    
    if(mode == 1):    
        print(f"{mod} ∠ {ang}°")
    if(mode == 2):
        return [mod, ang]
        
def complex_sum():
    num_type = int(input("Tipo do num1:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        num1 = fasor_to_scalar(mode=2)
    elif(num_type == 2):
        print("x + j * y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = complex(x,y)
    
    num_type = int(input("Tipo do num2:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        num2 = fasor_to_scalar(mode=2)
    elif(num_type == 2):
        print("aaaaaaaaaaa\nx + j * y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = complex(x,y)
        
    result = num1 + num2
    
    print(f"Forma complexa: {result.real} + j {result.imag}\nForma fasorial: {scalar_to_fasor(mode=3,x=result.real, y=result.imag)}")
    
def complex_sub():
    num_type = int(input("Tipo do num1:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        num1 = fasor_to_scalar(mode=2)
    elif(num_type == 2):
        print("x + j * y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = complex(x,y)
    
    num_type = int(input("Tipo do num2:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        num2 = fasor_to_scalar(mode=2)
    elif(num_type == 2):
        print("aaaaaaaaaaa\nx + j * y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = complex(x,y)
        
    sub = num1 - num2
    
    print(f"Forma complexa: {sub.real} + j {sub.imag}\nForma fasorial: {scalar_to_fasor(mode=3,x=sub.real, y=sub.imag)}")

def complex_mult():
    num_type = int(input("Tipo do num1:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        print("x∠y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = [x, y]
    elif(num_type == 2):
        num1 = scalar_to_fasor(mode=2)
    
    num_type = int(input("Tipo do num2:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        print("x∠y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = [x, y]
    elif(num_type == 2):
        num2 = scalar_to_fasor(mode=2)
    
    res_mod = num1[0] * num2[0]
    res_ang = num1[1] + num2[1]
    
    print(f"Forma complexa: {fasor_to_scalar(mode=3, x=res_mod, y=res_ang)}\nForma fasorial: {res_mod} ∠ {res_ang}°")

def complex_div():
    num_type = int(input("Tipo do num1:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        print("x∠y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = [x, y]
    elif(num_type == 2):
        num1 = scalar_to_fasor(mode=2)
    
    num_type = int(input("Tipo do num2:\n[1]fasor\n[2]complex\n>> "))    
    if(num_type == 1):
        print("x∠y\n")    
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = [x, y]
    elif(num_type == 2):
        num2 = scalar_to_fasor(mode=2)
    
    res_mod = num1[0] / num2[0]
    res_ang = num1[1] - num2[1]
    
    print(f"Forma complexa: {fasor_to_scalar(mode=3, x=res_mod, y=res_ang)}\nForma fasorial: {res_mod} ∠ {res_ang}°")
    

while True:
    op = int(input("Tipo de operação:\n[1]fasor -> escalar\n[2]escalar -> fasor\n[3]Soma\n[4]Subtração\n[5]Multiplicação\n[6]Divisão\n>> "))
    if(op > 0 or op < 7 and type(op) == int): break

if op == 1:
    fasor_to_scalar(mode=1)
elif op == 2:
    scalar_to_fasor(mode=1)
elif op == 3:
    complex_sum()
elif op == 4:
    complex_sub()
elif op == 5:
    complex_mult()
elif op == 6:
    complex_div()