from fman import DirectoryPaneCommand, show_alert
from distutils.file_util import copy_file
from shutil import copytree
import os.path

class DuplicateFileDir(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            #
            # Loop through each file/directory selected.
            #
            for filedir in selected_files:
                if os.path.isdir(filedir):
                    #
                    # It is a directory. Process as a directory.
                    #
                    newDir = filedir + "-copy"
                    copytree(filedir,newDir)
                else:
                    #
                    # It is a file. Process as a file.
                    #
                    dirPath, ofilenmc = os.path.split(filedir)
                    ofilenm, ext = os.path.splitext(ofilenmc)
                    nfilenm = os.path.join(dirPath,ofilenm + "-copy" + ext)
                    copy_file(filedir,nfilenm)
