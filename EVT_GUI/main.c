#include <windows.h>


int main()
{
    ShellExecuteA(NULL, "open", "bin\\pythonw.exe", "main.py", "src", SW_SHOW);
    return 0;
}