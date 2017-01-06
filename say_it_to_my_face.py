# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import platform
import shutil
import subprocess
import sys
import traceback

_PLATFORM = platform.system()
PROGRAMS = {"Darwin": "say", "Linux": "espeak"}
PROGRAM = PROGRAMS.get(_PLATFORM, None)


class SayItToMyFace(logging.Handler):

    def __init__(self, voice=None):
        """Create a logging handler that tells you the logs

        :param str voice: By default, the voice is determined by your
                          locale, though you can override it.
                          Run `say -v ?` to see a list of names you
                          could specify here. There's apparently
                          something similar for espeak.
        """
        self.voice = voice
        super().__init__()

    def emit(self, record):
        """Emit a log record through your speakers"""
        if PROGRAM is None:
            # :(
            return

        # This will fail if you run it in Python 2, but that's fine because
        # it's 2017.
        # Bonus fact: I adapted an 11 year old patch from an actual
        # child prodigy (Erik Demaine) in order to add a `which` function
        # to the standard library in Python 3.3. I did that mainly on a whim
        # one day while saying "let's find a super old issue and get it into
        # a release."
        if shutil.which(PROGRAM) is None:
            # :(
            return

        args = [PROGRAM]
        if self.voice is not None:
            args.append(["-v", voice])
        args.append("'%s'" % record.msg)

        subprocess.call(args)


_sitmf = SayItToMyFace()
_logger = logging.getLogger("verbalize_exceptions")
_logger.addHandler(_sitmf)


def verbalize_exceptions(type, value, trace):
    _logger.critical(value)
    traceback.print_exception(type, value, trace)

def say_exceptions_to_my_face():
    sys.excepthook = verbalize_exceptions
