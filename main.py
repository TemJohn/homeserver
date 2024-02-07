#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "John Hall"
__version__ = "0.1.0"


import tkinter as tk
from tkinter import filedialog
import os


def main():
    """ Main entry point of the app """
    # print("hello world")
    readFile()
    # print("End of function")

    # Need a main while loop to run continuously
    # what does the program do?
    #   * Rename media files to appropriate titles
    #   * Add media details like Artist/Focus Person, Date, Group/Album
    #   * Move media files from Contemplative to GlossyGrape, including putting them in the right folder
    #   * Ensure formatting is correct
    # 
    # How does it do this?
    #   * Use a text or csv file to direct the file attributes
    #   * Passively monitor the directory for that attributes file and the media files
    # 
    # Naming format: 
    # Music/ArtistName/AlbumName/TrackNumber - TrackName.ext
    # For the home videos:
    # HomeVideos/Grandchild/DiskTheme/TrackNumber - EventName.ext


def readFile():
    root = tk.Tk()
    root.withdraw()

    # file_path = filedialog.askopenfilename()
    # print(file_path)
    # Printed as:D:/Media/HomeVideo/data.txt
    file_path = 'D:/Media/HomeVideo/data.txt'
    file_name = os.path.split(file_path)[1] #splits into (head,tail), get tail
    # print(file_name)
    #data.txt
    # print(os.path.split(file_path)[0])
    #D:/Media/HomeVideo

    # f = open(file_path, 'r') #old format for opening files
    with open(file_path, 'r') as f:
        file_content = f.readlines()

    # file_content is a list[str]

    # List items are ordered, changeable, and allow duplicate values
    # Dict is a set of key-value pairs
#    thisdict = dict(Grandchild = "", age = 36, country = "Norway")

    # Fill the disk_info with TrackInformation
    # Get the grandchild and disk theme, which will be repeated for every track
    this_grandchild = file_content[0].replace('/','').replace('\n','')
    this_disk_theme = file_content[1].replace('/','').replace('\n','').strip()

    # disk_information will be a list of TrackInformation
    disk_information = []
#    disk_information.append("")
    # for x in fruits:
    #   print(x)

    header_counter = 2
    trackline = True
    for x in file_content:
        # Skip the first 2 lines
        if header_counter > 0:
            header_counter -= 1
            continue

        # In the track info there are alternating lines, trackline and dateline
        if trackline:
            current_track = x.partition(' - ')
            # splits into ['/#', ' - ', 'EventName']
            # should strip whitespace? 
            current_track_number = current_track[0].replace('/','').replace('\n','').strip()
            current_event_name = current_track[2].replace('\n','').strip()
            trackline = False
        else:
            # can only update TrackInformation (and thus disk_information) once we have the date
            current_date = x.replace('/','').replace('\n','').strip()
            t = TrackInformation(this_grandchild, this_disk_theme, current_track_number, current_event_name, current_date)

            disk_information.append(t)
            trackline = True

    # End of disk information collection
    for x in disk_information:
        print(x)




class TrackInformation:
    def __init__(self, grandchild, disk_theme, track_number, event_name, event_date):
        self.grandchild = grandchild
        self.disk_theme = disk_theme
        self.track_number = track_number
        self.event_name = event_name
        self.event_date = event_date

    def __str__(self):
        return "% s, % s, % s, % s, % s" % (self.grandchild, self.disk_theme, self.track_number, self.event_name, self.event_date)  
        

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


