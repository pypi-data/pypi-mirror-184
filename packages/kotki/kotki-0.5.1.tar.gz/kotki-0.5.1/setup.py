import io
import os
import re
import subprocess
import sys
import multiprocessing
from shutil import rmtree

from setuptools import Command, Extension, find_packages, setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py as _build_py


if sys.platform != "linux" and sys.platform != "linux2":
    raise Exception("Only Linux is supported at this moment.")

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}

# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # required for auto-detection & inclusion of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        cfg = "Debug" if debug else "Release"

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")
        build_arch = os.environ.get("BUILD_ARCH", "native")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
            f"-DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE",
            f"-DCMAKE_INSTALL_RPATH=$ORIGIN",  # https://crascit.com/wp-content/uploads/2019/09/Deep-CMake-For-Library-Authors-Craig-Scott-CppCon-2019.pdf
            f"-DCOMPILE_PYTHON=ON",
            f"-DVENDORED_LIBS=ON",
            f"-DRECONSTRUCT_GIT=ON",
            f"-DSSPLIT_USE_INTERNAL_PCRE2=ON",
            f"-DBUILD_ARCH={build_arch}",
        ]

        build_args = ["-t", "kotki"]
        # Adding CMake arguments set as environment variable
        # (needed e.g. to build for ARM OSx on conda-forge)
        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        # In this example, we pass in the version to C++. You might not need to.
        cmake_args += [f"-DEXAMPLE_VERSION_INFO={self.distribution.get_version()}"]

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator:
                try:
                    import ninja  # noqa: F401

                    cmake_args += ["-GNinja"]
                except ImportError:
                    pass

        else:

            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward compatibility
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                ]
                build_args += ["--config", cfg]

        if sys.platform.startswith("darwin"):
            # Cross-compile support for macOS - respect ARCHFLAGS if set
            archs = re.findall(r"-arch (\S+)", os.environ.get("ARCHFLAGS", ""))
            if archs:
                cmake_args += ["-DCMAKE_OSX_ARCHITECTURES={}".format(";".join(archs))]

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            cpu_count = multiprocessing.cpu_count()
            if cpu_count > 1:  # cut some slack :-P
                cpu_count -= 1
            build_args += [f"-j{cpu_count}"]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        print("cmake", ext.sourcedir, " ".join(cmake_args))

        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=self.build_temp
        )


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
long_description = ""
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

version = None
with open(os.path.join(here, "src", "BERGAMOT_VERSION")) as f:
    version = f.read().strip()
    suffix = os.environ.get("PYTHON_LOCAL_VERSION_IDENTIFIER", None)
    if suffix:
        version = "{}+{}".format(version, suffix)


class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="kotki",
    version=version,
    author="Kroket Ltd.",
    author_email="code@kroket.io",
    url="https://github.com/kroketio/kotki/",
    description="Translate text locally on your machine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[CMakeExtension("kotki")],
    cmdclass={"build_py": build_py, "build_ext": CMakeBuild},
    zip_safe=False,
    extras_require={"test": ["pytest>=6.0"]},
    license_files=("LICENSE",),
    python_requires=">=3.6",
    packages=["kotki"],
    package_dir={"kotki": "bindings/python"},
    install_requires=["requests", "pyyaml>=5.1", "appdirs"],
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Bug Reports": "https://github.com/kroketio/kotki/issues",
        "Source": "https://github.com/kroketio/kotki/"
    },
)
