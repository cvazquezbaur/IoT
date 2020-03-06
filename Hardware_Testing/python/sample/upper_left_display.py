#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from PIL import Image


class Upper_Left_Display(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        
        # Get the current time
        current_time = datetime.datetime.now()
        str_time = strftime(current_time.hour) + ":" +strftime(current_time.minute)
        self.parser.add_argument("-t", "--text", help="Display on upper left side: default is the time", default=str_time)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 255) #white
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            current_time = datetime.datetime.now()
            str_time = strftime(current_time.hour) + ":" +strftime(current_time.minute)
            
            # Reset the text to the current time
            my_text = str_time
            
            # Set the offscreen info to on screen
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    upper_left_display = Upper_Left_Display()
    if (not upper_left_display.process()):
        upper_left_display.print_help()
