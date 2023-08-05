from .decorator import coroutine


@coroutine
def trivialConsumer():
    try:
        while True:
            s = yield
            print(s)
    except StopIteration:
        pass

@coroutine
def fileConsumer(fname, mode='w'):
    try:
        with open(fname, mode) as f:
            while True:
                s = yield
                f.write(s)
    except StopIteration:
        pass


class DoneConsuming(Exception): pass


@coroutine
def limitedConsumer(n):
    for x in range(n):
        s = yield
        print(s, end='')
    print()
    s = yield DoneConsuming


class ConsumeToBuffer():
    def __init__(self, count):
        self.l = []
        self.count = count

    @coroutine
    def consumer(self):
        for i in range(self.count):
            s = (yield)
            self.l.append(s)

    @coroutine
    def bufferedconsumer(self, ncr=None):
        while True:
            s = (yield)
            self.l.append(s)
            if ncr:
                ncr.send(s)

    def output(self):
        l = self.l
        self.l = []
        return l
