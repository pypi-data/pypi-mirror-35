#!/usr/bin/python3
# -*- coding: utf-8 -*-
###############################################################################
#    ReadSLText Copyright (C) 2017 Xavier Faure
#    Contact: suizozukan arrobas orange dot fr
#
#    This file is part of ReadSLText.
#    ReadSLText is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ReadSLText is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ReadSLText.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
        ❏readsltext❏ readsltext/readsltext.py
        _______________________________________________________________________

        (Python3/GPLv3) modules to read text files with lines split on several
        lines, the so called "SLText" format.

        see README.md for more documentation, especially about the "SLText"
        format.
        _______________________________________________________________________

        ● ReadSLText class
"""
from collections import OrderedDict

# =============================================================================
# project's settings
#
# o for __version__ format string, see
#   https://www.python.org/dev/peps/pep-0440/ :
#
#   e.g. "0.1.2.dev1" or "0.1a"
#
# o See also https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
# =============================================================================
__projectname__ = "readsltext"
__version__ = "0.0.6"
__laststableversion__ = "0.0.4"
__author__ = "Xavier Faure (suizokukan / 94.23.197.37)"
__copyright__ = "Copyright 2018, suizokukan"
__license__ = "GPL-3.0"
__licensepypi__ = 'License :: OSI Approved :: '\
                  'GNU General Public License v3 (GPLv3)'
__maintainer__ = "Xavier Faure (suizokukan)"
__email__ = "suizokukan@orange.fr"
__status__ = "Pre-Alpha"
__statuspypi__ = 'Development Status :: 2 - Pre-Alpha'


def clientrypoint():
    """
        function called through the CLI when the use writes "readsltext"
        in a terminal.
    """
    print("project {0} (v. {1}); author : {2}".format(__projectname__,
                                                      __version__,
                                                      __author__))


class ReadSLText(object):
    """
        ReadSLText class
        _______________________________________________________________________

        Use this class to read a "SLText" file, e.g. :

                        with readsltext.ReadSLText("file4.txt") as src:
                            for line in src:
                                print(line)
        _______________________________________________________________________

        class attribute :
        ● regex__comma_eol : regex for a line ending with a comma

        instance attribute :
        ● _file : (_io.TextIOWrapper) the file to be read

        methods :
        ● __enter__(self)
        ● __exit__(self, typ, value, traceback):
        ● __init__(self, filename, sep_char="»", ordereddicts=True)
        ● __iter__(self)
        ● __next__(self)
        ● close(self)
        ● get_empty_full_line(self):
        ● next(self)
        ● open(self, filename)
    """

    def __enter__(self):
        """
            ReadSLText.__enter__(self)
            ___________________________________________________________________

            Method required by the "with..." statement.
            ___________________________________________________________________

            no ARGUMENT

            RETURNED VALUE : self
        """
        return self

    def __exit__(self, typ, value, traceback):
        """
            ReadSLText.__enter__(self)
            ___________________________________________________________________

            Method required by the "with..." statement.
            ___________________________________________________________________

            ARGUMENTS : mandatory arguments for such a method (__exit__).

            no RETURNED VALUE
        """
        self.close()

    def __init__(self, filename, sep_char="»", ordereddicts=True):
        """
            ReadSLText.__init__(self, _file)
            ___________________________________________________________________
            ___________________________________________________________________

            ARGUMENT:
            ▪ filename          : (str) the file to be read
            ▪ sep_char          : (str) the separator character, used one
                                  time (e.g. "*") and three times (e.g. "***").
            ▪ ordereddicts      : (bool) according to ordereddicts, the result
                                  of ReadSLText.__next__() will be different :

                             returned value structure:
                             “ if True, ReadSLText.__next__() will return
                             “ list( str(line_value), OrderedDict(line_key) )
                             “            -> line_key = OrderedDict(key:value)
                             “
                             “ if False, ReadSLText.__next__() will return
                             “ list( str(line_value), dict(line_key) )
                             “            -> line_key = dict(key:value)

            no RETURNED VALUE
        """
        self.sep_char = sep_char
        self._file = None

        self.ordereddicts = ordereddicts

        self.open(filename)

    def __iter__(self):
        """
            ReadSLText.__iter__()
            ___________________________________________________________________

            Method required by the "for ..." statement.
            ___________________________________________________________________

            no ARGUMENT

            RETURNED VALUE : self
        """
        return next(self)

    def __next__(self):
        """
            ReadSLText.__next__()
            ___________________________________________________________________

            Implement the reading of each 'line', i.e. one or several lines in
            the source file.
            ___________________________________________________________________

            no ARGUMENT

            RETURNED VALUE : (str) a 'line', i.e. one or several lines in the
                             source file. The returned value depends on the
                             value of self.ordereddicts :

                         returned value structure:
                         “ if True, ReadSLText.__next__() will return
                         “ list( str(line_value), OrderedDict(line_key) )
                         “            -> line_key = OrderedDict(key:value)
                         “
                         “ if False, ReadSLText.__next__() will return
                         “ list( str(line_value), dict(line_key) )
                         “            -> line_key = dict(key:value)
        """
        go_on = True
        full_line = self.get_empty_full_line()  # something like ["", dict()]

        while go_on:

            line = self._file.readline()

            if line == "":
                # end of the file
                go_on = False

            elif line.strip().startswith("#"):
                pass

            elif line.strip() == "":
                pass

            else:
                # simple line : just a line_key, no value (and no dict)
                if self.sep_char not in line:

                    if full_line[0] != "":
                        # let's flush full_line :
                        yield full_line
                    elif full_line[1]:
                        raise ValueError("ill-formed lines : "
                                         "don't known what to with " +
                                         str(full_line[1]))

                    # something like ["", dict()]
                    full_line = self.get_empty_full_line()

                    yield [line.strip(), None]

                # simple line : a line_key and a simple line_value (no dict) :
                elif line.count(self.sep_char) == 3:

                    if full_line[0] != "":
                        # let's flush full_line :
                        yield full_line
                    elif full_line[1]:
                        raise ValueError("ill-formed lines : "
                                         "don't known what to with " +
                                         str(full_line[1]))

                    # something like ["", dict()]
                    full_line = self.get_empty_full_line()
                    yield list(map(str.strip, line.split(self.sep_char*3)))

                # complex line :
                #     either we have   key_line, value_line = (key, value)
                #     either we have   valueline = (key, value)
                elif line.count(self.sep_char) == 4:

                    # "    grammaticaldetails »»»  grammatical nature » noun"
                    # let's flush full_line :
                    if full_line[0] != "":
                        yield full_line
                    elif full_line[1]:
                        raise ValueError("ill-formed lines : "
                                         "don't known what to with " +
                                         str(full_line[1]))

                    # something like ["", dict()]
                    full_line = self.get_empty_full_line()

                    _full_line = list(map(str.strip,
                                          line.split(self.sep_char*3)))

                    full_line[0] = _full_line[0]

                    subdict = list(map(str.strip,
                                       _full_line[1].split(self.sep_char)))
                    full_line[1].update({subdict[0]: subdict[1]})
                else:
                    # "                            gender             » neuter"
                    # we add this line to the current full_line :
                    subdict = list(map(str.strip,
                                       line.split(self.sep_char)))
                    full_line[1].update({subdict[0]: subdict[1]})

    def close(self):
        """
            ReadSLText.close()
            ___________________________________________________________________

            Close the source file.
            ___________________________________________________________________

            no ARGUMENT

            no RETURNED VALUE
        """
        self._file.close()

    def get_empty_full_line(self):
        """
            ReadSLText.get_empty_full_line
            ___________________________________________________________________

            Return an empty full_line, i.e. a structure where different lines
            are stored.
            ___________________________________________________________________

            no ARGUMENT

            RETURNED VALUE :
        """
        if self.ordereddicts:
            return ["", OrderedDict()]

        return ["", dict()]

    def next(self):
        """
            ReadSLText.next()
            ___________________________________________________________________

            Implement the reading of each 'line', i.e. one or several lines in
            the source file.
            ___________________________________________________________________

            no ARGUMENT

            RETURNED VALUE : (str) a 'line', i.e. one or several lines in the
                             source file.
        """
        return self.__next__()

    def open(self, filename):
        """
            ReadSLText.__init__(self, filename)
            ___________________________________________________________________

            Open the file to be read, initialize self._file.
            ___________________________________________________________________

            ARGUMENT:
            ▪ filename : (str) the file to be read.

            no RETURNED VALUE
        """
        self._file = open(filename, mode='r')
