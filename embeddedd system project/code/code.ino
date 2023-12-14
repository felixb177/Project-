#include "Arduino.h"
#include "LowPower.h"
#include "avr/wdt.h"

#define potensio A0
#define button 2

int input_sblm = HIGH;
int tepi_naik = HIGH;
unsigned long waktu_debouncing = 0;
unsigned long delay_debouncing = 50;
int input = LOW;
int kondisi_sblm = LOW;

volatile int state = 1;

void setup() {
  // put your setup code here, to run once:
  MCUSR &= ~(1<<WDRF); // Clear WDRF in MCUSR
  wdt_disable();
  Serial.begin(9600);
  pinMode(potensio, INPUT);
  pinMode(button, INPUT_PULLUP);
  delay(2000);
  wdt_enable(WDTO_8S);//enabling
}

void state_1(){
        LowPower.powerDown(SLEEP_4S, ADC_ON, BOD_OFF);
        int start = millis();
        while(millis() - start < 2000){
              int kondisi = digitalRead(button);
                      if(kondisi != kondisi_sblm){
                        waktu_debouncing = millis();
                      }
                      if((millis()-waktu_debouncing) > delay_debouncing){
                      if(kondisi != input){
                          input = kondisi;
                      }
                      }
                      kondisi_sblm = kondisi;
 
                      if(input == LOW && input_sblm == HIGH){
                        input_sblm = input;
                        }
                      else if(input == HIGH && input_sblm == LOW){
                      input_sblm = input;
                      tepi_naik = LOW;
                }
                if(tepi_naik == LOW){
                  state = 2;
                  break;
                }
        }
        wdt_enable(WDTO_8S);
}

void state_2(){
  wdt_enable(WDTO_8S);

  int value = analogRead(potensio);
  Serial.println(value);
  if(value > 512){
    state = 3;
  }
}
void state_3(){
  wdt_enable(WDTO_8S);
  int start = millis();
  while(millis()-start < 5000){
    int value = analogRead(potensio);
    Serial.println(value);
  }
  state = 1;
}
void loop() {
  // put your main code here, to run repeatedly:

  switch(state){
      case 1:
      Serial.println("s1");
       state_1();
        break;
      case 2:
      Serial.println("s2");
      state_2();
        break;
      case 3:
      Serial.println("s3");
      state_3();
      break;


  }
  wdt_reset();

}