#! /bin/bash

doIt()
{
    black --line-length 120 .

    pylama *.py whois/ |
    awk '
    /__init__/ && / W0611/ { next }
#    / W0401 / { next }
    / E501 / { next } # E501 line too long [pycodestyle]
    / E203 / { next } # E203 whitespace before ':' [pycodestyle]
    / C901 / { next } # C901 <something> is too complex (<nr>) [mccabe]
    { print }
    '
}

main()
{
    ls *.py >/dev/null 2>/dev/null && doIt

    mypy --strict --no-incremental *.py
    mypy --strict --no-incremental whoisdomain
}

main
