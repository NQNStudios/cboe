#!/bin/sh -ve

export CCFLAGS='-fdiagnostics-color=always -DFMT_BEGIN_NAMESPACE="namespace fmt {" -DFMT_END_NAMESPACE="}"'
scons