#include <cstdlib>
#include <iostream>
#include <vector>
#include <filesystem>
#ifdef _WIN32
    #include <windows.h>
#elif __linux__ || __unix__
    #include <unistd.h>
#endif


// Customize the path to your Python script
const std::string scriptPath = "./src/Main.py";


// Function to split a path into parent directory and file name
std::pair<std::string, std::string> splitPath(const std::string& path) {
    // Convert the path to a filesystem path and make it absolute
    std::filesystem::path fsPath(path);
    if (fsPath.is_relative()) {
        fsPath = std::filesystem::absolute(fsPath);
    }

    // Get the parent directory
    std::string parentPath = fsPath.parent_path().string();
    // Get the file name
    std::string fileName = fsPath.filename().string();

    // Return them as a pair
    return std::make_pair(parentPath, fileName);
}


// Function to get the Python executable path
std::string getPythonPath() {
    std::vector<std::string> possibleDirs;

    // Check PATH environment variable
    char* dirEnv = std::getenv("PATH");
    if (dirEnv != nullptr) {
        std::string dirStr(dirEnv);
        std::size_t prevPos = 0;
        std::size_t pos;

        while (
            (pos = dirStr.find(
                #ifdef _WIN32
                    ';'
                #elif __linux__ || __unix__
                    ':'
                #endif
                , prevPos)
            ) != std::string::npos
        ) {
            possibleDirs.push_back(dirStr.substr(prevPos, pos - prevPos));
            prevPos = pos + 1;
        }
        possibleDirs.push_back(dirStr.substr(prevPos));
    }

    // Add Conda default locations
    #ifdef _WIN32
        char* userProfile = std::getenv("USERPROFILE");
        if (userProfile != nullptr) {
            possibleDirs.push_back(std::string(userProfile) + "\\Anaconda3");
            possibleDirs.push_back(std::string(userProfile) + "\\miniconda3");
        }
        else {
            possibleDirs.push_back("C:\\ProgramData\\Anaconda3");
            possibleDirs.push_back("C:\\ProgramData\\miniconda3");
        }
    #elif __linux__ || __unix__
        char* home = std::getenv("HOME");
        if (home != nullptr) {
            possibleDirs.push_back(std::string(home) + "/anaconda3");
            possibleDirs.push_back(std::string(home) + "/miniconda3");
        }
        else {
            possibleDirs.push_back("/opt/anaconda3");
            possibleDirs.push_back("/opt/miniconda3");
        }
    #endif

    // Check for Python executable in each possible dir
    for (const auto& dir : possibleDirs) {
        std::filesystem::path pythonPath(dir);
        #ifdef _WIN32
            pythonPath /= "pythonw.exe";
        #elif __linux__ || __unix__
            pythonPath /= "python3";
            // Also check for 'python' on Unix-like systems
            if (!std::filesystem::exists(pythonPath)) {
                pythonPath = std::filesystem::path(dir) / "python";
            }
        #endif
        if (std::filesystem::exists(pythonPath)) {
            return pythonPath.string();
        }
    }

    // If still not found
    return "";
}


int main()
{
    // Get Python executable path
    std::string pythonPath = getPythonPath();
    if (pythonPath.empty()) {
        std::cout << "Failed to find Python executable path" << std::endl;
    }
    else {
        std::cout << "Python executable path: " << pythonPath << std::endl;
        return 0;
    }

    // Get script directory and name
    std::string scriptDir = splitPath(scriptPath).first;
    std::string scriptName = splitPath(scriptPath).second;

    #ifdef _WIN32
        // Set up parameters for ShellExecuteA
        HWND hWnd = nullptr;
        LPCSTR lpOperation = "open";
        LPCSTR lpFile = pythonPath.c_str();         // (如果对 lpFile 使用相对路径，请不要将相对路径用于 lpDirectory 参数)
        LPCSTR lpParameters = scriptName.c_str();   // 指定要传递给应用程序的参数 (如果 lpFile 指定文档文件，则 lpParameters 应为 NULL)
        LPCSTR lpDirectory = scriptDir.c_str();     // (如果此值为 NULL，则使用当前工作目录)
        INT nShowCmd = SW_SHOW;                     // 指定应用程序在打开时如何显示应用程序的标志

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

    #elif __linux__ || __unix__
        // Create a new process
        pid_t pid = fork();
        // Check if the fork was successful
        if (pid == -1) {
            std::cerr << "Error forking process." << std::endl;
            return 1;
        }
        else if (pid == 0) {
            // Execute Python script
            if (execl(pythonPath.c_str(), pythonPath.filename().c_str(), (scriptDir.c_str() + "/" + scriptName.c_str()), nullptr) == -1) {
                std::cerr << "Error executing Python script." << std::endl;
                return 1;
            }
        }
        else {
            wait(nullptr);
        }
        return 0;

    #else
        // TODO: Implement other version
        std::cout << "This program is not compatible with current operating system." << std::endl;
        return 1;

    #endif
}