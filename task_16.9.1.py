imoprt math

class Triangle:
   def __init__(self, a, b, alpha, x=0, y=0):
       alpha = math.radians(alpha)
       c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(alpha))
       self.x = x #Delta angle alpha position by axis x
       self.y = y #Delta angle alpha position by axis y
       self.a = a #Delta side a dimension (angle 0' by axis x)
       self.b = b #Delta side a dimension
       self.c = c #Delta side a dimension
       self.alpha = alpha #Delta angle between side a and side b
       
   def perimeter(self):
       return self.a + self.b + self.c
       
   def area(self):
       p = self.perimeter() / 2
       return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
       
   def attributes(self):
       return f"Triangle({self.x},{self.y},{self.a},{self.b},{math.degress(self.alpha)})"
