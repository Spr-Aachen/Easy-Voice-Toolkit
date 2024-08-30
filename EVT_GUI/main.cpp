#include <windows.h>
#include <iostream>


int main()
{
    #ifdef _WIN32
        // Get current directory
        char currentDir[MAX_PATH];
        GetCurrentDirectoryA(MAX_PATH, currentDir);
        // Get script directory
        std::string scriptDir = std::string(currentDir) + "\\src";

        // Set up parameters for ShellExecuteA
        HWND hWnd = nullptr;
        LPCSTR lpOperation = "open";
        LPCSTR lpFile = "./bin/pythonw.exe";      //(如果对 lpFile 使用相对路径，请不要将相对路径用于 lpDirectory 参数)
        LPCSTR lpParameters = "Main.py";          //指定要传递给应用程序的参数 (如果 lpFile 指定文档文件，则 lpParameters 应为 NULL)
        LPCSTR lpDirectory = scriptDir.c_str();   //(如果此值为 NULL，则使用当前工作目录)
        INT nShowCmd = SW_SHOW;                   //指定应用程序在打开时如何显示应用程序的标志

        // Execute ShellExecuteA
        HINSTANCE result = ShellExecuteA(
            hWnd,      
            lpOperation, 
            lpFile,      
            lpParameters,
            lpDirectory,
            nShowCmd
        );

        // Check if the execution was successful
        if (reinterpret_cast<intptr_t>(result) <= 32) {
            std::cerr << "Error opening Python script. Error code: " << reinterpret_cast<intptr_t>(result) << std::endl;
            return 1;
        }
        return 0;

    #else
        std::cout << "This program is only compatible with Windows operating systems." << std::endl;
        return 1;

    #endif
}