#define DEBUG_SPI

#include <FastSPI_LED.h>

#define NUM_LEDS 250

// Sometimes chipsets wire in a backwards sort of way
struct CRGB { unsigned char r; unsigned char g; unsigned char b; };
// struct CRGB { unsigned char r; unsigned char g; unsigned char b; };
struct CRGB *leds;

//#define PIN 4

void setup()
{
  Serial.begin(115200);
  Serial.println("Hello");
  
  FastSPI_LED.setLeds(NUM_LEDS);
  //FastSPI_LED.setChipset(CFastSPI_LED::SPI_TM1809);
  //FastSPI_LED.setChipset(CFastSPI_LED::SPI_LPD6803);
  //FastSPI_LED.setChipset(CFastSPI_LED::SPI_HL1606);
  //FastSPI_LED.setChipset(CFastSPI_LED::SPI_595);
  FastSPI_LED.setChipset(CFastSPI_LED::SPI_WS2801);

  //FastSPI_LED.setPin(PIN); // Irrelevant for ws2801
  
  FastSPI_LED.setDataRate(3);
  
  FastSPI_LED.init();
  FastSPI_LED.start();

  leds = (struct CRGB*)FastSPI_LED.getRGBData(); 
}


void loop() { 

   while (true)
   {
       if (Serial.available() > 0) {
         
         if (Serial.find("show"))
         {
           int numLeds = Serial.parseInt();
           for (int i=0;i<numLeds;++i)
           {
             byte r = Serial.parseInt();
             byte g = Serial.parseInt();
             byte b = Serial.parseInt();
             
//             Serial.print("Found: ");
//             Serial.print(i);
//             Serial.print(" = ");
//             Serial.print(r);
//             Serial.print(" , ");
//             Serial.print(g);
//             Serial.print(" , ");
//             Serial.print(b);
//             Serial.println();
             
             leds[i].r = r;
             leds[i].g = g;
             leds[i].b = b;
           }
           
           FastSPI_LED.show();
         }
       }
      
   }
}
