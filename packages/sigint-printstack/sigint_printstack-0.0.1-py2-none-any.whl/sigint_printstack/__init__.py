# coding: utf-8

import signal
import datetime
import traceback

last_sigint_time = None


def sigint_handler(sig, stack):
    global last_sigint_time
    now = datetime.datetime.now()
    if not last_sigint_time:
        stop = False
    elif now - last_sigint_time < datetime.timedelta(seconds=1):
        stop = True
    else:
        stop = False
    last_sigint_time = now
    if stop:
        signal.default_int_handler(sig, stack)
    else:
        traceback.print_stack(stack)

_signal = signal.signal


def new_signal(sig, action):
    if sig == signal.SIGINT:
        def _(sig, stack):
            traceback.print_stack(stack)
            return action(sig, stack)
        return _signal(sig, _)
    else:
        return _signal(sig, action)

signal.signal(signal.SIGINT, sigint_handler)
signal.signal = new_signal
