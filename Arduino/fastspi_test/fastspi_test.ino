#include <system_configuration.h>
#include <unwind-cxx.h>
#include <utility.h>

#define DEBUG_SPI

#include <FastSPI_LED.h>

#define NUM_LEDS 250
#define LIGHT_BOARD_WIDTH 19
#define LIGHT_BOARD_HEIGHT 13

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

void setLightBoardPixelColor(int x, int y, int r, int g, int b) {
  // The strand starts at the bottom right and snakes up and to the 
  // left, like so (assuming width of 4):
  //
  //  ^  11---10---09---08
  //  |  04---05---06---07
  //  y  03---02---01---00
  //   x --->
  // 
  // So, y*width will tell us the minimum index it could be.  Since
  // the rows alternate ordering, if the row is even, the additional
  // offset is width-x-1.
  int index = y * LIGHT_BOARD_WIDTH;
  if (y%2==1) {
      index += x;
  }else{
      index += (LIGHT_BOARD_WIDTH-x-1);
  }
  leds[index].r = r;
  leds[index].g = g;
  leds[index].b = b;
}

void setColor(int r, int g, int b) {
  memset(leds, 0, NUM_LEDS * 3);
  for (int i=0; i < NUM_LEDS; i++) {
    leds[i].r = r;
    leds[i].g = g;
    leds[i].b = b;
  }  
}

void showSinWave() {
  for (float t=0;t<12.0*3.1415;t=t+.04) {
    setColor( 8, 32, 16 );
    for (int x=0; x<LIGHT_BOARD_WIDTH; x++) {
      int y = int((sin(2.0*3.1415*x/LIGHT_BOARD_WIDTH+t)*0.8/2.0+0.5)*LIGHT_BOARD_HEIGHT);
      setLightBoardPixelColor( x, y, 255, 64, 255 );
    }
    FastSPI_LED.show();
  }
}

void loop() { 
  // one at a time
  for(int j = 0; j < 3; j++) { 
    for(int i = 0 ; i < NUM_LEDS; i++ ) {
      memset(leds, 0, NUM_LEDS * 3);
      switch(j) { 
        case 0: leds[i].r = 255; break;
        case 1: leds[i].g = 255; break;
        case 2: leds[i].b = 255; break;
      }
      FastSPI_LED.show();
      delay(1);
    }
  }
  
  showSinWave();

  // growing/receeding bars
  for(int j = 0; j < 3; j++) { 
    memset(leds, 0, NUM_LEDS * 3);
    for(int i = 0 ; i < NUM_LEDS; i++ ) {
      switch(j) { 
        case 0: leds[i].r = 255; break;
        case 1: leds[i].g = 255; break;
        case 2: leds[i].b = 255; break;
      }
      FastSPI_LED.show();
      delay(10);
    }
    for(int i = NUM_LEDS-1 ; i >= 0; i-- ) {
      switch(j) { 
        case 0: leds[i].r = 0; break;
        case 1: leds[i].g = 0; break;
        case 2: leds[i].b = 0; break;
      }
      FastSPI_LED.show();
      delay(1);
    }
  }
  
  // Fade in/fade out
  for(int j = 0; j < 3; j++ ) { 
    memset(leds, 0, NUM_LEDS * 3);
    for(int k = 0; k < 256; k++) { 
      for(int i = 0; i < NUM_LEDS; i++ ) {
        switch(j) { 
          case 0: leds[i].r = k; break;
          case 1: leds[i].g = k; break;
          case 2: leds[i].b = k; break;
        }
      }
      FastSPI_LED.show();
      delay(3);
    }
    for(int k = 255; k >= 0; k--) { 
      for(int i = 0; i < NUM_LEDS; i++ ) {
        switch(j) { 
          case 0: leds[i].r = k; break;
          case 1: leds[i].g = k; break;
          case 2: leds[i].b = k; break;
        }
      }
      FastSPI_LED.show();
      delay(3);
    }
  }
}
