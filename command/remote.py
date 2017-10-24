from .commands import NoCommand

class SimpleRemoteControl:
    def __init__(self):
        self.slot = None
    
    def set_command(self, command):
        self.slot = command
    
    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    
    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_command = NoCommand()
        
        self.no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(self.no_command)
            self.off_commands.append(self.no_command)
            
    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
        
    def on__button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]
        
    def off__button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]
        
    def undo__button_was_pushed(self, slot):
        self.undo_command.undo()
        
    def __str__(self):
        descr = ["\n------ Remote Control -------\n"]
        for i in range(len(self.on_commands)):
            descr.append("[slot " + str(i) + "]" + self.on_commands[i].__class__.__name__
                         + " " + self.off_commands[i].__class__.__name__ + "\n")
        
        return descr

        