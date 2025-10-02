import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        return[int(element) for element in bin(number)[2:].zfill(8)]

    def set_voltage(self, voltage):
        number = int(voltage / self.dynamic_range * 255)
        GPIO.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])

if __name__ == "__main__":
    try:
        dac = R2R_DAC([12, 20, 21, 25, 26, 17, 27, 22], 3.166, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                 print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()