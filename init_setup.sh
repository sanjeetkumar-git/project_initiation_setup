echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activate virtual env"
source activate ./env
echo [$(date)]: "Intalling requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"