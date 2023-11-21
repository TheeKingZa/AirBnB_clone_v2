#!/usr/bin/python3
# console.py
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in the usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formatting - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parentheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as an empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit the program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    # Updated do_create to handle object creation with given parameters
    def do_create(self, args):
        """ Create an object of any class with parameters"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Extract class name and parameters from the input
        class_name, *params = args.split()

        # Create an instance of the specified class
        new_instance = HBNBCommand.classes[class_name]()

        # Process parameters and set attributes of the instance
        for param in params:
            # Split the parameter into key and value
            key, value = param.split('=')

            # Handle special cases for string values
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')

            # Type cast as necessary
            if key in HBNBCommand.types:
                value = HBNBCommand.types[key](value)

            # Update the attribute of the instance
            setattr(new_instance, key, value)

        # Save the instance to the storage
        storage.save()

        # Print the id of the created instance
        print(new_instance.id)

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split(' ')[0]  # remove possible trailing args

        class_name = args_list[0]

        if args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print_list = []

        if len(args_list) > 1:
            key = class_name + "." + args_list[1]
            try:
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")
            return

        # Retrieve instances based on the class name
        instances = storage.all().values()
        for instance in instances:
            if instance.__class__.__name__ == class_name:
                print_list.append(str(instance))

        if not print_list:
            print("** no instance found **")
        else:
            print(print_list)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type with given parameters")
        print("[Usage]: create <className> <param1>=<value1> <param2>=<value2> ...\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
