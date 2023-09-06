import serial
import matplotlib.pyplot as plt
from PIL import Image
import json


# change this when we get ecg system i guess
ser = serial.Serial('COM1', baudrate=9600)
ecg_data = ser.read(1000)

plt.plot(ecg_data)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ECG')
plt.grid(True)

plt.savefig('ecg_plot.jpg')

# need work on saving data when we understand what exactly data we need to store
ecg_info = {
    'patient_id': '12300',
    'timestamp': '06-09-2023 10:00',
    'ecg_data_file': 'ecg_plot.jpg',
    'other_info': ' . . . '
}

with open('ecg_plot.jpg', 'w') as json_file:
    json.dump(ecg_info, json_file)


# TODO: create simple web server and API for getting data on apps
