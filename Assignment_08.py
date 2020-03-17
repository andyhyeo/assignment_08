#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# AYeo, 2020-Mar-10 9:06 PM,  Added working CD class
# AYeo, 2020-Mar-10 1:52 PM,  Added Main Body from previous script
# AYeo, 2020-Mar-10 2:99 PM,  Added Structured Error Handling
# AYeo, 2020-Mar-15 9:29 PM, Fixed CD class to have property, private methods, setters
# AYeo, 2020-Mar-15 9:29 PM, Edited FileIO to use CD class, HAVE NOT TESTED
# AYeo, 2020-Mar-15 9:29 PM, Edited FileIO to use CD class, Successfully Tested
# AYeo, 2020-Mar-16 5:00 PM, Correct FileIO.load_inventory to use pickle, Successfully Tested
# AYeo, 2020-Mar-16 5:00 PM, Correct FileIO.save_inventory to use pickle, NOT TESTED 
# AYeo, 2020-Mar-16 5:00 PM, Correct FileIO.save_inventory to use pickle, Tested


#------------------------------------------#

# -- DATA -- #
# DBiesinger, 2030-Jan-01, created file
from os import path
import pickle

strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # -- Contructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #        
        self.__ID = cd_id
        self.__title = cd_title
        self.__artist = cd_artist

    # -- Properties -- #
    @property
    def ID(self):
        return self.__ID

    @property
    def title(self):
        return self.__title.title()  

    @property       
    def artist(self):
        return self.__artist.title()
    
    @ID.setter
    def ID(self, value):
        if str(value).isnumeric():
            self.__ID = value
        else:
            raise Exception('The ID must be numeric')
        
    @title.setter
    def title(self, value):
        if str(value).isnumeric():
            raise Exception('The title must be a string')
        else:
            self.__title = value
    
    @artist.setter
    def artist(self, value):
        if str(value).isnumeric():
            raise Exception('The artist must be a string')
        else:
            self.__artist = value
            
    # -- Methods -- #
    def __str__(self):
        return self.ID
        return self.title
        return self.artist


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """    
        try:
            with open(file_name, 'rb') as objFile:
                table = pickle.load(objFile)
                return table
        except FileNotFoundError:
            pass

    @staticmethod
    def save_inventory(file_name, table):
        """Writes the inventory of IDs, CD Names, and Artists to a text file
        
        Args:
            file_name (string): The name of the file that it will write to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None but saves a file in the directory of the python script
            
        """
        with open(file_name, 'wb') as objFile:
            table = pickle.dump(table, objFile)
            
    
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for CD in table:
            print('{}\t{} (by:{})'.format(CD.ID, CD.title, CD.artist))
        print('======================================')

    @staticmethod
    def add_cd(row, table):
        """Adds a dictionary row to the inventory
        
        Args:
            row (dictionary): dictionary that holds the name of the ID, cd, and artist
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
            None.
            
        """
        table.append(row)
        return table
    
        
    @staticmethod
    def ask():
        """Ask user for new ID, CD Title and Artist
        
        Args:
            None
            
        Returns:
            CD (Object):  A dictionary entry with ID (int): integer that holds
            the ID tag,title (string): string that holds the name of the CD
                and an artist (string): string that holds the name of the Artist.
        """
        title = ''
        artist = ''
        while True:
            CD_id = input('Enter ID: ').strip()
            try: 
                CD_id = int(CD_id)
                break
            except ValueError:
                print('That is not an integer')
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        CD_row = CD(CD_id, title, artist)
        return CD_row

class DataProcessor:
    @staticmethod
    def delete_cd(intIDDel,table):
        """Deletes a CD row from the table
        
        Args:
            intIDDel (int): ID which indicate which entry user would like to delete
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
              table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """ 
        intRowNr = -1
        blnCDRemoved = False
        for CD in table:
            intRowNr += 1
            if CD.ID == intIDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('Could not find this CD!')    
        return table

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        row = IO.ask()
        # 3.3.2 Add item to the table
        IO.add_cd(row,lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        while True:
            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
                break
            except ValueError:
                print('That is not an integer')
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_cd(intIDDel,lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
