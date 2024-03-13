const int ledPin = LED_BUILTIN;
const int blinkDelay = 50;
const int pauseDelay = 250;
const int loopDelay = 5000;
const int baud = 9600;
const int buttonPin = 0;

int buttonState = 0;
int lastButtonState = 0;

unsigned long previousMillis = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(baud);
  testUsbConnection();
}

void loop() {

  buttonState = digitalRead(buttonPin);

  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button went from off to on:
      Serial.println("on");
    } else {
      // if the current state is LOW then the button went from on to off:
      Serial.println("off");
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = buttonState;

  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= loopDelay) {
    previousMillis = currentMillis;
    testUsbConnection();
  }
}

void testUsbConnection() {
  Serial.println("test");
  for (int i = 0; i < 3; i++) {
    digitalWrite(ledPin, HIGH);
    delay(blinkDelay);
    digitalWrite(ledPin, LOW);
    delay(pauseDelay);
  }
}