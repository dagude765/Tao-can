class tryr:

    def __init__ (self,name): # __ 两个

        self.name=name

         

    def lastName(self):

        return self.name.split()[-1]

         

BILL=tryr('BIGG SSID')

print(BILL.lastName())
