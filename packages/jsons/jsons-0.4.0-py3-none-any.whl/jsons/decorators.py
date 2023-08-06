from inspect import signature, Parameter
from datetime import datetime
from typing import Dict, Callable

import jsons
from jsons import JsonSerializable, dump, load







def func():
    return 123

res = jsons.dump(func)
print(res)








f = Callable

def loaded(fork_inst=JsonSerializable):
    def _loaded_decorator(decorated):
        def _wrapper(*args, **kwargs):
            sig = signature(decorated)
            params = sig.parameters

            args_ = []
            for i in range(len(params)):
                param_name = params[i]
            # for param_name in params:
            #     if params[param_name].annotation != Parameter.empty:
            #         cls = params[param_name].annotation
            #         load(arg, cls=signature.parameters[attr].annotation,
            #              fork_inst=fork_inst



            loaded_args = [load(arg, cls=signature.parameters[attr].annotation,
                                fork_inst=fork_inst)
                           for arg in args if arg in params]
            loaded_kwargs = {attr: dump(kwargs[attr], fork_inst=fork_inst)
                             for attr in kwargs}
            # TODO if awaitable, do await?
            result = decorated(*loaded_args, **loaded_kwargs)
            return load(result, fork_inst=fork_inst)
        return _wrapper
    return _loaded_decorator




def dumped(fork_inst=JsonSerializable):
    def _dumped_decorator(decorated):
        def _wrapper(*args, **kwargs):
            dumped_args = [dump(arg, fork_inst=fork_inst) for arg in args]
            dumped_kwargs = {attr: dump(kwargs[attr], fork_inst=fork_inst)
                             for attr in kwargs}
            # TODO if awaitable, do await?
            result = decorated(*dumped_args, **dumped_kwargs)
            return dump(result, fork_inst=fork_inst)
        return _wrapper
    return _dumped_decorator




if __name__ == "__main__":

    @dumped()
    def f(x):
        print(x)
        return datetime.now()

    @loaded()
    def f2(x: datetime, y):
        print(x)
        return jsons.dump(x)


    res = f(datetime.now())
    print('res: ' + str(res))

    f2(str(res), 'onzin')