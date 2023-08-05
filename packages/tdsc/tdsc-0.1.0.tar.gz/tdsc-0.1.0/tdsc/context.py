from __future__ import unicode_literals, absolute_import, print_function
import platform
import appdirs


class ContextInfo:
    @property
    def platform(self):
        return platform.system()


class ContextStore:
    pass


class Context:
    __store = ContextStore()
    info = ContextInfo()

    @property
    def store(self):
        return self.__store

    @staticmethod
    def paths_for_state(state_name, app_author="tdsc", version=None, roaming=False):
        return appdirs.AppDirs(
            state_name, appauthor=app_author, version=version, roaming=roaming
        )
