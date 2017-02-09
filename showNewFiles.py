# -*- coding: utf-8 -*-
'''
1- usage in Zim custum tools:
    download the showNewFiles.py file. Under linux don't forget to make it executable, chmod +x showNewFiles.py. 
    
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
    '''
    

import os
##directory="~/Dropbox/Notes"
#directory="."
#files=[os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(directory)) for f in fn]

#for root, dirs, files in os.walk('.'):
#    print root, dirs, files
    

#fileDate=[[f,os.path.getmtime(f)] for f in files ]

#dates=[os.path.getmtime(f) for f in files ]
#dates=[]
#i=0
#for fileWithPath in files:
#    i=i+1
#    dates.append([os.path.getmtime(fileWithPath),fileWithPath,i ])
#dates.sort()

import heapq
import sys


#directory="~/Dropbox/Notes/"
directory=sys.argv[1]+'/'
NoOfResultNotes=int(sys.argv[2])

fileDate=[]
for dp, dn, fn in os.walk(os.path.expanduser(directory)):
    for f in fn:
        fileWithPath=os.path.join(dp,f)
        if not( ('.git' in dp) or ('.svn' in dp) ):
            fileDate.append([os.path.getmtime(fileWithPath),fileWithPath, f ])#,dp,dn, fn])
#fileDate.sort(reverse=True)
#newest=fileDate
newest=heapq.nlargest(NoOfResultNotes, fileDate)
for i in range(NoOfResultNotes):        
#    print fileDate[i][1]
    noteAddress=newest[i][1].split(os.path.expanduser(directory),1)
    noteAddress=noteAddress[1].split('.txt',1)[0]
    noteAddress=noteAddress.replace('/',':')
    noteAddress=noteAddress.replace('\\',':')
    out='[['+noteAddress+']]'
    print out
    
