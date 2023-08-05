__author__ = 'Dror Paz, Israel Hydrological Service'
__CreatedOn__ = '2018/07/19'
__Version__ = '2018_08_16'

import os
import psutil
import time
import sys
import tempfile
import hashlib
import subprocess
import logging
try:
    from .launch import launch
except ImportError:
    try:
        from launch import launch
    except ImportError:
        import launch


popen_str=hashlib.sha224(('start popen %s from %s on %s %s'%(__file__, sys.executable, os.name, sys.platform)).encode()).hexdigest()


class TempFile(object):
    '''
    This class creates a temporary file which can be be opened in external program and be deleted only after the
    external program closes.
    A separate python instance will remain active in memory until no program uses the file (searched by filename),
    than deletes the file and closes.
    If the interpreter instance ends and the file is not open anywhere, it will be deleted.
    '''

    def __init__(self, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None):
        t = tempfile.NamedTemporaryFile(mode=mode, buffering=buffering, encoding=encoding, newline=newline,
                                        suffix=suffix, prefix=prefix, dir=dir, delete=False)

        logger = logging.getLogger()
        self.file = t
        # These are actually not necessary, but they make it it easier with auto-complete in the IDE.
        # self.name= t.name
        self.close = t.close
        self.write = t.write
        self.run = self.__run
        logger.debug('Initialized temporary file %s'%self.name)


    def __del__(self):
        logger = logging.getLogger()
        if not self.isRunning:
            self.delete()
            logger.debug('%s deleted from system'%self.name)
        else:
            logger.debug('%s is used by another program'%self.name)


    def delete(self, ignoreErrors=True):
        '''delete the temporary file and file object'''
        logger = logging.getLogger()

        if self.exist:
            try:
                self.close()
            except:
                pass
            try:
                os.remove(self.name)
                logger.debug('%s removed from system')
            except:
                if not ignoreErrors:
                    raise
        else:
            try:
                self.close()
            except:
                pass
            logger.debug('%s does not exist'%self.name)



    @staticmethod
    def run(fn, delete=True):
        '''
        Run a file with the program associated to it by your OS.
        :param fn: filename to run
        :type fn: str
        :param delete: Whether to delete file after it is closed.
        :type delete: bool
        :return:
        :rtype:
        '''
        logger=logging.getLogger()
        ret = launch(fn)
        print(ret)
        if ret:
            logger.error('Could not run %s'%fn)
        else:
            logger.debug('Launched %s'%fn)
        if delete:
            cmd = '%s "%s" -popen_str "%s" -filename "%s"' % (sys.executable, __file__, popen_str, fn)
            s = subprocess.Popen(cmd)
        return ret

    def __run(self, delete=True):
        '''
        Run the temporary file with the program associated to it by your OS.
        :param delete: Whether to delete file after it is closed.
        :type delete: bool
        :return:
        :rtype:
        '''
        if self.exist:
            return self.__class__.run(self.name, delete)
        else:
            logging.getLogger().error('%s does not exist'%self.name)

    @classmethod
    def monitorAndDelete(cls, fn, interval=1):
        '''
        Monitor file for usage, and deletes it when it is not in use.
        Args:
            fn (): file name
            interval (int): seconds between checks on file.

        Returns:
        '''
        while isRunning(fn):
            time.sleep(interval)
        os.remove(fn)

    @property
    def exist(self):
        return os.path.exists(self.name)

    @property
    def isRunning(self):
        if not self.file.closed:
            return True

        elif self.exist:
            return isRunning(self.name)
        else:
            return False

    @property
    def name(self):
        return self.file.name

def test():
    t = TempFile(mode='w', suffix='.csv')
    t.write('some, text')
    print(t.name, os.path.exists(t.name))
    t.close()
    t.run()
    quit()
    # print(t.name, os.path.exists(t.name))
    for i in range(10000000):
        i=i**2
    print(t, t.name, os.path.exists(t.name))


def isRunning(fn):
    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                if item.path == fn:
                    return True
        except:
            pass
    return False

if __name__ == '__main__':
    import argparse
    args_parser = argparse.ArgumentParser(description='Run monitorAndDelete on a file')
    args_parser.add_argument('-popen_string', dest='popen_str', metavar='popen string',
                             default=None, help='a string that will activate seperate process')
    args_parser.add_argument('-filename', dest='filename', metavar='file name', default=None,
                             help='Temporary file to monitor and delete')
    args_parser.add_argument('-interval', dest='interval', metavar='file name', default=1, type=int,
                             help='seconds between isRunning checks')
    args = args_parser.parse_args()

    if args.popen_str and args.filename and args.popen_str==popen_str:
        TempFile.monitorAndDelete(fn=args.filename, interval=args.interval)
    elif args.popen_str is None:
        test()
    else:
        raise argparse.ArgumentError('Cant run script with selected arguments: %s'%args)
