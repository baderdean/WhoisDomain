#! /usr/bin/env python3

import sys
import whoisdomain


print("TEST: manually setup a cache", file=sys.stderr)
verbose: bool = True

# start a parameter context
pc = whoisdomain.ParameterContext(verbose=verbose)
whoisdomain.setMyCache(whoisdomain.DummyCache(verbose=verbose))
# whoisdomain.setMyCache(whoisdomain.DBMCache(dbmFile="testfile.dbm", verbose=verbose))
# whoisdomain.setMyCache(    whoisdomain.RedisCache(        verbose=verbose    ))


def lookup(what: str) -> None:
    # do a lookup
    d = whoisdomain.q2(
        what,
        pc,
    )

    # print results
    print(d.__dict__)


what: str = "google.com"
lookup(what)
# lookup(what)
