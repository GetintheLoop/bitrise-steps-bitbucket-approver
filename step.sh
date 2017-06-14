#!/bin/bash
THIS_SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pip install requests
python "${THIS_SCRIPTDIR}/approvePR.py"
