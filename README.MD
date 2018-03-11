# Build an Item Catalog Application
Project of the Udacity Fullstack Developer Nano Degree Program.
To develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Assumptions
User knows and can execute Python 2, Vagrant, VirtualBox and have access Google and or Facebook accounts.

### Design of this Project
The application that provides a list of wines within a variety of categories, a brief description of the catergory, as well as provide a user registration and authentication system.
Selecting a specific category shows all the wines stored in the database for that category, the name, origin, tasting notes and price of the wines.
To create a new or to edit categories or wines, the user will have to log in and be authenticated from a third party application, either with a Google or Facebook account.
Only the creator of a particilar category or wine will be able to delete the category or wine.

### Project files are:
1. database_setup.py
	* the database setup (to store and organize the information)
2. lotsofwines.py
	* python file to populate the database
3. application.py
	* python file with the Flask Application, including authentication/authorization to allow users to login before making changes
4. templates folder
	* contains HTML (structure of the pages)
5. static folder
	* contains CSS (the style of the pages) and images
6. fb_client_secrets
	* api client ID and Key for user to login via Facebook account
7. client_secrets
	* api client ID and Key for user to login via Google account

### How to run the Project
1. Download the project file.
2. Unzip the project file to folder and put it in the directory which is shared with your virtual machine.
3. Launch the Vagrant VM (by typing vagrant up in the directory fullstack/vagrant from the terminal).
4. From the terminal, to load the data, cd into the virtual machine directory and use the command: *python database_setup.py*
5. It is optional to populate the database with the command: *python lotsofwines.py*
6. Run the application with the command: *python application.py*
7. Access the application by visiting http://localhost:8000 locally on your browser.

#### Acknowledgement
1. images from various Free Stock images websites
2. wines information from wikipedia and https://sg.epicurio.co

#### License
Free for distribution

#### Disclaimer
No liability will be accepted by the author.
