# BrowserFix

## Browser Hijacker Repair Tool

BrowserFix is a Windows utility designed to repair common browser hijacking problems, such as unwanted search engine changes, malicious extensions, and browser settings being modified without permission.

## What BrowserFix Does

BrowserFix can:

* Remove unwanted browser extensions
* Restore Google as the default search engine
* Repair browser search settings
* Clean common browser hijacker changes
* Backup removed extension files before deletion
* Work with both Google Chrome and Microsoft Edge

## Why This Tool Exists

Browser hijackers often change browser settings to redirect searches, display unwanted advertisements, or install unwanted extensions.

Common symptoms include:

* Search engine changing to Yahoo or another provider
* Unknown extensions appearing
* Homepage changing without permission
* Browser behavior changing after restarting the computer

BrowserFix helps restore the browser to a clean state.

## How To Use

1. Close Google Chrome and Microsoft Edge.
2. Right-click `BrowserFix.exe`.
3. Select:

```
Run as administrator
```

4. Follow the messages shown in the program window.
5. Restart the browser and check your settings.

## Backup Information

Before removing extensions, BrowserFix creates backups.

Removed extensions are stored in:

```
Desktop\Extension_Backup
```

If something is removed by mistake, the backup can be used to restore it.

## Privacy

BrowserFix does not:

* Collect personal information
* Upload files
* Track browsing history
* Monitor user activity
* Send data to external services

All repairs are performed locally on the computer.

## Source Code

The source code is included so users can inspect how the program works.

Main file:

```
watchdog.py
```

## Building From Source

Requirements:

* Python 3.x
* PyInstaller

Install PyInstaller:

```
py -m pip install pyinstaller
```

Build:

```
py -m PyInstaller --onefile --name BrowserFix watchdog.py
```

## Security Notes

Because BrowserFix changes browser files and removes extensions, Windows security software may warn about it.

This can happen because:

* The program is new
* It is not digitally signed
* It modifies browser settings
* It requires administrator permission

Users should only run BrowserFix from a trusted source.

## License

Free to use and modify for personal or educational purposes.
