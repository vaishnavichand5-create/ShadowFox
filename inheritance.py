# Base Class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera")


# Child Class - Apple
class Apple(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print("\nApple Device:", self.model)
        print(self.__dict__)


# Child Class - Samsung
class Samsung(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print("\nSamsung Device:", self.model)
        print(self.__dict__)


# ---------------- OBJECTS ----------------

# Apple objects
iphone1 = Apple("iPhone 14", "Touch Screen", "5G", True, "12MP", "48MP", "4GB", "128GB")
iphone2 = Apple("iPhone 13", "Touch Screen", "4G/5G", True, "12MP", "12MP", "4GB", "64GB")

# Samsung objects
galaxy1 = Samsung("Galaxy S22", "Touch Screen", "5G", True, "16MP", "64MP", "8GB", "256GB")
galaxy2 = Samsung("Galaxy A52", "Touch Screen", "4G", True, "12MP", "48MP", "6GB", "128GB")


# ---------------- FUNCTION CALLS ----------------

iphone1.show_details()
iphone1.make_call()
iphone1.take_a_picture()

galaxy1.show_details()
galaxy1.receive_call()
galaxy1.take_a_picture()