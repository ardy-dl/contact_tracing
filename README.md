# Contact_tracing_app
###### Required:  Create “your” own covid contact tracing app with GUI 
###### - Create a program that ask user for typical information found in covid contact tracing app
###### - Write the collected information in a file (use any format you like)
###### - The app should be able to add and search entry

## How it works?
- This app is recommended only for single establishments/boutiques inside a mall but not for the whole mall since the destination part in the hdf
doesn't have a search function and we all know that when inside a mall customers enter from boutiques to boutiques. Therefore, it is best used for single establishments or boutiques only.
- The content_class.py contains all the functions needed for processing the data of the Health Declaration Form
- from the content class, the data are then transferred to hdf_gui.py file containing the HDFApp Class that binds together the functions and GUI
- The submit button(submit_form method)
          - saves the data inputted by the user
          - automatically saves the date and time in the csv file
          - clears out the form for the next user
  - The search_gui.py contains all the functions and GUI related to the search function 
  - The main.py has the shortest code but this is where all functions and GUI are binded together
  - user_info.csv is where the data are all stored

## How to use?
1. Run the program from the main.py file.
2. A small window will appear with two buttons:
     - Fill Out HDF
         - a. After filling out the HDF form click the submit button and you're all done.
     - Search Entries
         - a. JUAN DELA CRUZ - For searching names, it is required to write in the uppercase(All caps) format since the entries for names uses the .upper() function to avoid searching errors.
         - b. 07-23 - For searching date, type in the format (MM-DD) as it is the format followed by the system and is recorded in the csv.
                
