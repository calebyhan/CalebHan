// define IO pin
#define PWMA 5    // Controls power to right motor
#define PWMB 6    // Controls power to left motor
#define AIN 7
#define BIN 8
#define STBY 3

const int trigPin = 13;
const int echoPin = 12;
float duration, distance;

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(BIN, OUTPUT);
  pinMode(AIN, OUTPUT);
  pinMode(STBY, OUTPUT);
  digitalWrite(STBY, HIGH);
  digitalWrite(PWMA, LOW);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  distance = 10000;
  
  digitalWrite(STBY, LOW);
  Serial.begin(9600);
}

void loop() {
  while (distance > 7){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    duration = pulseIn(echoPin, HIGH);
    distance = (duration*.0343)/2;
    Serial.print("Distance: ");
    Serial.println(distance);
    delay(100);
  }

  //L: A, R: B
  // 90 degree turns: 270
  
  delay(1000);

  start();

  // CHANGE HERE

  moveBlock();
  turnRight(390);
  
  // CHANGE HERE
  endRun();

  delay(10000000);
}

void start() {
  //back(385);
  //delay(500);
  turnRight(670);
  delay(500);
}

void endRun() {
  go(400);
}

void moveBlock() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(STBY, HIGH);
    digitalWrite(AIN, LOW);
    analogWrite(PWMA, 255);
    digitalWrite(BIN, LOW);
    analogWrite(PWMB, 180);
    delay(240);
    digitalWrite(STBY, LOW);
    delay(300);
  }
  delay(300);
}

void turnLeft(int mS) {
  digitalWrite(STBY, HIGH);
  digitalWrite(AIN, HIGH);
  analogWrite(PWMA, 255);
  digitalWrite(BIN, LOW);
  analogWrite(PWMB, 180);
  delay(mS);
  digitalWrite(STBY, LOW);
  delay(300);
}

void turnRight(int mS) {
  digitalWrite(STBY, HIGH);
  digitalWrite(AIN, LOW);
  analogWrite(PWMA, 255);
  digitalWrite(BIN, HIGH);
  analogWrite(PWMB, 180);
  delay(mS);
  digitalWrite(STBY, LOW);
  delay(300);
}

void go(int mS) {
  digitalWrite(STBY, HIGH);
  digitalWrite(AIN, LOW);
  analogWrite(PWMA, 255);
  digitalWrite(BIN, LOW);
  analogWrite(PWMB, 180);
  delay(mS);
  digitalWrite(STBY, LOW);
}
