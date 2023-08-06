import os
import shutil
import subprocess
import sys

###########################################################################################################


cwd=os.path.dirname(__file__)
home=os.getenv('HOME')

src=f'{cwd}/.sc'
dist=f'{home}/.sc'
###########################################################################################################
def install():
    try:
        shutil.rmtree(dist)
    finally:
        shutil.copytree(src, dist)
        os.chdir(dist)
        subprocess.run(['python','-m','venv','venv'])
        subprocess.run(['venv/bin/python','-m','pip','install','-r','requirements.txt'])
        subprocess.run(['venv/bin/python', 'install.py'])


def uninstall():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'uninstall.py'])
    finally:
        try:
            shutil.rmtree(dist)
        except:
            pass


def upgrade()
import sxxxs
    version = sxxxs.__version__
    subprocess.run(['pip','install','--upgrade',sxxxs])
    import sxxxs
    if version != sxxxs.__version__:
        print('updating ...')
        sxxxs.m.install()
        print('updated')
    else : print('it is up to date')

def update():
    upgrade()


def open():
    try:
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'main.py'])
    except:
        install()
        os.chdir(dist)
        subprocess.run(['venv/bin/python', 'main.py'])
###########################################################################################################
def main():
    command = sys.argv
    if len(command) == 1:
        open()
    else:
        exec (f'{command[1]}()')
