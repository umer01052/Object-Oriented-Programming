import math

class Vector:
    def __init__(self, *args):
        self.coordinates = tuple(args)

    def magnitude(self):
        result=0
        for x in self.coordinates:
            result =result + x**2

        return math.sqrt(result)

    def dot_product(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same dimension for dot product.")

        result = 0
        for i in range(len(self.coordinates)):
            result += self.coordinates[i] * other.coordinates[i]

        return result



def main():
    # 2-dimensional vector
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1.magnitude()) 
    print (v1.dot_product(v2) )
    # 3-dimensional vector
    v3 = Vector(1, 2, 3)
    v4 = Vector(4, 5, 6)
    print (v3.magnitude()) 
    print(v3.dot_product(v4)) 

    # 4-dimensional vector
    v5 = Vector(1, 2, 3, 4)
    v6 = Vector(5, 6, 7, 8)
    print(v5.magnitude())
    print(v5.dot_product(v6)) 

    # 5-dimensional vector
    v7 = Vector(1, 2, 3, 4, 5)
    v8 = Vector(6, 7, 8, 9, 10)
    print( v7.magnitude()) 
    print(v7.dot_product(v8))

    # 1-dimensional vector (special case)
    v9 = Vector(3)
    v10 = Vector(7)
    print( v9.magnitude()) 
    print( v9.dot_product(v10)) 
   


main()
