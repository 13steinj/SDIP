from __future__ import print_function
import os, sys, ctypes
import re

try:
    import urllib2
    import Tkinter
    import tkFileDialog
except ImportError:
    import urllib.request as urllib2
    import tkinter as Tkinter
    import tkinter.filedialog as tkFileDialog

default_folder = "~"

class init:
    @staticmethod
    def pkgmgr_installprefix(self):
        if sys.version_info[0] == 2:
            pkgmgr_installprefix = ['py', '-2']
        elif sys.version_info[0] == 3:
            pkgmgr_installprefix = ['py', '-3']
        else:
            raise('This script only works with Python 2 or 3')
            sys.exit()
    return pkgmgr_installprefix
    
    @staticmethod
    def is_admin():
        if sys.platform == "win32":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        elif sys.platform == "cygwin":
            is_admin = None
        else:
            is_admin = os.getuid() == 0
    
        if __name__ == '__main__':
            if is_admin == True:
                print("""
                      You are running this script as root/administrator.
                      All installations shall be installed for all users.
                      """)
            elif is_admin == False:
                print("""
                      You are not running this script as root/administrator.
                      All installations shall be installed in your user path.
                      """)
        while is_admin == None:
            cygwinchoice = input("You are using Cygwin. There is no way to determine if you are running as an administrator or not.\nAre you (Y/n)?\nWarning: If you accidentally answer yes, when not running as admin, all installations shall end in error.")
            cygwinadminyes = ['yes', 'ye', 'y']
            cygwinadminno = ['no', 'n']
            cygwinadmin = cygwinadminyes + cygwinadminno
            while cygwinchoice.lower() not in cygwinadmin:
                cygwinchoice = input("This is a yes or no question.\nAnswer it as such, Y for yes or n for no.\n")
            if cygwinchoice in cygwinadminyes:
                is_admin = True
            elif cygwinchoice in cygwinadminno:
                is_admin = False
    
        if is_admin == True:
            installsuffix = []
        elif is_admin == False:
            installsuffix = ['--user']
        return installsuffix

    def installer():
        if sys.version_info < (2, 4):
            easy_install = False
            legacy_easy_install = False
            print("Easy_Install is incompatable with this version.")
        elif (sys.version_info == (2, 4) or sys.version_info == (2, 5):
            easy_install = True
            legacy_easy_install = True
        elif sys.version_info >= (2, 6)
            easy_install = True
            legacy_easy_install = False
        if (sys.version_info < (2, 6) or sys.version_info == (3, 0) or sys.version_info == (3, 1)):
            pip = False
        else:
            pip = True
        if (pip == False and easy_install == False):
            installmethod = "1"
            installoptions = ["1"]
        elif (pip == True and easy_install == False):
            installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"2\" without quotes if you would like to install via pip.\n")
            installoptions = ["1", "2"]
        elif (pip == False and easy_install == True):
            installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"3\" without quotes if you would like to install via easy_install.\n")
            installoptions = ["1", "3"]
        elif (pip == True and easy_install == True):
            installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"2\" without quotes if you would like to install via pip.\nInput \"3\" without quotes if you would like to install via easy_install.\n")
            installoptions = ["1", "2", "3"]
        while installmethod not in installoptions:
            print("You did not input correctly")
            if (pip == True and easy_install == False):
                installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"2\" without quotes if you would like to install via pip.\n")
            elif (pip == False and easy_install == True):
                installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"3\" without quotes if you would like to install via easy_install.\n")
            elif (pip == True and easy_install == True):
                installmethod = input("Input \"1\" without quotes if you would like to install via a local setup.py.\nInput \"2\" without quotes if you would like to install via pip.\nInput \"3\" without quotes if you would like to install via easy_install.\n")
        return installmethod, legacy_easy_install


