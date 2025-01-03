@ECHO OFF

REM Retrieve the current IP address
for /f "tokens=2 delims=:" %%A in ('ipconfig ^| findstr "IPv4 Address"') do (
    for /f "tokens=* delims= " %%B in ("%%A") do (
        set IP=%%B
    )
)

REM Trim any leading spaces (if needed)
set IP=%IP:~1%

REM Start the server with the current IP address
start cmd.exe /C "python3 manage.py runsslserver %IP%:3000"
