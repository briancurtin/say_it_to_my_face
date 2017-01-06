from setuptools import setup

AUTHOR = "Brian Curtin"
AUTHOR_EMAIL = "brian@python.org"

setup(name="say_it_to_my_face",
      description="Log handler and exception hook to verbalize messages.",
      license="Apache 2",
      url="https://twitter.com/logout",
      version="1.0",
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      keywords="this is dumb",
      long_description=open("README.rst").read(),
      py_modules=["say_it_to_my_face"],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio :: Speech"],
)
