@echo OFF
setlocal enabledelayedexpansion
color 0a
echo.

set /p clientid= ������Ҫ����ɾ�����̶˿ں�(Ĭ��ɾ����һ��PID)��
echo ����ֵΪ��%clientid%
netstat -aon|findstr %clientid%




for /f "tokens=5" %%a in ('netstat -aon ^| findstr "%clientid%"') do (
    echo �˿ں�Ϊ%%a
    taskkill /PID %%a /F
    goto :done
)
:done

PAUSE