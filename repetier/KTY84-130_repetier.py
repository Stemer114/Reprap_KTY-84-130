# based on python script from
#  http://diyhpl.us/reprap/trunk/users/wizard23/python/lookupTables/KTY84-130.py
#
# adapted by Stemer114 for usage with 4.7k pull-up resistor
# table format for repetier firmware
# https://github.com/Stemer114/Reprap_KTY-84-130
# 
# generates a Lookuptable for the following termistor
# KTY 84-130
# http://www.datasheetcatalog.org/datasheet/philips/KTY84_SERIES_5.pdf

# usage: 
#   python KTY84-130.py >ThermistorTable.h
#   copy ThermistorTable.h into your firmware dir
#   enable the lookup table in firmware config.h (depends on firmware)

# resistor values are taken from data sheet page 4, table 1
# temperature range is 0C to 300C in steps of 10K
# the negative temperature entries and the entry for 25C are omitted
resistorValues = [
498,
538,
581,
626,
672,
722,
773,
826,
882,
940,
1000,
1062,
1127,
1194,
1262,
1334,
1407,
1482,
1560,
1640,
1722,
1807,
1893,
1982,
2073,
2166,
2261,
2357,
2452,
2542,
2624]

tempValues = range(0, 301, 10)

if len(tempValues) != len(resistorValues):
	print "Length of temValues %d and resistorValues %d does not match" % (len(tempValues), len(resistorValues))
else:
	print "// reprap thermistor table for KTY 84-130 temperature sensor"
	print "// adapted for repetier firmware user thermistortable 1 format"
	print "// for further details see https://github.com/Stemer114/Reprap_KTY-84-130"
	print ""
	print "// consult the readme for how to insert the table into"
	print "// repetier Configuration.h"
	print "#define NUM_TEMPS_USERTHERMISTOR1 %d" % (len(tempValues))
	print "#define USER_THERMISTORTABLE1 {\ "
	suffix = ","
	for i in range(0, len(tempValues)):
		current = 5.0/(4700.0+resistorValues[i])
		voltage = current*resistorValues[i]
		adValue = round(voltage*1023.0/5.0)
		if i == len(tempValues)-1:
			suffix = ""
		print "   {%d*4, %d*8}%s \ " % (adValue, tempValues[i], suffix)
	print "};"
