@ECHO OFF
REM:: make variable scope =local.
SETLOCAL

REM:: setup the virtual environment.
%1 -m venv "../venv"

REM:: activate the virtual environment
CALL "../venv/Scripts/activate.bat"

REM:: install the required pip packages.
pip install -r requirements3.txt

REM:: clean-up the virtual environment.
CALL "../venv/Scripts/deactivate.bat"

ENDLOCAL
@ECHO ON