class Car(object):

    def __init__(self,modal,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.modal=modal
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")
        "accelerator functionality here"
    def change_gear(self,gear_type):
        print("gear change")
aud=Car("A6","red","audi",80)
print(aud.stop())