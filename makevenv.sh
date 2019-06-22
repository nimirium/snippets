#!/bin/bash

python_v="/usr/bin/python36"

read -p "venv name: " venv_name

virtualenv -p ${python_v} ${venv_name}

read -n 1 -p "install requirements file [y/n]? " yn

if [[ ${yn} == "y" ]]
then
    read -p "
    requirements file path: " file_path
    echo "Installing requirements from file: ${file_path}"
    ${venv_name}/bin/pip install -r ${file_path}
fi

read -n 1 -p "install libraries [y/n]? " yn

if [[ ${yn} == "y" ]]
then
    read -p "
    Please input library, with or without version: " lib_name
    echo "Installing library: ${lib_name}"
    ${venv_name}/bin/pip install ${lib_name}
fi

echo "Done! created virtual environment in $venv_name, using python version $python_v"
