import serial
import platform
import time

ARDUINO_PORT = "COM7" if platform.system() == "Windows" else "/dev/ttyACM0"
BAUDRATE = 115200

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUDRATE)
    time.sleep(2)
    print("Succes: The Arduino has connected succesfully!")
except Exception as e:
    print(f"An error has occured during the opening of serial port: {e}")

def send_command(text:str, encoding="utf-8"):
    try:
        arduino.write(text.encode(encoding))
        print("Succesfully send the message to arduino!")
        return "Success"
    except Exception as e:
        print(f"An error has occured during the sending of the message in arduino: {e}")
        return "Error"

def read_command(decoding="utf-8"):
    try:
        return arduino.readline().decode(decoding).strip()
    except Exception as e:
        print(f"An error has occured during the reading of the message from arduino: {e}")
        return "Error"
