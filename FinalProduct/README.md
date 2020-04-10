# C3 Smart Clock
**This is a website application that programs an AdaFruit RGB 32x32 LED Matrix running on a Model 4 Raspberry Pi to display Google calender events, time, and/or the weather.**

The C3 Smart Clock is designed to act as a customizable smart display that changes from day to day or as wanted by the user.

## Getting Started
(NOTE: The Raspberry Pi may not be plugged in at this time due to the COVID19 pandemic and therefore this program has lost it's remote programability.)
 * Go to http://c3smartclock.hopto.org or the IP address of the Raspberry Pi. 
 * Enter in display preferences and then press 'Submit'.
 * Watch as the display on the AdaFruit RGB 32x32 LED Matrix reflects the inputted preferences.

## Creators
** Caroline Sonnen, Carlos Vazquez Baur, and Caterina Valdovinos**

## Why was this created?
This is Group 6's hands on project for Internet of Things CPSC 310 section one course.

## References
All files in matrix_code, except for those found in bindings/python/c3 were created by 
Hzeller and can be found at https://github.com/hzeller/rpi-rgb-led-matrix. Slight editations were made to fine tune the software to the AdaFruit
RGB 32x32 LED Matrix running on a Model 4 Raspberry Pi. These changes are listed below:
* Removed all other choices of gpiomapping in hardware-mapping.cc except 'classic-pi1'
* lib\ledmatrix.cc
    * In RGBMatrix Options (line 189)
        * Set all the options with accordance to our matrix