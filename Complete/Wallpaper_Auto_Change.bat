reg add "hkcu\control panel\desktop" /v wallpaper /t REG_SZ /d "C:\temp\UMA.jpg" /f
reg add "hkcu\control panel\desktop" /v WallpaperStyle /t REG_SZ /d 10 /f

RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters ,1 ,True