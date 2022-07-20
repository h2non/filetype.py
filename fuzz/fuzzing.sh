#!/bin/bash

set -x
set -e

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
cd "${THISDIR}/.."


# -atheris_runs - must be greater than corpus files in 'corpus' directory to produce new seeds.
# Many interactions require more rss memory - the limit must be decided.
python -m fuzz \
    -rss_limit_mb=1024 \
    -atheris_runs=$(( 1048576 + $(ls fuzz/corpus | wc -l) )) \
    -verbosity=1 \
    fuzz/corpus/ \
    ;
