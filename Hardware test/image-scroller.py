#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width/4, self.matrix.height/4), Image.ANTIALIAS)

        double_buffer_UL = self.matrix.CreateFrameCanvas()
        double_buffer_UR = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size

        # let's scroll on UL
        xpos_UL = 0
        xpos_UR = 16
        xpos_LR = 16
        xpos_LL = 0
        while True:
            #UL
            xpos_UL += 1
            if (xpos_UL > img_width):
                xpos_UL = 0
            double_buffer_UL.SetImage(self.image, -xpos_UL)
            double_buffer_UL.SetImage(self.image, -xpos_UL + img_width)

            double_buffer_UL = self.matrix.SwapOnVSync(double_buffer_UL)
            time.sleep(0.01)
            
            #UR
            xpos_UR += 1
            if (xpos > img_width):
                xpos = 0
            double_buffer_UR.SetImage(self.image, -xpos_UR)
            double_buffer_UR.SetImage(self.image, -xpos_UR + img_width)

            double_buffer = self.matrix.SwapOnVSync(double_buffer_UR)
            time.sleep(0.01)
            
            # #LR
            # xpos_LR += 1
            # if (xpos > img_width):
                # xpos = 0
            # double_buffer.SetImage(self.image, -xpos)
            # double_buffer.SetImage(self.image, -xpos + img_width)

            # double_buffer = self.matrix.SwapOnVSync(double_buffer)
            # time.sleep(0.01)
            
            # #LL
            # xpos_LL += 1
            # if (xpos > img_width):
                # xpos = 0

            # double_buffer.SetImage(self.image, -xpos)
            # double_buffer.SetImage(self.image, -xpos + img_width)

            # double_buffer = self.matrix.SwapOnVSync(double_buffer)
            # time.sleep(0.01)
              

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
