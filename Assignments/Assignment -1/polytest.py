from poly import Polynomial
poly = Polynomial(3,[4,7,9,1])
poly2 = Polynomial(3,[7,1,8,9])

print(poly.multiply_polynomials(poly2))

poly3 = poly-poly2
a = poly3.eval(5)
print(a)