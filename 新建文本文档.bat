@echo OFF
setlocal enabledelayedexpansion
color 0a
echo.

set /p clientid= ������Ҫ����ɾ�����̶˿ں�(Ĭ��ɾ����һ��PID)��
echo ����ֵΪ��%clientid%
set "pid="
set "found=false"

for /f "tokens=5" %%a in ('netstat -aon ^| findstr "%clientid%"') do (
    echo �˿ں�Ϊ%%a
    set "pid=%%a"
    set "found=true"
    goto :confirm
)

:confirm
if "%found%"=="true" (
    tasklist /FI "PID eq %pid%" | find /i "%pid%" >nul
    if %errorlevel% equ 0 (
        set /p choice= �˿� %clientid% �ѱ�ռ�ã��Ƿ���ֹ�ý���(Y/N)��
        if /i "!choice!"=="Y" (
            taskkill /PID %pid% /F
            echo ���� %pid% �ѱ���ֹ��
        ) else (
            echo ȡ����ֹ���̡�
        )
    ) else (
        echo δ�ҵ�ռ�ö˿� %clientid% �Ľ��̡�
    )
) else (
    echo δ�ҵ�ʹ�ö˿� %clientid% ��Ӧ�ó���
)

PAUSE
