from .commands import LightOnCommand, GarageDoorUpCommand, LightOffCommand, GarageDoorDownCommand, CeilingFanOnCommand, CeilingFanOffCommand, StereoOnCommand, StereoOffCommand, StereoSetCdCommand
from .receivers import Light, GarageDoor, CeilingFan, Stereo
from .remote import SimpleRemoteControl, RemoteControl

if __name__ == "__main__":
    
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)
    garage_door = GarageDoor()
    garage_door_open = GarageDoorUpCommand(garage_door)
    
    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_door_open)
    remote.button_was_pressed()
    
    remote_control = RemoteControl()
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door2 = GarageDoor("")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)
    garage_door2_up = GarageDoorUpCommand(garage_door)
    garage_door2_down = GarageDoorDownCommand(garage_door)
    stereo_on = StereoOnCommand(stereo)
    stereo_off = StereoOffCommand(stereo)
    
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on, stereo_off)
    
    print(remote_control)
    
    remote_control.on__button_was_pushed(0)
    remote_control.off__button_was_pushed(0)
    remote_control.on__button_was_pushed(1)
    remote_control.off__button_was_pushed(1)
    remote_control.on__button_was_pushed(2)
    remote_control.off__button_was_pushed(2)
    remote_control.on__button_was_pushed(3)
    remote_control.off__button_was_pushed(3)
