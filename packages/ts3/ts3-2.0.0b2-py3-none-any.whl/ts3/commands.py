#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2013-2018 <see AUTHORS.txt>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



class TS3Command(object):

    def __init__(self):
        #: The command name, e.g. ``clientkick``
        self.cmd = cmd

        #: The names of the supported options, e.g. ``{}``
        self.options = frozenset(options)

        #: The names of all supported properties, e.g. ``{}``
        self.properties = frozenset(properties)

        #: The TS3 help info for this command.
        self.help = help
        return None

    @classmethod
    def from_help(cls, help):
        """Parses the TS3 help info for a command and initialises a new
        :class:`TS3Command` with it.
        """

    def to_query(eslf, **kargs):
        q = TS3QueryBuilder(self.cmd)
        for key, val in kargs.items():
            if key in self.options:
                if val:
                    q = q.options(key)
            elif key in self.properties:
                if val is not None:
                    q = q.params(key=val)
            else:
                raise KeyError("Unknown property/option '{}'.".format(key))
        return q


class TS3Commander(object):

    def __init__(self):
        self.cmds = dict()
        return None

    def __getattr__(self, cmd, **kargs):
        cmd = self.cmds[cmd]
        query = cmd.to_query(**kargs)
        return self.conn.exec_query(query)


ts3conn("clientkick", ...)

ts3conn.c.clientkick(clid=2)


ts3cmds = TS3Commander(ts3conn)
resp = ts3cmds.clientkick()
