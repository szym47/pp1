class Phone():
    def __init__(self,brand,model,size):
        self.brand=brand
        self.model=model
        self.size=size
        self.battery_lvl=47
        self.is_charging=False
        self.wifi_connected=False
    def charge(self):
        self.is_charging=True
    def stop_charge(self):
        self.is_charging=False
    def connect(self):
        self.wifi_connected=True
    def connect(self):
        self.wifi_connected=True
    def change_battery(self,b_lvl):
        self.battery_lvl=b_lvl

phone= Phone('Iphone','12 Pro','6inch')
print(f'I have {phone.brand} {phone.model} that have {phone.size}.')
phone.charge()
phone.change_battery(69)
if phone.is_charging:
    print(f'My phone have now {phone.battery_lvl}%')