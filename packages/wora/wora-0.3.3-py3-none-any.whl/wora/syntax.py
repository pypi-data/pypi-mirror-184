from typing import Any

def tern(cond, x, y) -> Any:
    ''' Ternary operator '''
    return x if cond else y

def tern_bool(cond) -> bool:
    ''' Returns true if the condition is true, else false '''
    return tern(cond, True, False)

def tern_func(cond, f1, f2, *args, **kwargs) -> Any:
    if cond:
        return f1(*args, **kwargs)
    else:
        return f2(*args, **kwargs)

def fallback(default, val):
    ''' Fallback to a default value if the value is None '''
    return tern(val is None, default, val)

def config_fallback(cfg: dict, default: Any, val: Any) -> Any:
    return tern(default in cfg, cfg.get(default), val)

