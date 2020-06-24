# Reboot Now!

Reboot to a specific device easily (HDD2, USB, CDROM, BIOS Setup, etc.) 

![image](https://user-images.githubusercontent.com/6168083/85631445-d6d60300-b675-11ea-95d4-32dee62ae18b.png)

# Why this tool?

You probably know the problem since years: let's say you want to reboot your computer on HDD2 or HDD3, to boot on another OS than the main OS. You have to:

* open *Start menu > Restart computer*

* Wait a few seconds for the shutdown, wait a few seconds for the initial BIOS boot

* Depending on your computer, press `F1`, `F12`, `DEL` at the *right precise timing* after reboot to trigger the *"Select the alternate device you want to boot on"* option

* Wait a few seconds again

* Sometimes you have to press another button, and wait again

* Select the device in the boot menu

* Sometimes you miss the precise timing, and you have to restart again!

**This tool allows the user to choose the next device to boot on, directly from Windows, and reboots.**

Thus, you don't need to "babysit" the reboot and waste 1 minute of your life pressing keys at the right timing.

# Pro tip

You can use AutoHotkey to associate `CTRL+WIN+ALT+DELETE` with this tool:

    ^!#Del:: Run python "D:\path\to\rebootnow.py"
