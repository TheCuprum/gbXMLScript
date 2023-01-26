$dir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $dir

& .\_venv\Scripts\Activate.ps1 
python .\edit_block_10-10-6.py
deactivate