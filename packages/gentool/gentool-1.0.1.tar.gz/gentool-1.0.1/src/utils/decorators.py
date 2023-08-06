import functools


def transform_args(transform_type):
    def wrapper_transform_args(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            new_args = []
            for arg in args:
                arg = transform_arg(arg, transform_type)
                new_args.append(arg)
            args = tuple(new_args)
            for kwarg in kwargs.keys():
                kwargs[kwarg] = transform_arg(kwarg, transform_type)
            value = func(*args, **kwargs)

            return value
        return wrapper_decorator
    return wrapper_transform_args


def transform_arg(inputarg, action):
    func_dict = {
        "str": str(inputarg)
    }
    return func_dict.get(action, inputarg)
