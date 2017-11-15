#!/bin/bash
THIS_SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pip2 install requests
python "${THIS_SCRIPTDIR}/approvePR.py"
