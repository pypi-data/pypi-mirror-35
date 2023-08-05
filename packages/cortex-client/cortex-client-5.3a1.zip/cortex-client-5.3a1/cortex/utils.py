import hashlib
import logging
from contextlib import closing


def md5sum(file_name, blocksize=65536):
    md5 = hashlib.md5()
    with closing(open(file_name, "rb")) as f:
        for block in iter(lambda: f.read(blocksize), b""):
            md5.update(block)
    return md5.hexdigest()


def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or console
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False


def log_message(msg: str, log: logging.Logger, level=logging.INFO, *args, **kwargs):
    if is_notebook():
        print(msg)
        log.debug(msg, *args, **kwargs)
    else:
        log.log(level, msg, *args, **kwargs)
