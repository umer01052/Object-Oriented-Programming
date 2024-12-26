class Polynomial:

    def __init__(self,degree,coefficients):
        self.__degree = degree
        self.__coefficients = coefficients
        self.exponents = [i for i in range(degree,-1,-1)]
        

    
    @property
    def degree(self):
        return self.__degree
    
    @degree.setter
    def degree(self,x):
        self.__degree = x

    @property
    def coefficients(self):
        return self.__coefficients
    
    @coefficients.setter
    def coefficients(self,x):
        self.__coefficients = x

    def __add__(self,other):
        trms = []
        for i in range(len(self.__coefficients)):
            trms.append(self.__coefficients[i]+ other.__coefficients[i])
            

        return Polynomial(self.__degree,trms)
    
    def __sub__(self,other):
        trms = []
        for i in range(len(self.__coefficients)):
            trms.append(self.__coefficients[i]- other.__coefficients[i])
        return Polynomial(self.__degree,trms)

   
    def eval(self,e):
        a = []
        for i in range(len(self.__coefficients)):
            a.append(self.__coefficients[i] * (e**self.exponents[i]))
        result = 0
        for i in range (len(a)):
            result += a[i]
        print("After putt the valu",e,"result is: ",end = " ")
        return result
    def multiply_polynomials(poly1, poly2):
        max_degree = poly1.degree + poly2.degree
        result_coefficients = [0] * (max_degree + 1)

        for i in range(poly1.degree + 1):
            for j in range(poly2.degree + 1):
                result_coefficients[i + j] += poly1.coefficients[i] * poly2.coefficients[j]

        return Polynomial(max_degree, result_coefficients)
    
                     
        
            


    def __str__(self) -> str:
        s = ''
        handl_plus = 1

        for i,j in zip(self.__coefficients,self.exponents):
            s += f'{i}x^{j}'
            if len(self.__coefficients) != handl_plus:
                s+= " + "
                handl_plus +=1
        return s
           




        


        
    
