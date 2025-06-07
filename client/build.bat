@echo off
windres icon.rc -o icon.o
g++ main.cpp icon.o -o Main.exe -mwindows -s
upx Main.exe
pause