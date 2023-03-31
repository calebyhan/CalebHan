#define LED_PIN1 3
#define LED_PIN2 4
#define LED_PIN3 5

int FSR_pin = A0;    // select the input pin for the potentiometer
int avg_size = 10; // number of analog readings to average
float R_0 = 220.0; // known resistor value in [Ohms]
float Vcc = 5.0; // supply voltage
int val1 = 300; // bound for led
int val2 = 800; // bound for led

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  digitalWrite(LED_PIN1, LOW);
  digitalWrite(LED_PIN2, LOW);
  digitalWrite(LED_PIN3, LOW);
}

void loop() {
  float sum_val = 0.0; // variable for storing sum used for averaging
  float R_FSR;
  for (int ii=0;ii<avg_size;ii++){
    sum_val+=(analogRead(FSR_pin)*(5/1023.0)); // sum
    delay(10);
  }
  sum_val/=avg_size; // take average
 
  float grams = 5567 - (3501 * log(sum_val)) - 24.94; // equation for converting volts to grams
  if (sum_val == 5.00) {
    grams = 0;
  }
  Serial.print("VOLTS: " + String(sum_val));
  Serial.println("; GRAMS: " + String(grams));
  delay(10);

  // leds
  if (grams <= val1 and grams > 30) {
    digitalWrite(LED_PIN1, HIGH);
    digitalWrite(LED_PIN2, LOW);
    digitalWrite(LED_PIN3, LOW);
  }
 
  if (grams <= val2 and grams > val1) {
    digitalWrite(LED_PIN1, LOW);
    digitalWrite(LED_PIN2, HIGH);
    digitalWrite(LED_PIN3, LOW);
  }
 
  if (grams <= 1000 and grams > val2) {
    digitalWrite(LED_PIN1, LOW);
    digitalWrite(LED_PIN2, LOW);
    digitalWrite(LED_PIN3, HIGH);
  }
}
