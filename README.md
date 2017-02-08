# Zim-Scripts
Contains scripts related to Zim desktop wiki

showNewFiles.py: prints the latest edited notes. In command line prints to the console. In Zim (using custom tools), prints in the active page (replacing the selected text)

# Usage 
1- usage in Zim custum tools:
    add the following line to a new costum tool:
        ~/showNewFiles.py %n 10 
    check the box which says: Output should replace the current selection
    in any page that you want to see the output select a dummy text, then run the tool and it will replace
    the selected text with the links to the last n (here: 10) modified pages. To make the links effective, press 
    CTRL+R to refresh the page.
    
2- usage commandline (returns the last 10 newly edited pages) :  ~/showNewFiles "~/Dropbox/Notes/"  10        
