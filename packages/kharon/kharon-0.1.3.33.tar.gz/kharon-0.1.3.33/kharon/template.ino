//Imports
//IMPORT

//Global declarations
int channel, messageLen;
//GLOBALS


//Functions
//FUNCTIONS

void setup(){
    Serial.begin(9600);

    //Setup
    //SETUP
}

void loop(){

    //No Input


    if(Serial.available() >= 2){
        channel = Serial.read() << 8;
        channel += Serial.read();

        messageLen = Serial.read() << 8;
        messageLen += Serial.read();

        for(messageLen; messageLen > 0; messageLen--)


        switch(channel){
            //Input Cases
            //CASES

        }

    }

}