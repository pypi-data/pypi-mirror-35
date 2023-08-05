from distutils.core import setup, Extension

timetravel10_hash_module = Extension('timetravel10_hash',
                               sources = ['timetravel10_module.c',
                                          'timetravel10.c',
                                          'sha3/blake.c',
                                          'sha3/bmw.c',
                                          'sha3/groestl.c',
                                          'sha3/jh.c',
                                          'sha3/keccak.c',
                                          'sha3/skein.c',
                                          'sha3/cubehash.c',
                                          'sha3/echo.c',
                                          'sha3/luffa.c',
                                          'sha3/simd.c',
                                          'sha3/shavite.c'],
                            include_dirs=['.', './sha3'])

setup (name = 'timetravel10_hash',
       version = '1.0',
       author = "kimkkikki",
       author_email = "kimkkikki1@gmail.com",
       url = "https://github.com/kimkkikki/timetravel10_hash",
       description = 'Bindings for proof of work used by timetravel10',
       ext_modules = [timetravel10_hash_module])