class install_package:
    def default(choosefile=None):
        if choosefile == None:
            window = Tkinter.Tk()
            window.withdraw()
            filetypelist = [('All Files', '.*'), ('All Python Scripts', '.py*'), ('Python Scripts (Terminal)', '.py'), ('Python Scripts (Compiled)', '.pyc'), ('Python Scripts (Optimized and Compiled)', '.pyo'), ('Python Scripts (No Terminal)', '.pyw'), ('Python DLLs', '.pyd'), ('Cython Scripts', '.pyx'), ('Cython Scripts (Header)', '.pxd')]
            choosefile = '"' + tkFileDialog.askopenfilename(defaultextension='.py', filetypes=filetypelist, initialdir="/", initialfile="setup.py", multiple=False, title="Choose a Setup Script", parent=window) + '" install'
            while choosefile = '"" install':
                choosefile = '"' + tkFileDialog.askopenfilename(defaultextension='.py', filetypes=filetypelist, initialdir="/", initialfile="setup.py", multiple=False, title="You must choose a Setup Script", parent=window) + '" install'
            choosefile = [choosefile]
        else:
            choosefile = '"' + choosefile + '" install'
            choosefile = [choosefile]
        try:
            fullcmd = pkgmgr_installprefix + choosefile + installsuffix
            fullcmd = ' '.join(fullcmd)
        except NameError:
            fullcmd = ['python'] + choosefile + ['--user']
            fullcmd = ' '.join(fullcmd)
        successful = os.system(fullcmd)
        if successful == 0:
            print("According to the checks in place, the package has installed successfully.\nYou should still make sure of this however.")
            if "--user" in fullcmd:
                print("The script was installed in your user path, since you have either not specified admin priveleges, or this script was run not as an admin.")
        else:
            print("Installation unsuccessful.")

def main():
    pkgmgr_installprefix = pkgmgr_installprefix()
    installsuffix = installsuffix()
    pkgmgr_installfileprefix = pkgmgr_installfileprefix()
    installmethod, legacy_easy_install = installercheck()
    CHOOSER = True
    while CHOOSER == True:
        if installmethod = "1":
            install_package.default()
        elif installmethod = "2":
            install_package.pip()
        elif installmethod = "3"
            install_package.easy_install()
        again = input("Would you like to install another package?(Y/n)\n")
        yes = ['yes', 'ye', 'y']
        no = ['no', 'n']
        yesno = yes + no
        while again not in yesno:
            again = input("Invalid Answer.\nWould you like to install another package (Same installation method applies)?(Y/n)\n")
        if again.lower() in yes:
            CHOOSER = True
        elif again.lower() in no:
            CHOOSER = False

def install_packagemanager(pip_or_easy_install):
    url = "https://bootstrap.pypa.io/" + pip_or_easy_install
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()
    install_name = "py -3 " + file_name
    os.system(install_name)
    print("Pip has been installed!")

def install_package_pip(packagename, version=None, minimum_version=None, maximum_version=None, update=None):    
    try:
        import pip
    except ImportError:
        print("You don't have pip. Pip will be installed now.")
        try:
            install_pip()
            import pip
        except PermissionError:
            print("You don't have the necessary permissions.\nPlease rerun this script as an administrator.")
        except IOError:
            print("You don't have the necessary permissions.\nPlease rerun this script as an administrator.")
        except OSError:
            print("You don't have the necessary permissions.\nPlease rerun this script as an administrator.")
    if (version != None and (minimum_version != None or maximum_version != None or update != None):
        print("You have chosen a specific version.\nThe minimum version, and/or maximum version, and/or update parameters you have chosen shall be stripped from the process.")
        minimum_version = maximum_version = update = None
    elif (version == None and (minimum_version != None or maximum_version != None) and update != None)
        print("You have chosen to update to the lates version.\nThe minimum version, and/or maximum version parameters you have chosen shall be stripped from the process.")
        minimum_version = maximum_version = None



    if (version == None and minimum_version == None and maximum_version == None and update == None):
        package = packagename
        install_args = ['install', package]
        install_info = "Pip shall now install the latest version of " + packagename
    elif (version != None and minimum_version == None and maximum_version == None and update == None):
        package = packagename + "==" + version
        install_args = ['install', package]
        install_info = "Pip shall now install " + packagename + " at version " + version
    elif (version == None and minimum_version != None and maximum_version == None and update == None):
        package = "'" + packagename + ">=" + minimum_version + "'"
        install_args = ['install', package]
        install_info = "Pip shall now install " + packagename + " at a minimum of version " + minimum_version
    elif (version == None and minimum_version == None and maximum_version != None and update == None):
        package = "'" + packagename + "<=" + maximum_version + "'"
        install_args = ['install', package]
        install_info = "Pip shall now install " + packagename + " at a maximum of version " + maximum_version
    elif (version == None and minimum_version != None and maximum_version == None and update == None):
        package = "'" + packagename + ">=" + minimum_version + "'"
        install_args = ['install', package]
    pip.main(['install', ])

def install_package_easy_install(packagename, version=None, minimum_version=None, maximum_version=None, update=None):    
    try:
        from setuptools.command import easy_install
    except ImportError:
        print("You don't have pip. Pip will be installed now.")
        try:
