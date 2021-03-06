# encoding: utf-8

import sys, os
sys.path[0:0] = [os.path.join(os.path.dirname(__file__), "..", ".."),]
import datasift

class Env(object):
    """
    Sets up and provides access to the environment for the Historics examples.
    """
    _user = None
    _args = []

    def __init__(self, args):
        """
        Initialise the environment with the provided arguments.
        """
        if len(args) < 2:
            sys.stderr.write('Please specify your DataSift username and API key as the first two command line arguments!\n')
            sys.exit(1)

        self._user = datasift.User(args[1], args[2])

        self._args = args[3:]

    def get_user(self):
        return self._user

    def get_arg_count(self):
        return len(self._args)

    def get_arg(self, num):
        return self._args[num]

    def get_args(self):
        return self._args

    def display_historic_details(self, historic):
        print 'Playback ID:  ', historic.get_hash()
        print 'Stream hash:  ', historic.get_stream_hash()
        print 'Name:         ', historic.get_name()
        print 'Start time:   ', historic.get_start_date()
        print 'End time:     ', historic.get_end_date()
        print 'Sources:      ', historic.get_sources();
        print 'Created at:   ', historic.get_created_at()
        print 'Status:       ', historic.get_status()
        print 'Progress:     ', '%d%%' % (historic.get_progress())
