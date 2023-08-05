import os
import setuptools

join = os.path.join
fpzipdir = 'fpzip-1.2.0'

# NOTE: If fpzip.cpp does not exist:
# cython -3 --fast-fail -v --cplus ./ext/src/third_party/fpzip-1.2.0/src/fpzip.pyx

import numpy as np

sources = [ join(fpzipdir, 'src', x) for x in ( 
  'error.cpp', 'rcdecoder.cpp', 'rcencoder.cpp', 
  'rcqsmodel.cpp', 'write.cpp', 'read.cpp', 
) ]

sources += [ 'fpzip.cpp' ]

setuptools.setup(
  setup_requires=['pbr', 'numpy'],
  extras_require={
    ':python_version == "2.7"': ['futures'],
    ':python_version == "2.6"': ['futures'],
  },
  ext_modules=[
    setuptools.Extension(
      'fpzip',
      sources=sources,
      language='c++',
      include_dirs=[ join(fpzipdir, 'inc'), np.get_include() ],
      extra_compile_args=[
        '-std=c++11', 
        '-DFPZIP_FP=FPZIP_FP_FAST', '-DFPZIP_BLOCK_SIZE=0x1000', '-DWITH_UNION',
      ]
    )
  ],
  pbr=True)





