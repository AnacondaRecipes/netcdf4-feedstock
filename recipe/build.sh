#!/bin/bash

if [[ $(uname) == Darwin ]]; then
    export LDFLAGS="-headerpad_max_install_names ${LDFLAGS}"
fi

export NETCDF4_DIR="${PREFIX}"
export HDF5_DIR="${PREFIX}"

${PYTHON} -m pip install \
    --no-binary :all: \
    --no-deps \
    --ignore-installed .
