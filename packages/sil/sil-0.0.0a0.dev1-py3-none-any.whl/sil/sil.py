class Sil:
    '''
    For making a status indicator inline
    '''
    indicator='█' #█ █ █ █

    def __init__(self, total, length=40, every=1):
        '''

        Kwargs:
            total (int): The total number of elements which are being processed.
            length (int): The number of characters the progress bar should be.
                Defaults to 40.
            every (int): After how many elements should the progress bar be
                updated. Defaults to 1.

        Returns:
            None
        '''

        self.total = total;
        self.length = length;
        self.current = 0;
        self._index = 1
        self.every = every


    def empty(self):
        blank = ' ' * self.length;
        return f'\r[{blank}\t{self.current+1}/{self.total}]'

    def progress_string(self):
        indicators = self.indicator * self.indicators_needed();
        blank = ' ' * (self.length - self.indicators_needed());
        return f'\r[{indicators}{blank}]\t{self.current+1}/{self.total}'

    def fraction_complete(self):
        return self.current / self.total;

    def indicators_needed(self):
        return round(self.fraction_complete() * self.length);

    def print_progress(self, prefix='', suffix=''):
        if not self.check_rate(): return
        self._index = 0
        progress_bar = self.progress_string()
        flush_q = True if self.current != self.total else False
        end = '' if self.current != self.total else '\n'
        print(prefix+progress_bar+suffix, end=end, flush=flush_q)

    def check_rate(self):
        return self._index > self.every

    def tick(self, prefix='', suffix=''):
        self.current += 1
        self._index += 1
        self.print_progress()

    def update(self, current=None, prefix='', suffix=''):
        if current is None:
            self.tick(prefix, suffix)
        else:
            previous = self.current
            self.current = current
            self._index += current - previous
            self.print_progress(prefix, suffix)
