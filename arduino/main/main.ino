int baud = 9600;


void setup()
{
    // initialize digital pin LED_BUILTIN as an output.
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(baud);

    testUsbConnection();
}

void loop()
{
  delay(5000);
  testUsbConnection();
}

void testUsbConnection()
{
  Serial.println("test");
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
    delay(50);                     // wait for a second
    digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
    delay(250); 
  }
}