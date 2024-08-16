############################################################################
# Autor: Niclas Bork - https://github.com/niclasbork                       #
# Created: 13.08.24                                                        #
# Last modified: 14.08.24                                                  #
# This program is free software; you can redistribute it and/or modify     #
# it under the terms of the GNU General Public License as published by     #
# the Free Software Foundation version 2                                   #
############################################################################

from utils import classes as cl

root = cl.App('Welcome to the Contacts-App. What do you want to do?', 70)
root.importFile()
root.prettyPrint()
root.displayMenu()
