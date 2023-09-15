@echo off
setlocal enabledelayedexpansion

set /a "random_seconds=!random! %% 571 + 30"

set /a "hours=random_seconds / 3600"
set /a "minutes=(random_seconds %% 3600) / 60"
set /a "seconds=random_seconds %% 60"

set /a "total_seconds=random_seconds"

echo Random seconds: %random_seconds%

set /a "time_to_wait=total_seconds - ((60 * hours * 60) + (minutes * 60) + seconds)"

echo Waiting for %hours%:%minutes%:%seconds%...
timeout /t %random_seconds% /nobreak

python checkin.py

pause

endlocal
