# rename_subtitles on windows machine. Not tested on any other OS
# * A simple script to organize my courses directory, creating a folder for subtitles and then moving them to it
# my directory tree is organized this way: [Courses main Directory] -> [Course Directory] -> [Topic Directory]

import glob
import os
import shutil

# Course main directory. Hard coded for convenience
root = r"C:\Media\Courses"

# list subfolders
dirs = os.listdir(root)

for dir in dirs:

    # Course directory. os.path.join is basicly a path concatenation
    root_dir = os.path.join(root, dir)

    print("Working on: " + root_dir)

    folders = os.listdir(root_dir)

    for folder in folders:

        # Topic directory
        path = os.path.join(root_dir, folder)

        subs_path = os.path.join(path, "subtitles")

        # if a folder called "subtitles" already existis, os.mkdir returns an exception
        try:
            os.mkdir(subs_path)
            print("\tDirectory " + subs_path + " was created")
        except:
            print("\tDirectory " + subs_path + "  already existed")

        #! all my subs have .srt or .vtt file extention. For more than 2 formats, an list would be better than individual vars.
        sub_files_srt = path + "\\*.srt"
        sub_files_vtt = path + "\\*.vtt"

        # create a vector with all files with that extention
        subtitles_vtt = glob.glob(sub_files_vtt)
        subtitles_srt = glob.glob(sub_files_srt)

        # move the files to the subtitles folder
        for file in subtitles_srt:
            shutil.move(file, subs_path)
        for file in subtitles_vtt:
            shutil.move(file, subs_path)
