
int led = A4;
int shutter = 7;
int dip1 = 4;
int dip2 = 2;
int dip3 = 3;
int dip4 = 5;
int dip5 = 6;
int dip6 = A2;
int dip7 = A1;
int dip8 = A0;
int sw = 1;

long dip1_value = 0;
long dip2_value = 0;
long dip3_value = 0;
long dip4_value = 0;
long dip5_value = 0;
long dip6_value = 0;
long dip7_value = 0;
long dip8_value = 0;

void setup() {                
  Serial.begin(9600);
  pinMode(led, OUTPUT);     
  pinMode(shutter, OUTPUT);     
  pinMode(dip1, INPUT_PULLUP);     
  pinMode(dip2, INPUT_PULLUP);     
  pinMode(dip3, INPUT_PULLUP);     
  pinMode(dip4, INPUT_PULLUP);     
  pinMode(dip5, INPUT_PULLUP);     
  pinMode(dip6, INPUT_PULLUP);     
  pinMode(dip7, INPUT_PULLUP);     
  pinMode(dip8, INPUT_PULLUP);     
  pinMode(sw, INPUT_PULLUP);     
}

// the loop routine runs over and over again forever:
void loop() {
  if(digitalRead(sw) == LOW) {
    delay(500);
    if(digitalRead(sw) == LOW) {
      long shutter_time;
      long number_of_subs;
      dip1_value = 1 - int(digitalRead(dip1));
      dip2_value = 1 - int(digitalRead(dip2));
      dip3_value = 1 - int(digitalRead(dip3));
      dip4_value = 1 - int(digitalRead(dip4));
      
      dip5_value = 1 - int(digitalRead(dip5));
      dip6_value = 1 - int(digitalRead(dip6));
      dip7_value = 1 - int(digitalRead(dip7));
      dip8_value = 1 - int(digitalRead(dip8));
      
      shutter_time = 15*(dip1_value + 2*dip2_value + 3*dip3_value + 6*dip4_value)*1000;
      number_of_subs = 10*(dip5_value + 2*dip6_value + 3*dip7_value + 4*dip8_value);
      Serial.println(shutter_time);
      Serial.println(number_of_subs);
      for(int i=0; i < number_of_subs; i++) {
        digitalWrite(led, HIGH);
        digitalWrite(shutter, HIGH);
        delay(shutter_time);
        digitalWrite(led, LOW);
        digitalWrite(shutter, LOW);
        delay(5000);
      }
    }
  }
}
