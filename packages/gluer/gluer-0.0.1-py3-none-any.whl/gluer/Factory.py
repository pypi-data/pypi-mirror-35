import inspect

from typing import Callable, get_type_hints

from .exceptions import Unannotated

class Factory:
    """Wrapper for a factory function/class constructor"""

    def __init__(self, gluer: 'Gluer', init: Callable):
        self.single_instance = False
        self.instance = None
        self.parameters = dict()
        self.type = None

        self.gluer = gluer
        self.init = init

        sign = inspect.signature(init)
        annotations = get_type_hints(init)

        if inspect.isclass(init):
            self.type = init
            annotations = get_type_hints(init.__init__)
        elif "return" in annotations:
            self.type = annotations["return"]
        else:
            msg = f"Factory {init} has an unannotated return type"
            raise Unannotated(msg)

        for name, parameter in sign.parameters.items():
            if name == "self":
                continue
            if parameter.kind in [parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD]: #*args and **kwargs
                continue
            if parameter.default is not inspect._empty:
                continue

            if name not in annotations:
                msg = f"Factory {init} has an unannotated, not default parameter: {name}"
                raise Unannotated(msg)
            annotation = annotations[name]
            self.parameters[name] = annotation


    def __call__(self):
        if self.instance is not None:
            return self.instance

        parameters = {name: self.gluer.resolve(cls) for name, cls in self.parameters.items()}
        instance = self.init(**parameters)

        if self.single_instance:
            self.instance = instance

        return instance
