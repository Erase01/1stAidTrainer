import serial

def serRead():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting < 0:
            signal = ser.readlines().decode('utf-8')
            return signal
