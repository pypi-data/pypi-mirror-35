import os
import platform
import logging
import shutil
import re
import sys
import time
from threading import Thread

if platform.system() == 'Windows':
    import winreg
    import psutil
    import easygui

APP_TITLE = "PHISHERMON"

# Logging setup
log = logging.getLogger('phishermon')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)


class MitigateProcess(object):

    def __init__(self):
        pass

    def prompt_kill_process(self, pid, process_name):
        """Asks user if they want terminate the suspicious process.
        
        :param pid: The process ID to be killed.
        :type pid: int
        :param process_name: The name of the process to be killed.
        :type process_name: str

        :returns: True or False depending on whether it was able to kill the process. 
        """

        if psutil.pid_exists(pid) and psutil.Process(pid).name() == process_name:
            self.suspend_process(pid, process_name)

            if self._show_alert_process(pid, process_name):
                self.kill_process(pid, process_name)
                return True
            else:
                self.resume_process(pid,process_name)
                log.info("User did not want to end process: {}-{}".format(process_name, pid))
                return False
        else:
            log.warning("Process: {} with ID: {} does not exist".format(process_name, pid))
            return False

    def _show_alert_process(self, pid, process_name):
        """Helper function displays a prompt asking user if they would like to stop the selected process.
        
        :param pid: The process ID to be killed.
        :type pid: int
        :param process_name: The name of the process to be killed.
        :type process_name: str
        
        :returns: True if the user decided to kill the process, False otherwise.
        """

        msg = ["Phishermon found a suspicious application, would you like to close it?\n",
               "Process Name: {}".format(process_name), 
               "Process ID: {}".format(pid), 
               "{}".format(APP_TITLE)]

        msg = '\n'.join(msg)

        decision = easygui.ccbox(msg)
        return decision

    def kill_process(self, pid, process_name, recursive=False):
        """Helper function that kills process and its children.
        
        :param pid: The process ID to be killed.
        :type pid: int
        :param process_name: The name of the process to be killed.
        :type process_name: str
        :param recursive: If True will kill all child processes of the specified process
        :type recursive: bool
        """

        if pid == os.getpid():
            log.info("I refuse to kill myself")

        if not (type(pid) is int):
            raise RuntimeError("The input must be an integer value representing the Process ID to kill")

        if psutil.pid_exists(pid) and psutil.Process(pid).name() == process_name:
            parent = psutil.Process(pid)

            if recursive:
                for child in parent.children(recursive=True):
                    child.kill()
            parent.kill()

        else:
            log.warning("Process: {} with ID: {} does not exist".format(process_name, pid))

    def suspend_process(self, pid, process_name):
        """Helper function that suspends a process.
        
        :param pid: The process ID to be killed.
        :type pid: int
        :param process_name: The name of the process to be killed.
        :type process_name: str        
        """

        if pid == os.getpid():
            print("I refuse to suspend myself")

        if not isinstance(pid, int):
            raise RuntimeError("The input must be an integer value representing the Process ID to kill")

        if psutil.pid_exists(pid) and psutil.Process(pid).name() == process_name:
            parent = psutil.Process(pid)
            parent.suspend()

        else:
            log.warning("Process: {} with ID: {} does not exist".format(process_name, pid))

    def resume_process(self, pid, process_name):
        """Helper function to resume a suspended process
        
        :param pid: The process ID to be killed.
        :type pid: int
        :param process_name: The name of the process to be killed.
        :type process_name: str  
        """

        if not isinstance(pid, int):
            raise RuntimeError("The input must be an integer value representing the Process ID to kill")

        if psutil.pid_exists(pid) and psutil.Process(pid).name() == process_name:
            parent = psutil.Process(pid)
            parent.resume()

        else:
            log.warning("Process: {} with ID: {} does not exist".format(process_name, pid))

    def get_process_id(self, process_name):
        """Finds process ID by process name, returns None if process not found"""

        for proc in psutil.process_iter():
            if proc.name() == process_name:
                print("Process: " + process_name + ", PID: " + str(proc.pid))
                return proc.pid

        log.warning("No process found with name: " + process_name)
        return None


