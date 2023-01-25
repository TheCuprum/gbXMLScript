$dir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $dir

& .\_venv\Scripts\Activate.ps1
pip freeze > requirements.txt
pip download -r requirements.txt -d .\pip_packages