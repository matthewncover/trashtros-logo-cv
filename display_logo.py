import wx

class TrashcanClipart:

    def __init__(self, filename, x0=100, y0=100):

        self.filename = filename
        self.x = x0
        self.y = y0

        self.set_dc_and_bitmap()       
    
    def set_dc_and_bitmap(self):
        
        app = wx.App(False)
        self.dc = wx.ScreenDc()

        im = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
        self.bitmap = im.ConvertToBitmap()

    def draw_bitmap(self):

        self.dc.DrawBitmap(self.bitmap, self.x, self.y)

    def update_loc(self, x, y):

        self.x = x
        self.y = y
        self.draw_bitmap()

    def update_size(self):
        """ use PIL and numpy to manipulate image
        """
        pass


if __name__ == "__main__":
    # app=wx.App(False)
    # dc=wx.ScreenDC()

    # im_filename = "trashtros_logo.png"

    # im = wx.Image(im_filename, wx.BITMAP_TYPE_ANY)
    # bitmap = im.ConvertToBitmap()

    # dc.DrawBitmap(bitmap, 100, 100)

    trash = TrashcanClipart("trashtros_logo.png")
    trash.draw_bitmap()

# app.MainLoop()

# September 23rd, 2021 Angels v. Astros

