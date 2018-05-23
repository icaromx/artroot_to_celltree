#!/bin/bash

source /grid/fermiapp/products/uboone/setup_uboone.sh

setup uboonecode v06_43_00_01 -q e14:prof
#setup uboonecode v06_26_01_06 -q e10:prof
#setup uboonecode v06_61_00 -q e14:prof


export WIRECELLFUNPATH=/uboone/app/users/icaro/WC
#########################################################
#source ${WIRECELLFUNPATH}/wire-cell/waf-tools/sourceme-for-ups
#setup uboonecode v06_56_00 -q e14:nu:prof
#########################################################

export PATH=${WIRECELLFUNPATH}/wire-cell/install/bin:$PATH
export LD_LIBRARY_PATH=${WIRECELLFUNPATH}/wire-cell/install/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=${WIRECELLFUNPATH}/wire-cell/install/lib64:$LD_LIBRARY_PATH
export PYTHONPATH=${WIRECELLFUNPATH}/wire-cell/install/lib:$PYTHONPATH
export PYTHONPATH=${WIRECELLFUNPATH}/wire-cell/insatll/lib64:$PYTHONPATH

##########################################################################################
#export PKG_CONFIG_PATH=${WIRECELLFUNPATH}/Eigen_install/share/pkgconfig:$PKG_CONFIG_PATH
#export PKG_CONFIG_PATH=${WIRECELLFUNPATH}/fftw3share/lib/pkgconfig:$PKG_CONFIG_PATH
#export PKG_CONFIG_PATH=${WIRECELLFUNPATH}/fftw_bin/lib/pkgconfig:$PKG_CONFIG_PATH
#export CPATH=${WIRECELLFUNPATH}/Eigen_install/include/eigen3:$CPATH

#export PATH=${SEISMIC}/bin:$PATH
#export LD_LIBRARY_PATH=${SEISMIC}/lib:$LD_LIBRARY_PATH
#export LD_LIBRARY_PATH=${SEISMIC}/lib64:$LD_LIBRARY_PATH
#export PYTHONPATH=${SEISMIC}/lib:$PYTHONPATH
#export PYTHONPATH=${SEISMIC}/lib64:$PYTHONPATH
###########################################################################################

source ${WIRECELLFUNPATH}/wire-cell/waf-tools/sourceme-for-ups


####################################################################################################################
#alias waf='${WIRECELLFUNPATH}/wire-cell/waf-tools/waf --prefix=${WIRECELLFUNPATH}/wire-cell/ configure build install'
##################################################################################################################
alias waf='${WIRECELLFUNPATH}/wire-cell/waf-tools/waf --prefix=${WIRECELLFUNPATH}/wire-cell/ build install'
##################################################################################################################
#alias seismic='${SEISMIC}/waf-tools/waf --prefix=${SEISMIC}/ configure build install'
#################################################################################################################
