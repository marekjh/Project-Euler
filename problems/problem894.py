from sympy import *
import numpy as np

alpha, theta, l = symbols("alpha, theta, l")
eqn1 = Eq(l**2 - 2*l**2*alpha*cos(theta) + l**2*alpha**2, (alpha+1)**2)
eqn2 = Eq(l**2 - 2*l**2*alpha**7*cos(7*theta) + l**2*alpha**14, (alpha**7+1)**2)
eqn3 = Eq(l**2 - 2*l**2*alpha**8*cos(8*theta) + l**2*alpha**16, (alpha**8+1)**2)

alpha = nsolve([eqn1, eqn2, eqn3], [alpha, theta, l], [1, np.pi/4, 1], prec=50)[0]

a = 1 + alpha
b = 1 + alpha**8
c = alpha + alpha**8
theta1 = acos((a**2+b**2-c**2)/(2*a*b))
theta2 = acos((a**2+c**2-b**2)/(2*a*c))
theta3 = acos((b**2+c**2-a**2)/(2*b*c))

a = 1 + alpha**7
b = 1 + alpha**8
c = alpha**7 + alpha**8
theta1prime = acos((a**2+b**2-c**2)/(2*a*b))
theta2prime = acos((a**2+c**2-b**2)/(2*a*c))
theta3prime = acos((b**2+c**2-a**2)/(2*b*c))

area = (alpha**(9/2)*sqrt(alpha**8+alpha+1) + alpha**(15/2)*sqrt(alpha**8+alpha**7+1) 
        - 1/2*(theta1+theta1prime+alpha**2*theta2+alpha**14*theta2prime+alpha**16
        *(theta3+theta3prime)))/(1-alpha**2)

print(area)