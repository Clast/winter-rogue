
#The Map_Object class contains the basic variables and functions that any object placed on the board will need.

class Map_Object:

    def __init__(self, x, y, imgpath, Img):
        self.xcoordinate = x
        self.ycoordinate = y
        self.imgpath = imgpath
        self.Img= pygame.image.load(self.imgpath)


    def move (self, dx, dy):
        self.x = dx
        self.y = dy


    def get_image(self):
        print "Returning Image %s" % self.imgpath
        return self.Img