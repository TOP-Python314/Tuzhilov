from datetime import date, time, datetime
import decimal 

class PowerMeter:

    def __init__(self, tariff1= 4.35, tariff2= 3.21, tariff2_starts = time(23, 0), tariff2_ends = time(7, 0)):
        self.tariff1 = decimal.Decimal(tariff1)
        self.tariff2 = decimal.Decimal(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = decimal.Decimal(0)
        self.charges = {}
        
    def __repr__(self):
        return f'<PowerMeter: {self.power} кВт/ч>'
    
    def __str__(self):
        return f'({datetime.today().strftime("%b")}), {datetime.today().strftime("%Y, %m")}'
    
    def meter(self, power):  
        power = decimal.Decimal(power)
        self.power = power
        
        current_time = datetime.now().time()
        
        if self.tariff2_starts <= current_time or current_time <= self.tariff2_ends:
            charge = power * self.tariff1
        else:
            charge = power * self.tariff2
            
        today = date.today()
        self.charges[today] = self.charges.get(today, decimal.Decimal(0)) + charge
        
        return charge.quantize(decimal.Decimal('1.00'))
        
# >>> pm2 = PowerMeter()
# >>>
# >>> pm.meter(2)
# Traceback (most recent call last):
# >>> pm2.meter(2)
# Decimal('6.42')
# >>> pm2.meter(1.5)
# Decimal('4.81')
# >>>
# >>> pm2
# <PowerMeter: 1.5 кВт/ч>
# >>> print(pm2)
# (Jul), 2024, 07