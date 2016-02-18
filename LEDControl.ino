#include "FastLED.h"

#define NUM_LEDS 50

#define DATA_PIN 11
#define CLOCK_PIN 13

CRGB leds[NUM_LEDS];
String htmlColour;
long number;

void setup() { 
  Serial.begin(9600);
  FastLED.addLeds<WS2801, RGB>(leds, NUM_LEDS);
}

void loop(){

  if (Serial.available() > 0){
    htmlColour = Serial.readStringUntil('\n');
    Serial.read();
    number = strtol( &htmlColour[1], NULL, 16);
    Serial.println(number);
  }
  
  for(int i = 0; i < NUM_LEDS; i++) {
    leds[i] = number;
    leds[i].maximizeBrightness();
  }
  FastLED.show();
}
