// reprap thermistor table for KTY 84-130 temperature sensor
// adapted for teacup firmware single table format
// for further details see https://github.com/Stemer114/Reprap_KTY-84-130

// the following defines need matching settings in config.h of your firmware
#define NUMTABLES 1
#define THERMISTOR_EXTRUDER 0
#define NUMTEMPS 31
uint16_t const temptable[NUMTABLES][NUMTEMPS][2] PROGMEM = {
{
   {98, 0},  // 0.48 V |   0 C
   {105, 40},  // 0.51 V |  10 C
   {113, 80},  // 0.55 V |  20 C
   {120, 120},  // 0.59 V |  30 C
   {128, 160},  // 0.63 V |  40 C
   {136, 200},  // 0.67 V |  50 C
   {144, 240},  // 0.71 V |  60 C
   {153, 280},  // 0.75 V |  70 C
   {162, 320},  // 0.79 V |  80 C
   {170, 360},  // 0.83 V |  90 C
   {179, 400},  // 0.88 V | 100 C
   {189, 440},  // 0.92 V | 110 C
   {198, 480},  // 0.97 V | 120 C
   {207, 520},  // 1.01 V | 130 C
   {217, 560},  // 1.06 V | 140 C
   {226, 600},  // 1.11 V | 150 C
   {236, 640},  // 1.15 V | 160 C
   {245, 680},  // 1.20 V | 170 C
   {255, 720},  // 1.25 V | 180 C
   {265, 760},  // 1.29 V | 190 C
   {274, 800},  // 1.34 V | 200 C
   {284, 840},  // 1.39 V | 210 C
   {294, 880},  // 1.44 V | 220 C
   {303, 920},  // 1.48 V | 230 C
   {313, 960},  // 1.53 V | 240 C
   {323, 1000},  // 1.58 V | 250 C
   {332, 1040},  // 1.62 V | 260 C
   {342, 1080},  // 1.67 V | 270 C
   {351, 1120},  // 1.71 V | 280 C
   {359, 1160},  // 1.76 V | 290 C
   {367, 1200},  // 1.79 V | 300 C
}
};
