#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <windows.h>
#include <shlwapi.h>


#pragma comment(lib, "shlwapi.lib")


std::string GetCurrentDir() {
    char path[MAX_PATH];
    GetModuleFileNameA(NULL, path, MAX_PATH);
    PathRemoveFileSpecA(path);
    return std::string(path);
}


void RunProcess(
    const std::string &manifestPath,
    const std::string &requirementsPath,
    const std::string &dependencyDir,
    const std::string &modelDir,
    const std::string &outputDir,
    const std::string &profileDir
) {
    std::string currentDir = GetCurrentDir();

    std::string clientFile = currentDir + "\\client\\src\\main.py";
    std::string serverPath = currentDir + "\\server\\app\\main.py";

    std::string command = "python \"" + clientFile + "\"";
    command += " --server \"" + serverPath + "\"";
    command += " --manifest \"" + manifestPath + "\"";
    command += " --requirements \"" + requirementsPath + "\"";
    command += " --dependencies \"" + dependencyDir + "\"";
    command += " --models \"" + modelDir + "\"";
    command += " --output \"" + outputDir + "\"";
    command += " --profile \"" + profileDir + "\"";

    //std::cout << "Executing: " << command << std::endl;

    STARTUPINFOA si = {sizeof(STARTUPINFOA)};
    PROCESS_INFORMATION pi;
    bool isCreationSucceeded = CreateProcessA(
        NULL,
        (LPSTR)command.c_str(),
        NULL,
        NULL,
        FALSE,
        CREATE_NO_WINDOW,
        NULL,
        currentDir.c_str(),
        &si,
        &pi
    );
    if (!isCreationSucceeded) {
        DWORD error = GetLastError();
        std::cerr << "CreateProcess failed (" << error << ")" << std::endl;
        return;
    }

    // Don't wait
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
}


// Run
int main() {
    std::string currentDir = GetCurrentDir();

    RunProcess(
        currentDir + "\\manifest.json",
        currentDir + "\\requirements.txt",
        currentDir,
        currentDir + "\\Models",
        currentDir,
        currentDir
    );

    return 0;
}