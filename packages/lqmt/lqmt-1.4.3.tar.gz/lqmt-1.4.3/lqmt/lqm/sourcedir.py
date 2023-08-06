from . import processed
import os
from .sources import Source
from lqmt.lqm.exceptions import ConfigurationError
import logging


class FilesToProcess(object):
    """Implements a directory traversal of each of the top-level dirs this object is initialized with"""

    def __init__(self, dirs, postProcess):
        self._iters = []
        self._dirs = dirs
        self._dirIter = iter(self._dirs)
        self._curFiles = None
        self._curDir = None
        self._postProcess = postProcess
        self.numFiles = 0
        self.numDirs = 0

        self._getNextTLD()

    def _getNextTLD(self):
        # get the next top-level directory
        self._currentTLD = next(self._dirIter)
        # and put the iterator for the list of files in the directory on the _iters list
        self._iters.append((self._currentTLD, iter(os.listdir(self._currentTLD))))

    def _advanceToNextFile(self):
        """Advance to the next file"""
        found = False
        while not found:
            # while a valid file pair (file/metadata file) has not been found
            # get the last dir & iter on the iters list
            dirName, cDirIter = self._iters[-1]
            try:
                # get the next entry from the dir
                entry = next(cDirIter)
                path = dirName + "/" + entry
                if os.path.isdir(path):
                    # if it is a path and it is not to be skipped,
                    # append an iterator of the directory's contents
                    if not self._postProcess.skipDirectory(path):
                        self._iters.append((path, iter(os.listdir(path))))
                elif not entry.startswith("."):
                    # otherwise, if the entry doesn't start with a '.'
                    if os.path.isfile(path):
                        # and it is a file, check to see if a metadata file exists
                        if os.path.exists(dirName + "/." + entry):
                            # if there is a matching metadata file
                            # check to see if we have left a directory
                            if self._curDir != dirName:
                                # if we have, then tell the post processor
                                if self._curDir is not None:
                                    self._postProcess.leavingDirectory(self._curDir)
                                self._curDir = dirName
                                self._postProcess.enteringDirectory(self._curDir)
                                self.numDirs += 1
                            self._curDir = dirName
                            # if the file hasn't already been processed, then we found the next file
                            if not self._postProcess.isProcessed(path):
                                # so set the flag to exit the loop and save the file info for retrieval
                                found = True
                                self._curFiles = (path, dirName + "/." + entry)
            except StopIteration:
                # if the iteration of the current dir is done
                # get the next dir, if any, and continue
                self._iters.pop()
                if len(self._iters) == 0:
                    self._getNextTLD()
        if not found:
            if self._curDir is not None:
                self._postProcess.leavingDirectory(self._curDir)
            raise StopIteration()

    def getNextFile(self):
        self._advanceToNextFile()
        self.numFiles += 1
        return self._curFiles

    def __iter__(self):
        return self

    def __next__(self):
        return self.getNextFile()


class DirectorySource(Source):
    """ This source provides an iterator for all the file pairs (alert/metadata) contained in all of
    its children that haven't already been processed (as determined by the post-processor specified
    in its configuration)."""

    def __init__(self, config):
        self._logger = logging.getLogger("LQMT.Source.Directory")
        self.files_to_process = None
        self.post_process = "move"
        # TODO: Have post_process_location also be used to define where the 'move' post_process option moves files
        self.post_process_location = "./processed"

        if 'dirs' not in config:
            raise ConfigurationError("Missing required key: 'dirs' in section: 'Source.Directory'")
        self._dirs = config["dirs"]
        hasError = False
        for dirName in self._dirs:
            if not os.path.exists(dirName):
                self._logger.error('dir ({0}) is not a valid path'.format(dirName))
                hasError = True
        if hasError:
            raise ConfigurationError("Configuration error with Source.Directory")

        if 'post_process' in config:
            self.post_process = config["post_process"]
            if self.post_process not in ["move", "delete", "track", "nothing"]:
                raise ConfigurationError(
                    "Invalid value for key: 'post_process' in section: 'Source.Directory': " + self.post_process)

        if 'post_process_location' in config:
            self.post_process_location = config['post_process_location']
        else:
            if self.post_process == "track":
                self._logger.info(" Post process option is currently set to track, but a post_process_location was not"
                                  "provided in the user configuration. Using the default location of "
                                  "{0}".format(self.post_process_location))

        self._processedHandler = self._getProcessedHandler()

    def getFilesToProcess(self):
        self.files_to_process = FilesToProcess(self._dirs, self._processedHandler)
        return self.files_to_process

    def _getProcessedHandler(self):
        if self.post_process == "move":
            return processed.ProcessHandlerMove()
        elif self.post_process == "delete":
            return processed.ProcessHandlerDelete()
        elif self.post_process == "track":
            return processed.ProcessHandlerTrackFile(self.post_process_location)
        else:
            return processed.ProcessHandlerDoNothing()

    def processed(self, datafile):
        self._processedHandler.processed(datafile)

    def logStatistics(self, numAlerts):
        self._logger.info(
            "dirs: {0} Directories Scanned: {1}, Files located: {2}".format(
                ",".join(self._dirs),
                self.files_to_process.numDirs,
                self.files_to_process.numFiles
            )
        )
