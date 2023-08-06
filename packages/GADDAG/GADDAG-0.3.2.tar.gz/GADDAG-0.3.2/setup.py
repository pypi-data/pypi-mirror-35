from setuptools import setup, Extension
from distutils.command.build_ext import build_ext


class build_ext(build_ext):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypes)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)


class CTypes(Extension):
    pass


with open("README.rst") as f:
    long_desc = f.read()

libcgaddag = CTypes("libcgaddag", sources=["src/cGADDAG-0.3.1/src/cgaddag.c"])

setup(name="GADDAG",
      version="0.3.2",
      description="Python wrapper of cGADDAG",
      long_description=long_desc,
      license="MIT",
      author="Jordan Bass",
      author_email="jordan+gaddag@jbass.io",
      url="https://github.com/jorbas/GADDAG",
      download_url="https://github.com/jorbas/GADDAG/archive/0.3.2.tar.gz",
      keywords=["gaddag", "trie"],
      package_dir={"": "src"},
      py_modules=["gaddag"],
      ext_modules=[libcgaddag],
      cmdclass={"build_ext": build_ext},
      classifiers=[])
