import cProfile
import functools
import logging
import pstats
import sys

import six


_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)
_stream_handler = logging.StreamHandler(sys.stdout)
_stream_handler.setLevel(logging.DEBUG)
_logger.addHandler(_stream_handler)


def profile(
        fn=None, sort_key='cumtime', n=20, prefix='', suffix='', logger=None):

    if fn is None:
        return functools.partial(
            profile, sort_key=sort_key, n=n, prefix=prefix, suffix=suffix,
            logger=logger)

    @functools.wraps(fn)
    def hook(*args, **kwargs):
        out = logger
        if out is None:
            out = _logger
        stream = six.StringIO()

        cp = cProfile.Profile()
        cp.enable()
        stream.write(prefix)
        ret = fn(*args, **kwargs)
        st = pstats.Stats(cp, stream=stream)
        st.strip_dirs().sort_stats(sort_key).print_stats(n)
        stream.write(suffix)
        out.debug(stream.getvalue())
        return ret

    return hook
