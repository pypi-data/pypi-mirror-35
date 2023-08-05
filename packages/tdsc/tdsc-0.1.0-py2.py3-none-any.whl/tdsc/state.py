from __future__ import unicode_literals, absolute_import, print_function
from abc import ABC, abstractmethod
import logging

"""
Define conventional "state" behaviour.

The simplest state is an object that encapsulates a pre-execution guard,
``should_execute``, an action to be performed, ``execute``, and a post-execute
callback and transform, ``post_execute``. By default, ``should_execute`` is
``True``, and ``post_execute`` returns the result or raised error from
``execute``, or ``None`` if ``should_execute`` guarded against execution.
"""


class State(ABC):
    def _get_logger(self):
        return logging.getLogger("tdsc.state.{}".format(self.__class__.__name__))

    def should_execute(self, ctx):
        return True

    @abstractmethod
    def execute(self, ctx):
        raise NotImplemented

    def post_execute(self, ctx, ran_successfully, result):
        if not ran_successfully:
            self._get_logger().exception(
                "State {} did not run successfully.".format(self.__class__.__name__),
                exc_info=result,
            )
        return result

    def run(self, ctx):
        result = None
        ran_successfully = False

        try:
            if self.should_execute(ctx):
                result = self.execute(ctx)
                ran_successfully = True
        except Exception as err:
            result = err
        finally:
            return self.post_execute(ctx, ran_successfully, result)
