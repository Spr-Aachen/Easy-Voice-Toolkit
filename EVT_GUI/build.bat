@echo off
windres icon.rc -o icon.o
gcc main.c icon.o -o main.exe -mwindows -s
upx main.exe
pause