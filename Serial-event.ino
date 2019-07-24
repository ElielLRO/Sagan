int rele = 4;
int bt = 6;
int sens = 7;
int led = 5;
int entrada = 0;

int estadoSensor = 0;
int ultestadoSensor = 0;

float t1 = 0;
float t2 = 0;

void setup() {

  Serial.begin(14400);
  pinMode(rele, OUTPUT);
  pinMode(bt, INPUT);
  pinMode(sens, INPUT);
  pinMode(led, OUTPUT);
  delay(500);
  digitalWrite(led, 1);

}
void loop() {

  // O Loop espera do script em python a rotina desejada

  if (Serial.available() > 0) {
    entrada = Serial.read();
    if (entrada == 65){ // A        //Primeira rotina: 
      Rotina_1();
      }
      
    else if (entrada == 66){ // B
      Rotina_2(bt);
      }
      
    else if (entrada == 67){ // C
      Rotina_2(sens);
      }

    else if (entrada == 68){ // D
      Rotina_3();
      } 
    else if (entrada == 70){ // F
      solenoide();
      } 
    else if (entrada == 98) {  // b
      output_bt();            //envia valor do Pino
      }

    else if (entrada == 115) { // s
      output_sens();
      }

    else if (entrada == 114) { // r
      if (digitalRead(rele) == HIGH) {
        digitalWrite(rele, 0);
        }
      else {digitalWrite(rele,0);}
    }
    else if (entrada == 99) { // c
      conf_receive();
      }
  }
}

void Rotina_1() { //serial-velocimetro.py

while (true){
  digitalWrite(rele,1); 
  if (digitalRead(bt) == 1){
    digitalWrite(rele,0);
    delay(750);
    while (true){
      
      if (digitalRead(bt) == 1){
        digitalWrite(rele,1);
        break;
        }
      else {continue;}
      }
    while (digitalRead(sens) == 0){continue;}
    Serial.write(1);
    while (digitalRead(sens) == 1){continue;}
    Serial.write(1);
    delay(750);
    break;
    }
  }
}

void Rotina_2(int pino){  // crono-4steps-sens.py  e crono-4steps-bot.py 
  
  for (int i = 0; i<=5; i++){
    while (digitalRead(pino) == 0){continue;}
    Serial.write(1); 
    while (digitalRead(pino) == 1){continue;}
  }
}

void Rotina_3(){ // tempo-queda.py
  digitalWrite(rele,0);
  while (digitalRead(bt) == 0){continue;}
  digitalWrite(rele,1);
  delay(750);
  while (digitalRead(bt) == 0){continue;}
  digitalWrite(rele,0);
  Serial.write(0);
  while (digitalRead(sens) == 0){continue;}
  Serial.write(1);
}

void output_bt() {
  Serial.println(digitalRead(bt));  // Lê o estado so botão
}

void output_sens() {
  Serial.println(digitalRead(sens)); // Lê o estado do sensor
}

void conf_receive() { // Envia 1 Bit para a serial
  Serial.write(1);
}

void solenoide() {  // solenoide
 while (true){
  if(digitalRead(bt) == 1){
    if (digitalRead(rele) == 1){
      digitalWrite(rele,0);
      }
    else{digitalWrite(rele,1);}
    }  
  }
}