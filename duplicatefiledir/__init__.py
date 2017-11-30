from fman import DirectoryPaneCommand, show_alert
from urllib.parse import urlparse
import os.path
from shutil import copytree, copyfile

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
                p = urlparse(filedir)
                filepath = os.path.abspath(os.path.join(p.netloc, p.path))
                if os.path.isdir(filepath):
                    #
                    # It is a directory. Process as a directory.
                    #
                    newDir = filepath + "-copy"
                    copytree(filepath, newDir)
                else:
                    if os.path.isfile(filepath):
                        #
                        # It is a file. Process as a file.
                        #
                        dirPath, ofilenmc = os.path.split(filepath)
                        ofilenm, ext = os.path.splitext(ofilenmc)
                        nfilenm = os.path.join(dirPath,ofilenm + "-copy" + ext)
                        copyfile(filepath, nfilenm)
                    else:
                        show_alert('Bad file path : {0}'.format(filepath))
