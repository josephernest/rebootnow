# Reboot Now!
# https://github.com/josephernest/rebootnow

import ctypes, win32api, win32security, struct  # do this if necessary: pip install pywin32

# Get elevated privileges
htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
newPrivileges = [(win32security.LookupPrivilegeValue(None, win32security.SE_SYSTEM_ENVIRONMENT_NAME), win32security.SE_PRIVILEGE_ENABLED),
                 (win32security.LookupPrivilegeValue(None, win32security.SE_SHUTDOWN_NAME), win32security.SE_PRIVILEGE_ENABLED)]
win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)

# Get UEFI Variables
EFI_GLOBAL_VARIABLE = "{8BE4DF61-93CA-11D2-AA0D-00E098032B8C}"
kernel32 = ctypes.WinDLL('kernel32')
GetFirmwareEnvironmentVariable = kernel32.GetFirmwareEnvironmentVariableW
SetFirmwareEnvironmentVariable = kernel32.SetFirmwareEnvironmentVariableW
for i in range(100):
    buf = ctypes.create_string_buffer(1000)
    GetFirmwareEnvironmentVariable("Boot%04X" % i, EFI_GLOBAL_VARIABLE, buf, 1000)
    description = buf.raw[6:].decode('utf16', 'ignore').split('\x00')[0]
    if description != '':
        print(i, description)

# Set UEFI Variable and reboot
print('On which device do you want to reboot?')
try:
    bootnext = int(input())
    res = SetFirmwareEnvironmentVariable("BootNext", EFI_GLOBAL_VARIABLE, struct.pack('<H', bootnext), 2)
    win32api.InitiateSystemShutdown(None, None, 0, True, True)
except:
    print('Error: Please run it from a terminal to be able to enter a number.')
