@echo OFF
setlocal enabledelayedexpansion
color 0a
echo.

set /p clientid= 请输入要进行删除进程端口号(默认删除第一个PID)：
echo 变量值为：%clientid%
set "pid="
set "found=false"

for /f "tokens=5" %%a in ('netstat -aon ^| findstr "%clientid%"') do (
    echo 端口号为%%a
    set "pid=%%a"
    set "found=true"
    goto :confirm
)

:confirm
if "%found%"=="true" (
    tasklist /FI "PID eq %pid%" | find /i "%pid%" >nul
    if %errorlevel% equ 0 (
        set /p choice= 端口 %clientid% 已被占用，是否终止该进程(Y/N)？
        if /i "!choice!"=="Y" (
            taskkill /PID %pid% /F
            echo 进程 %pid% 已被终止。
        ) else (
            echo 取消终止进程。
        )
    ) else (
        echo 未找到占用端口 %clientid% 的进程。
    )
) else (
    echo 未找到使用端口 %clientid% 的应用程序。
)

PAUSE
