class Solution(object):
    #Creamos una función llamada isPalindrome para cada vez que se quiera validar un caso.
    def isPalindrome(self, x): #self para hacer referencia al objeto cuando llamamos al método y x(integer) como parámetro.
        """
        :type x: int
        :rtype: bool
        """
        #Transformamos x en un dato tipo string para usar un recorrido como herramienta de validación.
        x = str(x) 
        #Usando condicionales, revisamos SI el valor de x es igual que x recorrido desde el final hasta el inicio o NO.
        if x == x[::-1]:
            return True 
        else: 
            return False 
    
#Usamos un try and except para validaciones, en este caso,  para los valores ingresados por teclado.
try: 
    #Al crear una instancia de la clase dentro de una variable, evitamos que, cambios que hagamos, se guarden en la clase global y así podamos darle usos personalizados.
    solution = Solution() 
    #Solicitamos el número.
    x = int(input("Ingrese un número: "))
    #Llamamos la función
    print(solution.isPalindrome(x))
except ValueError:
    print("Ingreso inválido. Debe ser un número!")