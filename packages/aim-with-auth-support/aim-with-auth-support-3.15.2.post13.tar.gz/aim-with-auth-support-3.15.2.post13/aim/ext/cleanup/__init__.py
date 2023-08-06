import time
from abc import abstractmethod
import os
import atexit
import weakref
import logging
import threading

from func_timeout import func_timeout, FunctionTimedOut


from typing import Generic, Tuple, TypeVar, Dict

T = TypeVar('T')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class RobustExec(threading.Thread):
    """
    A thread that executes a function and catches all soft interrupts.
    Users very often Ctrl-C to stop the program multiple times which leaves
    program no chance to clean up.
    """
    def __init__(self, *args, stop_signal, **kwargs):
        super().__init__(*args, **kwargs)
        self.stop_signal = stop_signal

    def join(self):
        while True:
            try:
                # Pressing Ctrl-C will raise KeyboardInterrupt and stop only
                # the `Event.wait()` call. The target function of `RobustExec`
                # will continue to run, until stop_signal is set.
                return self.stop_signal.wait()
            except KeyboardInterrupt:
                logger.warning('Received Ctrl-C. Closing gracefully.')


class AutoClean(Generic[T]):
    PRIORITY = 10
    _registered_with_atexit = False
    _finalizers: Dict[
        T, Tuple[int, weakref.finalize]
    ] = weakref.WeakKeyDictionary()

    stop_signal = threading.Event()

    def __init__(self, instance: T) -> None:
        """
        Initialize object resources that need to be cleaned up automatically.
        """
        self.finalizer = weakref.finalize(instance, self._close)
        # We do not finalizer to automatically close the object itself.
        # Instead, we will collect all finalizers and call them at exit.
        self.finalizer.atexit = False
        self._finalizers[instance] = (self.PRIORITY, self.finalizer)

        if not AutoClean._registered_with_atexit:
            atexit.register(AutoClean.cleanup)
            AutoClean._registered_with_atexit = True

    def close(self) -> None:
        """Manually close the object."""
        try:
            func_timeout(5, self.finalizer)
        except FunctionTimedOut:
            print(f"finalizer could not complete within 5 seconds and was terminated.\n")
            if os.getenv('AIM_TRACK_UNSAFE') == 'true':
                raise
        except Exception as e:
            err = "There was an exception in  "
            err += self.finalizer.__name__
            logger.exception(err)
            if os.getenv('AIM_TRACK_UNSAFE') == 'true':
                raise

    @abstractmethod
    def _close(self):
        """
        This method is called when the instance is garbage collected.
        Meant to be overridden by subclasses.
        """
        ...

    @staticmethod
    def _cleanup():
        """
        Actually cleanup all the remaining resources in order of specified
        priorities. Resources with bigger priority numbers are cleaned up first (have higher priority)
        while the resources with equal priorities are cleaned up in reverse order
        of their registration (hence why reversed is used).
        This is called automatically by atexit. It is not meant tobe called manually.
        """

        finalizers = sorted(AutoClean._finalizers.items(), key=lambda x: x[1][0])
        logger.debug(f'Cleaning up...  Found {len(finalizers)} finalizers')
        logger.debug('Cleaning up...  Iterating over instances in order')
        for key, (priority, finalizer) in reversed(finalizers):
            logger.debug(f'Cleaning up...  with priority={priority} instance {key}')
            try:
                func_timeout(5, finalizer)
            except FunctionTimedOut:
                print(f"finalizer with priority={priority} instance {key} could not complete within 5 seconds and was terminated.\n")
                if os.getenv('AIM_TRACK_UNSAFE') == 'true':
                    raise
            except Exception as e:
                err = "There was an exception in  "
                err += finalizer.__name__
                logger.exception(err)
                if os.getenv('AIM_TRACK_UNSAFE') == 'true':
                    raise
        AutoClean.stop_signal.set()

    @staticmethod
    def cleanup():
        """
        Cleanup all the remaining objects. This is called automatically
        when the program exits.
        It also blocks until all the cleanup functions have finished to ensure
        data consistency.
        """
        logger.debug('Cleaning up...  Blocking KeyboardInterrupts')
        example = RobustExec(stop_signal=AutoClean.stop_signal, target=AutoClean._cleanup)
        example.start()
        example.join()
        logger.debug('Cleaning up...  Done')
