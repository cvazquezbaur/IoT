from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

#gets pressure
pressure = sense.get_pressure()

#gets temperature
temp = sense.get_temperature()

#gets humidity
humidity = sense.get_humidity()

#gets orientation
orientation = sense.get_orientation()
p = round(orientation["pitch"], 0)
r = round(orientation["roll"], 0)
y = round(orientation["yaw"], 0)

while True:
    for event in sense.stick.get_events():        
        if event.direction == "right":
            print("Temperature")
            print(str(temp))
            
            sense.show_message(str(temp))
        elif event.direction == "left":
            print("Pressure")
            print(str(pressure))
            sense.show_message(str(pressure))
            
        elif event.direction == "up":
            print("Humidity")
            print(str(humidity))
            sense.show_message(str(humidity))
            
        elif event.direction == "down":
            print("Orientation")
            print("p: %s, r: %s, y: %s" % (p,r,y))
            sense.show_message("p: %s, r: %s, y: %s" % (p,r,y))
        #print(event.direction, event.action)
        
