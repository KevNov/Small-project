def enforce(*type):
    def decorator(f):
        def new_func(*args,**kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args,type):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str,int)
def repeat_msg(msg,times):
    for time in range(times):
        print(msg)

print(repeat_msg("welcome","5"))

    