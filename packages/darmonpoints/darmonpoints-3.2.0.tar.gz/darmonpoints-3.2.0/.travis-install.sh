#! /bin/bash
set -e
SAGE_IMAGE=`python2 -c "import setup; print setup.get_all_version_names('${SAGE_SERVER}index.html',${SAGE_AGE})"`
cd $HOME
if [ ! -x SageMath/sage ] ; then
    rm -f SageMath.tar.bz2
    wget ${SAGE_SERVER}${SAGE_IMAGE} -O SageMath.tar.bz2
    tar xf SageMath.tar.bz2
fi
MAKE="make -j4"
export MAKE
# Install packages
#SageMath/sage -i lrslib
# To initialize matplotlib font manager
SageMath/sage -python -c 'import matplotlib.pyplot'