class MitigateFile(object):

    def __init__(self):
        pass

    def prompt_delete_file(self, path):
        """Asks user if they want delete the suspicious file.
        
        :param path: The path to the file to be deleted
        :type path: str
        
        :returns: True if the file was deleted.
        """

        if self._show_alert_file(path):
            return self.delete_file(path)
        else:
            log.info("User did not want to delete file: {}".format(path))
            return False

    def _show_alert_file(self, path):
        """Helper function displays a prompt asking user if they would like to delete the selected file.
        
        :param path: The path to the file to be deleted
        :type path: str
        """

        text = "Phishermon has found a suspicious file or folder, would you like to delete it?\n\nFile path: {}\n".format(path)

        return easygui.ccbox(text, APP_TITLE)

    def delete_file(self, path):
        """Deletes a file, returns True if file was deleted"""

        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
                log.info("Deleted directory at: {}".format(path))
                return True
            else:
                os.remove(path)
                log.info("Deleted file at: {}".format(path))
                return True
        else:
            log.error("The path {} does not exist.".format(path))
            return False


class MitigateRegistry(object):

    def __init__(self):
        self.hive_regex = re.compile(r'(HKEY_[A-Z, _]*)(?:\\)(.*)')

    def prompt_delete_registry_key(self, path, key_to_delete):
        """Asks user if they want delete the suspicious registry key.
        
        :param path: The path to the key to be deleted
        :type path: str
        :param key_to_delete: The key to be deleted
        :type key_to_delete: str
        
        :returns: True if the registry key was deleted.
        """
        key = '{}\\{}'.format(path, key_to_delete)
        if self._show_alert_registry_key(key):
            return self.delete_registry_key(path, key_to_delete)
        else:
            log.info("User did not want to delete registry key: {}".format(key))
            return False

    def _show_alert_registry_key(self, path):
        """Helper function displays a prompt asking user if they would like to delete the selected registry key"""

        text = "Phishermon has found a suspicious registry key, would you like to delete it?\n\nRegistry key path: {}\n".format(path)


        return easygui.ccbox(text, APP_TITLE)

    def delete_registry_key(self, path, key_to_delete):
        """Deletes a registry key tree.
        
        :param path: The path to the key to be deleted
        :type path: str
        :param key_to_delete: The key to be deleted
        :type key_to_delete: str      
        """

        reg, folder = self._parse_reg_path(path)
        log.debug("Inside: {}\\{}".format(folder, key_to_delete))

        try:
            parent_folder = winreg.OpenKey(reg, folder, access=winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
            to_delete = winreg.OpenKey(reg, folder + '\\' + key_to_delete, access=winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)

            key_info = winreg.QueryInfoKey(to_delete)

            try:
                while True:
                    sub_key = winreg.EnumKey(to_delete, 0)
                    key = '{}\\{}'.format(path, key_to_delete)
                    self.delete_registry_key(key, sub_key)
            except:
                pass

            winreg.DeleteKey(parent_folder, key_to_delete)
            log.info("Deleted registry key: {}\\{}".format(folder, key_to_delete))
        except OSError as e:
            log.error("An error has occured \nError: {0}".format(e))

    def _parse_reg_path(self, path):
        """Parses a full registry key path"""

        match = re.search(self.hive_regex, path)

        if not match:
            raise RuntimeError("Path could not be parsed: " + path)

        hive_name = match.group(1)
        key = match.group(2)

        if hive_name == 'HKEY_CLASSES_ROOT':
            return winreg.HKEY_CLASSES_ROOT, key
        elif hive_name == 'HKEY_CURRENT_USER':
            return winreg.HKEY_CURRENT_USER, key
        elif hive_name == 'HKEY_LOCAL_MACHINE':
            return winreg.HKEY_LOCAL_MACHINE, key
        elif hive_name == 'HKEY_USERS':
            return winreg.HKEY_USERS, key
        elif hive_name == 'HKEY_PERFORMANCE_DATA':
            return winreg.HKEY_PERFORMANCE_DATA, key
        elif hive_name == 'HKEY_CURRENT_CONFIG':
            return winreg.HKEY_CURRENT_CONFIG, key
        else:
            raise RuntimeError("The hive {} does not exist in the Windows registry".format(hive_name))



















