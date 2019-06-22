#!/bin/bash

PYTHON_V="/usr/bin/python36"

if [[ $1 ]]
then
    venv_name=$1
else
    read -p "venv name: " venv_name
fi

#echo "venv name from input: $venv_name"

virtualenv -p ${PYTHON_V} ${venv_name}

read -n 1 -p "
Install requirements file [y/n]? " install_req_file

if [[ ${install_req_file} == "y" ]]
then
    read -p "
    requirements file path: " file_path
    echo "Installing requirements from file: ${file_path}"
    ${venv_name}/bin/pip install -r ${file_path}
fi

read -n 1 -p "
Install libraries [y/n]? " install_lib

if [[ ${install_lib} == "y" ]]
then
    read -p "
    Please input library, with or without version: " lib_name
    echo "Installing library: ${lib_name}"
    ${venv_name}/bin/pip install ${lib_name}
fi

echo "Done! Created virtual environment $venv_name, using python version $PYTHON_V"
