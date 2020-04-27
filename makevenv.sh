#!/bin/bash

PYTHON_V="/usr/bin/python36"

if [[ $1 ]]
then
    venv_name=$1
else
    read -p "venv name: " venv_name
fi

virtualenv -p ${PYTHON_V} ${venv_name}

read -n 1 -p ">> Install requirements file [y/n]? " install_req_file
echo ""

while [[ ${install_req_file} == "y" ]]
do
    read -p ">> Requirements file path: " file_path
    echo "Installing requirements from file: ${file_path}"
    ${venv_name}/bin/pip install -r ${file_path}

    read -n 1 -p ">> Install another requirements file [y/n]? " install_req_file
    echo ""
done

read -n 1 -p ">> Install libraries [y/n]? " install_lib
echo ""

while [[ ${install_lib} == "y" ]]
do
    read -p ">> Please input library, with or without version: " lib_name
    echo "Installing library: ${lib_name}
"
    ${venv_name}/bin/pip install ${lib_name}

    read -n 1 -p ">> Install more libraries [y/n]? " install_lib
    echo ""
done

read -n 1 -p ">> Print virtual environment libraries (pip freeze) [y/n]? " print_pip_freeze
echo ""

if [[ ${print_pip_freeze} == "y" ]]
then
    echo ""
    ${venv_name}/bin/pip freeze
    echo ""
fi

echo "Done! Created virtual environment $venv_name, using python version $PYTHON_V"
