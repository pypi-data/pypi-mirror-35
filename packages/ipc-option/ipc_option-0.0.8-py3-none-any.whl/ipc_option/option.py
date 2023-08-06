import os
import json


class OptionMeta(type):
    def __new__(cls, name, bases, namespace, env_name=None, required=False, default=None):
        if name != 'Option':
            # subclass, set class name = env_name in globals
            if any([
                reserved_keyword in namespace
                for reserved_keyword in \
                ['super_options', 'option_instances', 'opiton_classes']
                ]):
                    raise Exception('super_options is reserved key word for class Option')
            option_instances = set()

            options_env = dict()
            for attr, option in namespace.items():
                if not OptionMeta.is_dunder(attr):
                    if isinstance(option, Option):
                        option._options = options_env
                        option_instances.add(option)

                    elif isinstance(option, type) and issubclass(option, Option):
                        # subclass should not provide any value
                        # attrs of subclass's instance provide values
                        # option is class and is subclass of Option
                        # replace it by it's instance
                        namespace[attr] = option()
                        option._options = options_env

            namespace['super_options'] = options_env
            namespace['option_instances'] = option_instances

            if env_name:
                namespace['_env_name'] = env_name
                namespace['_required'] = required
                namespace['_default'] = default

        return type.__new__(cls, name, bases, namespace)
    
    @staticmethod
    def is_dunder(name):
        return name.startswith('__') and name.endswith('__') and len(name) > 4


class Option(metaclass=OptionMeta):
    def __init__(self, env_name=None, required=False, default=None):
        if not hasattr(self, '_env_name'):
            self._env_name = env_name
            self._required = required
            self._default = default

        if self._env_name is None:
            raise Exception('env_name must be set')
    
    def __get__(self, obj, objtype=None):
        if hasattr(self, 'super_options'):
            # option class in a subclass of Option
            return self

        if hasattr(self, '_options'):
            get_option = self._options.get
        else:
            get_option = os.getenv

        if self._required:
            value = get_option(self._env_name)
            if value is None:
                raise ValueError('env var {} for option not found'.format(self._env_name))
        else:
            value = get_option(self._env_name, self._default)

        return value
    
    def load(self):
        if not hasattr(self, 'super_options'):
            # normal instance of class Option
            return self.__get__(self)

        if hasattr(self, '_options'):
            get_option = self._options.get
        else:
            get_option = os.getenv

        if self._required:
            value = get_option(self._env_name)
            if value is None:
                raise ValueError('env variable {} not found'.format(self._env_name))
        else:
            value = get_option(self._env_name, self._default)

        if value is not None:
            if isinstance(value, str):
                # top level option
                self.super_options.update(json.loads(value))
            elif isinstance(value, dict):
                # option subclass in a subclass of Option
                self.super_options.update(value)

        return self


def set_or_raise(name, value):
    if name in globals():
        raise Exception('{} already exists in globals'.format(name))
    else:
        globals()[name] = value
