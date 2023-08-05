"""Progress class file."""

from progressbar import ProgressBar

# Examples:

# from bitsapiclient.progress import Progress
# progress = Progress().start(self.users, verbose=self.verbose)
# progress.update()
# progress.finish()
#
# progress = Progress().start(verbose=self.verbose)
# progress.update(groups_list)
# progress.finish(groups_list)

class Progress(object):
    """Progress class."""

    def __init__(self, verbose=False):
        """Initiator method."""
        self.count = 0
        self.max = 100
        self.progress = None
        self.verbose = verbose

    def start_bar(self, items):
        """Start progress."""
        from progressbar import Bar, ETA, Percentage, SimpleProgress
        self.max = len(items)
        params = {
            'maxval': self.max,
            'widgets': [
                Percentage(),
                ' [',
                ETA(),
                '] ',
                SimpleProgress(),
                ' ',
                Bar(),
            ],
        }
        self.progress = ProgressBar(**params).start()

    def start_timer(self):
        """Start progress."""
        from progressbar import AnimatedMarker, Counter, SimpleProgress, Timer
        widgets = [
            '  ',
            AnimatedMarker(),
            '  [',
            Timer('Time: %s'),
            '] ',
            SimpleProgress(),
            # Counter(),
        ]
        self.progress = ProgressBar(widgets=widgets).start()

    def start(self, items=None, verbose=False):
        """Start progress."""
        self.verbose = verbose

        # if we got items, let's use a progress bar
        if items and verbose:
            self.start_bar(items)

        # otherwise, let's use a progress timer
        elif verbose:
            self.start_timer()

        return self

    def update(self, items=None, maxval=None):
        """Start progress."""
        if not self.verbose:
            return

        # check of we got items, and calculate count
        if isinstance(items, list) or isinstance(items, dict):
            count = len(items)
        else:
            count = int()

        # if we got items and a count, update the count and maxval
        if count:
            self.count = count
            if maxval:
                self.progress.maxval = maxval
            else:
                self.progress.maxval = count + 1

        # update the progress
        self.progress.update(self.count)

        # if we got no items, increment the count by one
        if not count:
            self.count += 1

    def finish(self, items=None):
        """Start progress."""
        if not self.verbose:
            return

        # check of we got items, and calculate count
        if isinstance(items, list) or isinstance(items, dict):
            count = len(items)
        else:
            count = int()

        # if we items and a count, update the max val
        if count:
            self.count = count
            self.progress.maxval = count

        # finish the progress
        self.progress.finish()
