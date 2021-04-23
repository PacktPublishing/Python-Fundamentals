class MobilePhone:
    def __init__(self, memory):
        self.memory = memory


class Camera:
    def take_picture(self):
        print("Say cheese!")


class CameraPhone(MobilePhone, Camera):
    pass


iphone = CameraPhone('16GB')

print(iphone.memory)
iphone.take_picture()