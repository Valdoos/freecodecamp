class Rectangle:

    def __init__(self,width=0,height=0):
        self.width = int(width)
        self.height = int(height)

    def set_width(self,width):
        self.width = int(width)

    def set_height(self,height):
        self.height = int(height)

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*self.height+2*self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        ans = (self.width*"*"+"\n")*self.height
        return ans

    def get_amount_inside(self,another):
        x = int(self.width / another.width)
        y = int(self.height/ another.height)
        return x*y

    def __repr__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self,side):
        self.set_width(side)
        self.set_height(side)

    def __repr__(self):
        return "Square(side="+str(self.width)+")"
