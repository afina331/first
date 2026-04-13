import RPi.GPIO as GPIO
dac_bits = [17, 27, 22, 23, 24, 25, 5, 6]
dynamic_range=3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage/dynamic_range*255)

def number_to_dac(number):
    for i in range(8):
        bit_value=(number>>i)&1
        GPIO.output(dac_bits[i], bit_value)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

try:
    while True:
        try:
            voltage=float(input("введите напряжение в Вольтах: "))
            number=voltage_to_number(voltage)
            number_to_dac(number)
            
        except ValueError:
            print("попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()    