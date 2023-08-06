"""Parallel library"""

from funpy import it

from concurrent import futures

from typing import Callable, Iterable, Type

Pool = Type[futures.Executor]

ThreadPool = futures.ThreadPoolExecutor

ProcessPool = futures.ProcessPoolExecutor


def pmap(
    f: Callable,
    *ls: Iterable,
    workers: int = None,
    timeout: int = None,
    chunksize: int = 1,
    pool: Pool = ProcessPool,
) -> Iterable:
    """Parallel of map.

    >>> list(pmap(pow, range(1, 5), range(1, 6), pool=ThreadPool))
    [1, 4, 27, 256]
    """
    with pool(max_workers=workers) as p:  # type: ignore
        yield from p.map(f, *ls, timeout=timeout, chunksize=chunksize)


def mapreduce(
    mapper: Callable,
    reducer: Callable,
    *ls: Iterable,
    workers: int = None,
    timeout: int = None,
    chunksize: int = 1,
    pool: Pool = ProcessPool,
) -> Iterable:
    """Parallel mapreduce.

    >>> def mapper(x): return x % 2, x
    >>> def reducer(xs): return sum(xs)
    >>> list(mapreduce(mapper, reducer, range(5), pool=ThreadPool))
    [(0, 6), (1, 4)]
    """
    with pool(max_workers=workers) as p:  # type: ignore
        mapped = p.map(mapper, *ls, timeout=timeout, chunksize=chunksize)

        grouped = it.groupkv(mapped)

        reduced = ((k, p.submit(reducer, v)) for k, v in grouped)

        yield from ((k, v.result(timeout=timeout)) for k, v in reduced)
