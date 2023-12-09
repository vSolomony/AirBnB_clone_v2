#!/usr/bin/python3
"""
This module contains the command interpreter class for the hbnb project
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex
import json
import re

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for hbnb project"""

    prompt = "(hbnb) "
    allowed_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass

    def do_EOF(self, line):
        """Exits the console using Ctrl+D or EOF"""
        print("")
        return True

    def do_quit(self, line):
        """Exits the console"""
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("Exits the console using Ctrl+D or EOF")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key in objects:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = shlex.split(line)
        objects = FileStorage().all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        filtered_objs = [
            str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name
        ]
        print(filtered_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = FileStorage().all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(objects[key], attribute_name, attribute_value)
        FileStorage().save()

    def do_count(self, line):
        """Counts the number of instances of a class"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        objects = FileStorage().all()
        count = sum(
            1 for obj in objects.values() if obj.__class__.__name__ == class_name
        )
        print(count)

    def default(self, line):
        """Default behavior for unknown commands"""
        regex = r"^(\w+)\.(\w+)\(([^)]*)\)$"
        match = re.match(regex, line)
        if match:
            groups = match.groups()
            class_name = groups[0]
            method_name = groups[1]
            method_args = groups[2].replace('"', "").replace("'", "").split(", ")
            objects = FileStorage().all()
            key = "{}.{}".format(class_name, method_args[0])
            if key not in objects:
                print("** no instance found **")
                return
            obj = objects[key]
            if method_name == "update":
                if len(method_args) < 2:
                    print("** attribute name missing **")
                    return
                attribute_name = method_args[1]
                if len(method_args) < 3:
                    print("** value missing **")
                    return
                attribute_value = method_args[2]
                try:
                    attribute_value = eval(attribute_value)
                except (NameError, SyntaxError):
                    pass
                setattr(obj, attribute_name, attribute_value)
                FileStorage().save()
            elif method_name == "all":
                print(
                    [
                        str(obj)
                        for obj in objects.values()
                        if obj.__class__.__name__ == class_name
                    ]
                )
            elif method_name == "show":
                print(obj)
            elif method_name == "destroy":
                del objects[key]
                FileStorage().save()
            elif method_name == "count":
                count = sum(
                    1
                    for obj in objects.values()
                    if obj.__class__.__name__ == class_name
                )
                print(count)
            else:
                print("** unknown command **")
        else:
            print("** unknown command **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

