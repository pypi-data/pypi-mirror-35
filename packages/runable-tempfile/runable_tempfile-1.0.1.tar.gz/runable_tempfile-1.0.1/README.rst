runable_tempfile.TempFile
=========================

This class creates a temporary file which can be be opened in external program and be deleted only after the external program closes.
A separate python instance will remain active in memory until no program uses the file (searched by filename), than deletes the file and closes.

Usage:
------
    >>> from runable_tempfile import TempFile
    >>> tf = TempFile(mode='w', suffix='.csv')
    >>> tf.write('column1, column2')
    >>> tf.close()
    >>> # do bunch of other stuff here
    >>> tf.run()

    After the interpreter and every program that uses the file will be closed, the file will be deleted.
