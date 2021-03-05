def zhuangshiqi(func):
    def wrap(request, *args, **kwargs):
        return func(request, *args, **kwargs)
        pass
    return wrap
