import libreriadecomplejos as lc
import math
def probabilidad(a,pos):
    
    s = 0
    for i in a:
        s+= lc.modulocomplejo(i)*lc.modulocomplejo(i)
    p = (s)**(1/2)
    pe=(lc.modulocomplejo(a[int(pos)]))**2/p**2
    return round(pe*100,2)
def amplituddetransicion(a,b):
   x = lc.producto_interno(b,a)
   y = lc.norma_vector(a)*lc.norma_vector(b)
   return lc.divisioncomplejos(x,[y,0])
def valoresperado(a,b):
    return round(lc.producto_interno(lc.accionmatrizvector(a,b),b)[0],1)
##def main():
##    a = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
##    b = [[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]
##    c = [[[2,0],[1,1]],[[1,-1],[3,0]]]
##    d = [[1/(2**.5),0],[0,1/(2**0.5)]]
##    pos = input()
##    print(probabilidad(a),pos)
##    print(amplituddetransicion(a,b))
##    print(valoresperado(c,d))
##   
##
