#!/usr/bin/python3
""" The console """
import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex
classes = ["Amenity", "BaseModel", "City",
           "Place", "Review", "State", "User"]


class HBNBCommand(cmd.Cmd):
    """ The console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ Will jump to a new command line when empty line is encountered
        """
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel class or
        instances of classes which inherits BaseModel class"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
            return False

        if command[0] in classes:
            objct = eval(command[0])()
        else:
            print("** class doesn't exist **")
            return False

        print(objct.id)
        objct.save()

    def do_show(self, arg):
        """Prints the string representation of an object
        stored in the engine based on its class and id
        """
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
            return False

        if command[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(command) == 1:
            print("** instance id missing **")
            return False

        key = f'{command[0]}.{command[1]}'
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return False
        else:
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an object stored based on its class and id.
        The changes will be saved to the Json file"""
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
            return False

        if command[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(command) == 1:
            print("** instance id missing **")
            return False

        key = f'{command[0]}.{command[1]}'
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return False
        else:
            models.storage.all().pop(key)
            models.storage.save()

    def do_all(self, arg):
        """Prints string representations of all objects
        if command is empty or prints string representation
        of all objects of a class entered as a command
        """
        command = shlex.split(arg)
        str_list = []
        if len(command) == 0:
            for objct in models.storage.all().values():
                str_list.append(str(objct))

            all_obj_str = ", ".join(str_list)
            print(f'[{all_obj_str}]')
            return False
        if command[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            for key in models.storage.all().keys():
                if command[0] in key:
                    objct = models.storage.all()[key]
                    str_list.append(str(objct))

            obj_str = ", ".join(str_list)
            print(f'[{obj_str}]')

    def do_update(self, arg):
        """Updates the values of attributes based on
        the class name, id, attribute and value.The
        update will be saved to the Json file.
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")

        if command[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(command) == 1:
            print("** instance id missing **")
            return False

        key = f'{command[0]}.{command[1]}'
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return False

        if len(command) == 2:
            print("** attribute name missing **")
            return False

        if len(command) == 3:
            print("** value missing **")
            return False

        setattr(models.storage.all()[key], command[2], command[3])
        models.storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
