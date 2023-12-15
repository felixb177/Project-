#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
int x = 0;
int y = 0;
int z = 0;

double sig_1, sig_2, sig_3, sig_4;


void setup() {
  Serial.begin(9600);
  myservo1.attach(3);
  myservo2.attach(5);
  myservo3.attach(6);
  myservo4.attach(9);

}

void loop() {

x = 6;
y = 8;
z = 5;
  double D = sqrt(pow(x, 2) + pow(y, 2));

  double theta_1 = atan(y/x) * 57.2957795131;

  double d = D - 9;

  double Zoffset = z - 5;

  double R = sqrt(pow(d, 2) + pow(Zoffset, 2));
  double alpha_1 = acos(d / R) * 57.2957795131;

  double alpha_2 = acos((pow(5, 2) + pow(R, 2) - pow(5, 2)) / (2 * 5 * R)) * 57.2957795131;

  double theta_2 = 90 + (alpha_1 + alpha_2);

  double theta_3 = acos((pow(5, 2) + pow(5, 2) - pow(R, 2)) / (2 * 5 * 5)) * 57.2957795131;

  double theta_4 = 180 - ((180 - (alpha_2 + theta_3)) - alpha_1);

    // KONVERSI SUDUT KE SINYAL SERVO
  sig_1 = map(theta_1, 0,180, 0,180); // SERVO 1
  sig_1 = constrain(sig_1,0,180);
  
  
  sig_2 = map(theta_2, 40,180, 30,180); // SERVO 2
  sig_2 = constrain(sig_2,30,180);
  
  
  sig_3 = map(theta_3, 10,175, 0,180); // SERVO 3
  sig_3 = constrain(sig_3,0,60);
  

  sig_4 = map(theta_4, 0,170, 0,180); // SERVO 4
  sig_4 = constrain(sig_4,0,60);
  


  Serial.print("Theta_1: ");
  Serial.println(sig_1);
  Serial.print("Theta_2: ");
  Serial.println(sig_2);
  Serial.print("Theta_3: ");
  Serial.println(sig_3);
  Serial.print("Theta_4: ");
  Serial.println(sig_4);

  // Rest of your code for servo control goes here

  delay(1000); // Delay for better readability in Serial Monitor
  for(int i = 0;i <=sig_1;i++){
    myservo1.write(i);
    delay(100);
  }
  for(int i = 0;i <=sig_2;i++){
    myservo2.write(i);
    delay(100);
  }
  for(int i = 0;i <=sig_3;i++){
    myservo3.write(i);
    delay(100);
  }
  for(int i = 0;i <=sig_4;i++){
    myservo4.write(i);
    delay(100);
  }

  delay(10000000000);
}