#define LED_PIN3 8
#define LED_PIN2 9
#define LED_PIN1 10

int R1= 1000;
int EC_Read = A0;
int ECPower = A1;
int Temp_pin = A5;
float Temp_C;
float Temp_F;
float Temp1_Value = 0;
float Temp_Coef = 0.019;
float Calibration_PPM =1080 ;
float K=1.89;
float PPM_Con=0.5;
float CalibrationEC= (Calibration_PPM*2)/1000;
float Temperature;
float EC;
float EC_at_25;
int ppm;
int ppm2;
float A_to_D= 0;
float Vin= 5;
float Vdrop= 0;
float R_Water;
float Value=0;

int iter = 0;
int sum = 0;

void setup() {
  Serial.begin(9600);
  pinMode(EC_Read,INPUT);
  pinMode(ECPower,OUTPUT);
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  digitalWrite(LED_PIN1, HIGH);
  digitalWrite(LED_PIN2, HIGH);
  digitalWrite(LED_PIN3, HIGH);
}

void loop() {
  iter += 1;
  GetEC();
  delay(6000);
  if (iter == 12) {
    Serial.print("SUM: ");
    Serial.print(sum / 12);
  }
  if (iter < 12) {
    Serial.print("CALIBRATING");
    Serial.print("\n");
  }
}

void GetEC() {
  int val;
  double Temp;
 
  val=analogRead(Temp_pin);
  Temp = log(((10240000/val) - 10000));
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp);
  Temp_C = Temp - 273.15; // Kelvin to Celsius
  Temp_F = (Temp_C * 9.0)/ 5.0 + 32.0; // Celsius to Fahrenheit
  Temp1_Value = Temp_C;
  Temperature = Temp_C;
  digitalWrite(ECPower,HIGH);
  A_to_D= analogRead(EC_Read);
  A_to_D= analogRead(EC_Read);
  digitalWrite(ECPower,LOW);
  Vdrop= (Vin*A_to_D) / 1024.0;
  R_Water = (Vdrop*R1) / (Vin-Vdrop);
  EC = 1000/ (R_Water*K);
  EC_at_25 = EC / (1+ Temp_Coef*(Temperature-25.0));
  ppm=((EC_at_25)*(PPM_Con*1000));
 
  Serial.print("PPM: ");
  Serial.print(ppm);
  float voltage;
  voltage = EC_at_25 * PPM_Con;
  Serial.print(" VOLTAGE: ");
  Serial.print(voltage);
  Serial.print("\n");
  if (ppm <= 600 and ppm > 0) {
    digitalWrite(LED_PIN1, HIGH);
    digitalWrite(LED_PIN2, LOW);
    digitalWrite(LED_PIN3, LOW);
  }
 
  if (ppm <= 1500 and ppm > 600) {
     digitalWrite(LED_PIN1, HIGH);
     digitalWrite(LED_PIN2, HIGH);
     digitalWrite(LED_PIN3, LOW);
  }
 
  if (ppm <= 3400 and ppm > 1500) {
    digitalWrite(LED_PIN1, LOW);
    digitalWrite(LED_PIN2, HIGH);
    digitalWrite(LED_PIN3, LOW);
  }
 
  if (ppm <= 5000 and ppm > 3400) {
    digitalWrite(LED_PIN1, LOW);
    digitalWrite(LED_PIN2, LOW);
    digitalWrite(LED_PIN3, HIGH);
  }
 
  if (iter > 3) {
    sum += ppm;
  }
}
