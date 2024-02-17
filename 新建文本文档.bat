@echo OFF
setlocal enabledelayedexpansion
color 0a
echo.

set /p clientid= 请输入要进行删除进程端口号(默认删除第一个PID)：
echo 变量值为：%clientid%
netstat -aon|findstr %clientid%




for /f "tokens=5" %%a in ('netstat -aon ^| findstr "%clientid%"') do (
    echo 端口号为%%a
    taskkill /PID %%a /F
    goto :done
)
:done

PAUSE