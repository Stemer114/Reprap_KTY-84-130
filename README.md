Reprap KTY-84-130
=====

Support files for using the KTY 84-130 temperature sensor with reprap 3d printer

The KTY 84-130 is a silicon temperature sensor rated for -40..300°C which I use as a replacement for the standard 100k thermistors used in repraps.

Motivation
-----

The KTY was more readily available for me than the standard 100k reprap
thermistors. At the german distributor reichelt, where I ordered most of my
electronic components the 100k thermistor is not available, but the KTY 84-130
is and is only about 0.77 EUR per piece.

The housing is a SOD68 leaded package with a diameter of 1.6mm which can easily
be incorporated into the hotend.

History
-----

This work is based on a python script from
http://diyhpl.us/reprap/trunk/users/wizard23/python/lookupTables/KTY84-130.py

adapted by Stemer114 for usage with 4.7k pull-up resistor
and table format for teacup and repetier firmware


usage for teacup firmware:
-----

-  python KTY84-130.py >ThermistorTable.h
-  copy ThermistorTable.h into your firmware dir
-  enable the lookup table in firmware config.h (depends on firmware)


usage for Repetier firmware:
-----

  see folder Repetier


Connection of the KTY 84-130 to your reprap controller
-----

The setup right now is the KTY 84-130 connected instead of the 100k Thermistor,
ie. the sensor connected between the port pin and ground. Additionally, on the
Sanguinololu 1.3a controller board I use, there is a 4.7k pull-up connected to
the port pin (which is accounted for in calculating the table values).

Status
-----

So far, the KTY has been tested successfully on a hotend and on the heated bed. 

For both applications, it works well. Besides calibration objects and various small parts, I have printed nearly all 
parts for a Mendel90 reprap printer, which will be my second printer.



