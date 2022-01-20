int motorpin=36; //defining the pin connected to servo
int potpin = A0;
int position=0; // initial position of servo
int hightime=0; // initial hightime
int dutycycle=12000; // total time of duty cycle in microsecond
String inputpos;
int inputposlength;
int oldReading = 0;


void setup() {
  pinMode(potpin,INPUT);
  pinMode(motorpin,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    String inputpos=Serial.readString(); 
    inputposlength = inputpos.length();
    if (inputpos[0] == 'B' && inputpos[1] == 'S' && inputpos[inputposlength-1] == 'X' ){
     inputpos.remove(inputposlength-1);
      inputpos.remove(0,2);
      inputposlength = inputpos.length();
      for (int i=0; i<inputposlength; i++){
        if (isdigit(inputpos[i])==true){
          position = inputpos.toInt();
        }
        else {
          position = -1;
        break;}
    }
      if (position>180){
        position = -1;}
      Serial.println(position);
     
    }
    else { position = -1;}
  }
  
 int potReading = analogRead(potpin);
  potReading = map(potReading,0,1023,0,180);
  delay(10);
  if (oldReading != potReading) {
   oldReading = potReading;
    position = oldReading;}
  
    if (position == -1) {
      hightime = 0; }
    else {
      hightime = map(position,0,180,1000,2000);}
  if(hightime){
  digitalWrite(motorpin,HIGH);
    delayMicroseconds(hightime);}
    digitalWrite(motorpin,LOW);
    delayMicroseconds(dutycycle-hightime);
            }       
