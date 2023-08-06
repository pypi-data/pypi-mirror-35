import inspect

from typing import get_type_hints, Type, Sequence, Union, Callable
from collections import defaultdict, OrderedDict

from .exceptions import ServiceNotRegistered
from .Factory import Factory
from .Registration import Registration
from .typing_helpers import is_list_type


class Gluer:
    def __init__(self):
        self._services = defaultdict(list)

        self.register_instance(self)


    def register(self, factory: Union[Type, Callable]) -> Registration:
        """Registers type as a set of given services"""

        factory = Factory(self, factory)
        registration = Registration(self._services, factory)

        return registration

    def register_instance(self, instance: object, cls: Type = None):
        """Registers instance. Optionally as a given class"""
        if cls is None:
            cls = instance.__class__

        def factory() -> cls:
            return instance

        self.register(factory)



    def resolve(self, service: Type):
        """Returns demanded service with dependencies injected"""

        if is_list_type(service):
            service = service.__args__[0]
            if service not in self._services:
                raise ServiceNotRegistered(f"service {service} has not been registered")
            services = self._services[service]
            return [const() for const in services]

        if service not in self._services:
            raise ServiceNotRegistered(f"service {service} has not been registered")
        constructor = self._services[service][-1] # last registered
        return constructor()

