## DuplicateFileDir

Plugin for [fman.io](https://fman.io) to make a duplicate of the current file or directory. The new file or directory will have **-copy** added to it's name.

Install by uploading "DuplicateFileDir" to your [data directory](https://fman.io/docs/customizing-fman)`/Plugins`.

### Usage

Select one or more files or directorys and press **`<shift>+u`**

**Warning**: Currently it runs in the same process/thread so be aware that running properties on a large dir will cause the UI to hang while calculating size

### Features

 - Creates a duplicate of the current file or directory.

### Problems

- If you duplicate a directory, delete the duplicate, then try to duplicate it again, python errors out. If you exit fman and relaunch fman, you can duplicate the directory again. I believe it's an issue with Python caching information from the disk. I don't know how to fix it. Anyone have an idea?
