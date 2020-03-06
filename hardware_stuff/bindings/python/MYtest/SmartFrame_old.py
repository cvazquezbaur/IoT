#!/usr/bin/env python
# Display time
from base import Base
from rgbmatrix import graphics
import time
from PIL import Image
from datetime import datetime


class SmartFrame(Base):
    def __init__(self, time_presence, weather_presence):
        super(SmartFrame, self).__init__()
        self.time_event_exist = False
        self.weather_event_exist = False
        self.weather_str = "This is the forcast"
        self.annc_q = [["EVENT","make sure the event part doesn't scroll"],["REMINDER 2", "make sure this all scrolls"],["TASK 3", "no scroll"]]

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        time_color = graphics.Color(255, 255, 255)
        weather_color = graphics.Color(0, 20, 255)
        annouce_header_color = graphics.Color(255, 0, 0)
        annouce_descpt_color = graphics.Color(100, 200, 255)
        
        self.version_1(offscreen_canvas, time_color, weather_color, annouce_header_color, annouce_descpt_color)
        self.version_2_1(offscreen_canvas, time_color, annouce_header_color, annouce_descpt_color)
        self.version_2_2(offscreen_canvas, weather_color, annouce_header_color, annouce_descpt_color)
        self.version_3(offscreen_canvas, annouce_header_color, annouce_descpt_color)
            
    def version_1(self, offscreen_canvas, time_color, weather_color, annouce_header_color, annouce_descpt_color):
        time_font = weather_font = annouce_header_font = annouce_descpt_font = graphics.Font()
        
        # Adjust the font being used for each displayed text
        time_font.LoadFont("../../../fonts/5x7.bdf")
        weather_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_header_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_descpt_font.LoadFont("../../../fonts/5x7.bdf")
        
        # Initialize variables outside incremental scope
        xpos_weather = annc_q_index = announment_round = 0
        xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
        
        while (self.time_event_exist and self.weather_event_exist):
            offscreen_canvas.Clear()
            # Is the annuncement queue empty?
            if (len(self.annc_q) != 0):
                announment_round += 1
                
                # Add the annuncement to the display
                annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                
                xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
                
                # Change the announcement after 3 scrolls
                if ((announment_round/xpos_announcement[2]) == 3):
                    annc_q_index += 1
                    announment_round = 0
                    xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
                    
                    # Add the annuncement to the display
                    offscreen_canvas.Clear()
                    annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                    annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                    xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
             
                if (annc_q_index == len(self.annc_q)):
                    annc_q_index = 0
            
            # Get the current time 
            current_time = datetime.now()
            str_time = current_time.strftime("%H:%M")
            
            # Add the time and weather to the display
            time_len = graphics.DrawText(offscreen_canvas, time_font, 4,8, time_color, str_time)
            weather_len = graphics.DrawText(offscreen_canvas, weather_font, xpos_weather,15, weather_color, self.weather_str)
            
            xpos_weather -= 1    
            if (xpos_weather + weather_len < 0):
                xpos_weather = offscreen_canvas.width 

            time.sleep(0.1)
            
            # Set the offscreen info to on screen
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        
    def version_2_1(self, offscreen_canvas, time_color, annouce_header_color, annouce_descpt_color):
        time_font = weather_font = annouce_header_font = annouce_descpt_font = graphics.Font()        
        
        # Adjust the font being used for each displayed text
        time_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_header_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_descpt_font.LoadFont("../../../fonts/5x7.bdf")
        
        # Initialize variables outside incremental scope
        xpos_announcement = annc_q_index = announment_round = announment_len = 0
        xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
        
        while (self.time_event_exist and not self.weather_event_exist):
            offscreen_canvas.Clear()
            # Is the annuncement queue empty?
            # Is the annuncement queue empty?
            if (len(self.annc_q) != 0):
                announment_round += 1
                
                # Add the annuncement to the display
                annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                
                xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
                
                # Change the announcement after 3 scrolls
                if ((announment_round/xpos_announcement[2]) == 3):
                    annc_q_index += 1
                    announment_round = 0
                    xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
                    
                    # Add the annuncement to the display
                    offscreen_canvas.Clear()
                    annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                    annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                    xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
             
                if (annc_q_index == len(self.annc_q)):
                    annc_q_index = 0
                    
            # Get the current time 
            current_time = datetime.now()
            str_time = current_time.strftime("%H:%M")
            
            # Add the time and weather to the display
            time_len = graphics.DrawText(offscreen_canvas, time_font, 4,8, time_color, str_time)
            time.sleep(0.1)
            
            # Set the offscreen info to on screen
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
    
    def version_2_2(self, offscreen_canvas, weather_color, annouce_header_color, annouce_descpt_color):
        weather_font = annouce_header_font = annouce_descpt_font = graphics.Font()

        # Adjust the font being used for each displayed text
        weather_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_header_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_descpt_font.LoadFont("../../../fonts/5x7.bdf")
        
        # Initialize variables outside incremental scope
        xpos_weather = xpos_announcement = annc_q_index = announment_round = announment_len = 0
        xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
        
        while (not self.time_event_exist and self.weather_event_exist):
            offscreen_canvas.Clear()
            # Is the annuncement queue empty?
            if (len(self.annc_q) != 0):
                announment_round += 1
                
                # Add the annuncement to the display
                annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                
                xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
                
                # Change the announcement after 3 scrolls
                if ((announment_round/xpos_announcement[2]) == 3):
                    annc_q_index += 1
                    announment_round = 0
                    xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
                    
                    # Add the annuncement to the display
                    offscreen_canvas.Clear()
                    annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                    annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                    xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
             
                if (annc_q_index == len(self.annc_q)):
                    annc_q_index = 0
                    
            # Add the weather to the display
            weather_len = graphics.DrawText(offscreen_canvas, weather_font, xpos_weather,15, weather_color, self.weather_str)
            
            xpos_weather -= 1    
            if (xpos_weather + weather_len < 0):
                xpos_weather = offscreen_canvas.width 

            time.sleep(0.1)
            
            # Set the offscreen info to on screen
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
    
    def version_3(self, offscreen_canvas, annouce_header_color, annouce_descpt_color):
        annouce_header_font = annouce_descpt_font = graphics.Font()
        
        # Adjust the font being used for each displayed text
        annouce_header_font.LoadFont("../../../fonts/5x7.bdf")
        annouce_descpt_font.LoadFont("../../../fonts/5x7.bdf")
        
        # Initialize variables outside incremental scope
        xpos_announcement = annc_q_index = announment_round = announment_len = 0
        xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
        
        while (not self.time_event_exist and  not self.weather_event_exist):
            offscreen_canvas.Clear()
            # Is the annuncement queue empty?
            if (len(self.annc_q) != 0):
                announment_round += 1
                
                # Add the annuncement to the display
                annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                
                xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
                
                # Change the announcement after 3 scrolls
                if ((announment_round/xpos_announcement[2]) == 3):
                    annc_q_index += 1
                    announment_round = 0
                    xpos_announcement = [offscreen_canvas.width,offscreen_canvas.width,0]
                    
                    # Add the annuncement to the display
                    offscreen_canvas.Clear()
                    annouce_header_len = graphics.DrawText(offscreen_canvas, annouce_header_font, xpos_announcement[0],24, annouce_header_color, self.annc_q[annc_q_index][0])
                    annouce_descpt_len = graphics.DrawText(offscreen_canvas, annouce_descpt_font, xpos_announcement[1],30, annouce_descpt_color, self.annc_q[annc_q_index][1])
                    xpos_announcement = self.decide_announcement_scroll(annouce_descpt_len, xpos_announcement[1], annouce_header_len, xpos_announcement[0], offscreen_canvas)
             
                if (annc_q_index == len(self.annc_q)):
                    annc_q_index = 0

            time.sleep(0.1)
            
            # Set the offscreen info to on screen
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
          
    #Return s the appropriete xpos depending on whether or not the text must scorll      
    def decide_announcement_scroll(self,d_len, d_xpos, h_len, h_xpos, canvas):
         a_len = 0;
         scroll_h = True
         scroll_d = True

         # Find the longer announcement length
         if d_len > h_len:
             a_len = d_len
             a_xpos = d_xpos
         else:
             a_len = h_len
             a_xpos = h_pos
         
         # if there's no need to scroll
         if h_len <= canvas.width:
             h_xpos = 0
             scroll_h = False  
         if d_len <= canvas.width:
             d_xpos = 0
             scroll_d = False
             
         # If descrpt or header need to scroll adjust xpos    
         if scroll_h and scroll_d:
             a_xpos -= 1
             if (a_xpos + a_len < 0):
                a_xpos = canvas.width
             h_xpos = d_xpos = a_xpos
         elif scroll_h:
            h_xpos -= 1    
            if (h_xpos + h_len < 0):
                h_xpos = canvas.width
         elif scroll_d:
            d_xpos -= 1
            if (d_xpos + d_len < 0):
                d_xpos = canvas.width
         return [h_xpos, d_xpos, a_len]
    
# Main function
if __name__ == "__main__":
    run_frame = SmartFrame()
    if (not run_frame.process()):
        run_frame.print_help()


