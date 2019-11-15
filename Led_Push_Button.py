import RPi.GPIO as GPIO #Mengimpor library untuk pin GPIO
import time #mengimpor library untuk mengaktifkan fungsi time

GPIO.setmode(GPIO.BCM) #merujuk pada pin berdasarkan nomor "Broadcom SOC Channel"

GPIO.setwarnings(False) #menonaktifkan peringatan/warning
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(24, GPIO.OUT, initial = GPIO.HIGH)  #LED to GPIO24(Red)
GPIO.setup(25, GPIO.OUT, initial = GPIO.HIGH)  #LED to GPIO25(Yellow)
GPIO.setup(27, GPIO.OUT, initial = GPIO.HIGH)  #LED to GPIO27(Green)
x=1  

try:
    while True: #kondisi ketika True
         button_state = GPIO.input(23) #mendeklarasikan bahwa variabel button_state adalah GPIO.input di pin 23
         if button_state == False: #ketika tombol push ditekan
                 
                 #Kondisi awal ketika push button ditekan
                 GPIO.output(24, GPIO.LOW) #LED Red mati
                 GPIO.output(25, GPIO.HIGH) #LED Yellow menyala
                 GPIO.output(27, GPIO.LOW) #LED Green mati
                 time.sleep(2) #Waktu LED menyala

                 #Kondisi selanjutnya setelah 2 detik
                 GPIO.output(24, GPIO.HIGH) #LED Red menyala
                 GPIO.output(25, GPIO.LOW) #LED Yellow mati
                 GPIO.output(27, GPIO.LOW) #LED Green mati
                 time.sleep(3) #Waktu LED menyala

                #Kondisi selanjutnya setelah 3 detik
                 GPIO.output(24, GPIO.LOW) #LED Red menyala
                 GPIO.output(25, GPIO.LOW) #LED Yellow mati
                 GPIO.output(27, GPIO.HIGH) #LED Gren mati
                 print('Button Pressed...') #perintah untuk print tulisan "Button Pressed" pada terminal menandakan button tertekan

except:
    GPIO.cleanup() #memebersihkan port dan warning