# Zim-Scripts
Contains scripts related to Zim desktop wiki

showNewFiles.py: prints the latest edited notes. In command line prints to the console. In Zim (using custom tools), prints in the active page (replacing the selected text)

# Usage 

1- usage in Zim custum tools:
    download the showNewFiles.py file. Under linux don't forget to make it executable, `chmod +x showNewFiles.py`. 
    
    add the following line to a new costum tool:
    
    * under linux: 
        ~/showNewFiles.py %n 10
    * under windows: if it is in a path for example "c:" 
        python c:\showNewFiles.py %n 10

    check the box which says: Output should replace the current selection
    in any page that you want to see the output select a **temporary text**, then run the tool and it will replace
    the selected text with the links to the last n (here: 10) modified pages. To make the links effective, press 
    CTRL+R to refresh the page.
    
2- usage commandline (returns the last 10 newly edited pages) :  ~/showNewFiles "~/Dropbox/Notes/"  10        
