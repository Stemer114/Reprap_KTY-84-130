## Usage for teacup firmware:
-----

1. call the python script to create the header file for the thermistor table

      python KTY84-130.py >ThermistorTable.h

2. copy the thermistor table into your teacup firmware dir

      cp ThermistorTable.h ../Teacup_Firmware

3. enable the thermistor table in the firmware configuration

      edit config.h


