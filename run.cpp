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
    const std::string &profileDir,
    const bool isCompiled = false
) {
    std::string currentDir = GetCurrentDir();

    std::string resourceDir = currentDir; // For simplicity, same as currentDir (no MEIPASS equivalent)

    std::string clientDir = resourceDir + "\\" + (isCompiled ? "EVT" : "EVT_GUI");

    std::string clientFile;
    if (isCompiled) {
        clientFile = clientDir + "\\Main.exe";
    }
    else {
        clientFile = clientDir + "\\src\\main.py";
    }

    std::string coreFile = currentDir + "\\EVT_Core\\main.py";

    std::string command = (isCompiled ? "" : "python \"") + clientFile + (isCompiled ? "\"" : "\"");
    command += " --EVT_Core \"" + coreFile + "\"";
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
        clientDir.c_str(),
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
        currentDir);

    return 0;
}