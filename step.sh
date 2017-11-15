#!/bin/bash
THIS_SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pip2 install requests
python2 "${THIS_SCRIPTDIR}/approvePR.py"
