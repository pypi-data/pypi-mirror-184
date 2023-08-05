import platform

from wora.syntax import (tern_bool)

def get_platform_dynlib_ext() -> str:
    ''' Retrieves the shared library file extension for the current platform '''
    ext = ''
    match platform:
        case 'darwin'   : ext = 'dylib'
        case 'win32'    : ext = 'dll'
        case _          : ext = 'so'
    return ext

def get_platform_dynlib_prefix() -> str:
    ''' Retrieves the shared library file prefix for the current platform '''
    prefix = ''
    match platform:
        case 'win32'        : prefix = ''
        case 'darwin' | _   : prefix = 'lib'
    return prefix

def fmt_platform_dynlib(libname: str) -> str:
    ''' Format the dynamic library for the current platform '''
    return f'{get_platform_dynlib_prefix()}{libname}.{get_platform_dynlib_ext()}'

def get_platform() -> str:
    return platform.system()

def is_win() -> bool:
    # return any(platform.win32_ver())
    return tern_bool(get_platform() == 'Windows')

def is_linux() -> bool:
    return tern_bool(get_platform() == 'Linux')

def is_apple() -> bool:
    # return any(platform.win32_ver())
    return tern_bool(get_platform() == 'Darwin')
