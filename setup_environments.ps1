$dir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $dir

python -m venv .\_venv
& .\_venv\Scripts\Activate.ps1

pip install --no-index --find-links=.\pip_packages -r .\requirements.txt