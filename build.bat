@echo off
windres icon.rc -o icon.o
g++ run.cpp icon.o -o Run.exe -mwindows -s
upx Run.exe
pause