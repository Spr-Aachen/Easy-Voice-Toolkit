import os
import sys
import re
#import time
import shutil
import psutil
import subprocess
import hashlib
import urllib
import platform
import configparser
from pathlib import Path
from github import Github
from tqdm import tqdm
from typing import Tuple, Union, Optional
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread

##############################################################################################################################

def CheckUpdate(
    AccessToken: Optional[str] = None,
    RepoOwner: str = ...,
    RepoName: str = ...,
    FileName: str = ...,
    FileFormat: str = ...,
    Version_Current: str = ...
):
    '''
    '''
    try:
        PersonalGit = Github(AccessToken)
        Repo = PersonalGit.get_repo(f"{RepoOwner}/{RepoName}")
        Version_Latest = Repo.get_tags()[0].name
    except:
        raise Exception("Failed to get tag")

    IsUpdateNeeded = True if Version_Current != Version_Latest else False

    URL = f"https://github.com/{RepoOwner}/{RepoName}/releases/download/{Version_Latest}/{FileName}"

    SHA = "Unknown"

    try:
        CommitSHA_Latest = Repo.get_latest_release().raw_data["target_commitish"]
        for File in Repo.get_commit(CommitSHA_Latest).raw_data["Files"]:
            if File["filename"] == f"{FileName}.{FileFormat}":
                SHA = File["sha"]
    except:
        raise Exception("Failed to get commit")

    return IsUpdateNeeded, URL, SHA


def DownloadFile(
    URL: str,
    DownloadDir: str,
    FileName: str,
    FileFormat: str,
    SHA_Expected: Optional[str]
) -> Tuple[Union[bytes, str], str]:
    '''
    '''
    os.makedirs(DownloadDir, exist_ok = True)

    DownloadPath = os.path.join(DownloadDir, FileName) + '.' + FileFormat

    def Download():
        with urllib.request.urlopen(URL) as source, open(DownloadPath, "wb") as output:
            with tqdm(total = int(source.info().get("Content-Length")), ncols = 80, unit = 'iB', unit_scale = True, unit_divisor = 1024) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break
                    output.write(buffer)
                    loop.update(len(buffer))
        return open(DownloadPath, "rb").read()

    if os.path.exists(DownloadPath):
        if os.path.isfile(DownloadPath) == False:
            raise RuntimeError(f"{DownloadPath} exists and is not a regular file")
        elif SHA_Expected is not None:
            with open(DownloadPath, "rb") as f:
                FileBytes = f.read()
            if len(SHA_Expected) == 40:
                SHA_Current = hashlib.sha1(FileBytes).hexdigest()
            if len(SHA_Expected) == 64:
                SHA_Current = hashlib.sha256(FileBytes).hexdigest()
            FileBytes = Download() if SHA_Current != SHA_Expected else FileBytes #Download() if SHA_Current != SHA_Expected else None
        else:
            FileBytes = Download()
    else:
        FileBytes = Download()

    return FileBytes, DownloadPath


def CleanDirectory(
    Directory: str,
    WhiteList: list
):
    '''
    '''
    if os.path.exists(Directory):
        for DirPath, Folders, Files in os.walk(Directory, topdown = False):
            for File in Files:
                FilePath = os.path.join(DirPath, File)
                try:
                    if not any(File in FilePath for File in WhiteList):
                        os.remove(FilePath)
                except:
                    pass
            for Folder in Folders:
                FolderPath = os.path.join(DirPath, Folder)
                try:
                    if not any(Folder in FolderPath for Folder in WhiteList):
                        shutil.rmtree(FolderPath)
                except:
                    pass

#############################################################################################################

def GetPath(
    Dir: str,
    Name: str
):
    '''
    '''
    for dirpath, dirnames, filenames in os.walk(Dir):
        for dirname in dirnames:
            if dirname == Name:
                return os.path.join(dirpath, dirname)
        for filename in filenames:
            if filename == Name:
                return os.path.join(dirpath, filename)


def MoveFiles(
    Dir: str,
    Dst: str
):
    '''
    '''
    for dirpath, dirnames, filenames in os.walk(Dir):
        for dirname in dirnames:
            if Dir != Dst:
                shutil.move(os.path.join(dirpath, dirname), Dst)
        for filename in filenames:
            if Dir != Dst:
                shutil.move(os.path.join(dirpath, filename), Dst)

#############################################################################################################

def IterChecker(
    Items,
    #Type: str = 'list'
):
    '''
    '''
    try:
        iter(Items)
        ItemList = Items
    except:
        ItemList = []
        ItemList.append(Items)

    return ItemList


def ItemReplacer(
    Dict: dict,
    Items: object
):
    '''
    Function to replace item using dictionary lookup
    '''
    ItemList = IterChecker(Items)

    ItemList_New = [Dict.get(Item, Item) if isinstance(Item, str) else Item for Item in ItemList]

    if isinstance(Items, list):
        return ItemList_New
    if isinstance(Items, tuple):
        return tuple(ItemList_New)
    if isinstance(Items, (int, float, bool)):
        return ItemList_New[0]
    if isinstance(Items, str):
        return str().join(ItemList_New)

#############################################################################################################

def NormPath(
    String: str,
    PathType: Optional[str] = None,
    TrailingSlash: Optional[bool] = None
):
    '''
    '''
    if re.search(r':[/\\\\]', str(String)): #if f':{os.path.sep}' in str(String):
        if TrailingSlash is None:
            TrailingSlash = True if str(String).endswith(('/', '\\')) else False
        if platform.system() == 'Windows' or PathType == 'Win32':
            String = Path(String).as_posix().replace(r'/', '\\')
            String += '\\' if TrailingSlash else ''
        if platform.system() == 'Linux' or PathType == 'Posix':
            String = Path(String).as_posix()
            String += '/' if TrailingSlash else ''
        return String

    else:
        #print("Not a complete path")
        return String


def RawString(
    Text: str,
    PathType: Optional[str] = None
):
    '''
    Return as raw string representation of text
    '''
    RawDict = {
        '\a': r'\a',
        '\b': r'\b',
        '\c': r'\c',
        '\f': r'\f',
        '\n': r'\n',
        '\r': r'\r',
        '\t': r'\t',
        '\v': r'\v',
        '\0': r'\0',
        '\1': r'\1',
        '\2': r'\2',
        '\3': r'\3',
        '\4': r'\4',
        '\5': r'\5',
        '\6': r'\6',
        '\7': r'\7',
        '\8': r'\8',
        '\9': r'\9',
        #'\'': r'\'',
        #'\"': r'\"'
    }
    StringRepresentation = repr(ItemReplacer(RawDict, NormPath(Text, PathType)))[1:-1] #StringRepresentation = ItemReplacer(RawDict, NormPath(Text)).encode('unicode_escape').decode()
    return re.sub(r'\\+', lambda arg: r'\\', StringRepresentation).replace(r'\\', '\\').replace(r'\'', '\'') #return eval("'%s'" % canonical_string)

#############################################################################################################

def RunCMD(
    Args: list,
    PathType: Optional[str] = None,
    DecodeResult: Optional[bool] = None
):
    '''
    '''
    ArgType = 'List' if isinstance(Args[0], list) else 'String'

    if ArgType is 'List':
        Output, Error = (bytes(), bytes())
        for Arg in Args:
            Subprocess = subprocess.Popen(Arg, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, env = os.environ, creationflags = subprocess.CREATE_NO_WINDOW)
            Result = Subprocess.communicate()
            Output, Error = Output + Result[0], Error + Result[1]
        #Output, Error = Output, Error

    if ArgType is 'String':
        Input = str()
        for Arg in Args:
            Input += f'{RawString(Arg, PathType)}\n'
        if platform.system() == 'Windows':
            Input = Input.encode(encoding = 'gbk')
            ShellArgs = ['cmd']
        if platform.system() == 'Linux':
            Input = Input.encode(encoding = 'utf-8')
            ShellArgs = ['bash', '-c']
        Subprocess = subprocess.Popen(ShellArgs, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, env = os.environ, creationflags = subprocess.CREATE_NO_WINDOW)
        Output, Error = Subprocess.communicate(Input)

    return Output.decode(errors = 'ignore') if DecodeResult and Output is not None else Output, Error.decode(errors = 'ignore') if DecodeResult and Error is not None else Error, Subprocess.returncode


def SetEnvVar(
    Variable: str,
    Value: str,
    Type: str = 'Temp',
    AffectOS: bool = True
):
    '''
    '''
    #Value = RawString(Value)
    EnvValue = os.environ.get(Variable)

    if EnvValue is not None and Value not in EnvValue:
        if Type == 'Sys':
            if Variable == 'PATH':
                RunCMD(
                    Args = [
                        'for /f "usebackq tokens=2,*" %A in (`REG QUERY "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH`) do set SYSPATH=%B',
                        f'setx PATH "{Value}{os.pathsep}%SYSPATH%" /M' #f'setx PATH "%SYSPATH%{os.pathsep}{Value}" /M'
                    ]
                )
            else:
                pass
        if Type == 'User':
            if Variable == 'PATH':
                RunCMD(
                    Args = [
                        'for /f "usebackq tokens=2,*" %A in (`reg query HKCU\Environment /v PATH`) do set userPATH=%B',
                        f'setx PATH "{Value}{os.pathsep}%userPATH%"' #f'setx PATH "%userPATH%{os.pathsep}{Value}"'
                    ]
                )
            else:
                pass
        if Type == 'Temp' or AffectOS:
            EnvValue = f'{Value}{os.pathsep}{EnvValue}' #EnvValue = f'{EnvValue}{os.pathsep}{Value}'
            os.environ[Variable] = EnvValue

    if EnvValue is None:
        if Type == 'Sys':
            RunCMD(
                Args = [
                    f'setx {Variable} "{Value}" /M'
                ]
            )
        if Type == 'User':
            RunCMD(
                Args = [
                    f'setx {Variable} "{Value}"'
                ]
            )
        if Type == 'Temp' or AffectOS:
            EnvValue = Value
            os.environ[Variable] = EnvValue

#############################################################################################################

def TaskAccelerating(
    TargetList: list,
    ArgsList: list = [(), ],
    TypeList: list = ['MultiProcessing', ],
    Workers: Optional[int] = None,
    Asynchronous: bool = False,
    ShowMessages: bool = True
):
    '''
    Function to create pool for multiprocessing/multithreading to accelerate tasks
    '''
    #StartTime = int(time.time())

    ProcessPool = ProcessPoolExecutor(max_workers = Workers)
    ThreadPool = ThreadPoolExecutor(max_workers = Workers)

    for Index, Target in enumerate(TargetList):
        Args = ArgsList[Index]
        Type = TypeList[Index]

        if Type == None:
            pass
        
        elif Type == 'MultiProcessing':
            Process = ProcessPool.submit(Target, *Args)
            print(
                "Task start\n" if Asynchronous == True else f"Task start ({Index + 1}/{len(TargetList)})\n"
                f"Name : {Target.__name__}\n"
                f"PID  : {os.getpid()}\n"
                "Please wait...\n"
            ) if ShowMessages == True else print('')
            Process.result() if Asynchronous == False else None
        
        elif Type == 'MultiThreading':
            Thread = ThreadPool.submit(Target, *Args)
            print(
                "Task start\n" if Asynchronous == True else f"Task start ({Index + 1}/{len(TargetList)})\n"
                f"Name : {Target.__name__}\n"
                f"TID  : {currentThread().ident}\n"
                "Please wait...\n"
            ) if ShowMessages == True else print('')
            Thread.result() if Asynchronous == False else None

        else:
            raise Exception(f"{Type} not found! Use 'MultiProcessing' or 'MultiThreading' instead.")
        
        print(
            f"Task done ({Index + 1}/{len(TargetList)})\n"
        ) if ShowMessages == True and Asynchronous == False else print('')
    
    ProcessPool.shutdown(
        wait = True,
        cancel_futures = True
    )
    ThreadPool.shutdown(
        wait = True,
        cancel_futures = True
    )

    print(
        "All done\n"
        "全部完成\n"
    ) if ShowMessages == True else print('')

    #Endtime = int(time.time())

#############################################################################################################

def TaskTerminating(
    ProgramPath: str,
    SelfIgnored: bool = True
):
    '''
    '''
    ProgramName = os.path.basename(ProgramPath)
    IsFileCompiled = ProgramName.endswith('.exe')
    for Process in psutil.process_iter():
        if Process.pid == os.getpid() and SelfIgnored:
            continue
        if Process.name() == (ProgramName if IsFileCompiled else "python.exe") and ProgramPath in Process.cmdline():
            Process.kill()


def Booter(
    TargetDir: str = ...,
    ExecuterPath: str = ...,
    IsFileCompiled: bool = ...,
    DelayTime: int = 3
):
    '''
    subprocess.call([ExecuterPath] if IsFileCompiled else ['python.exe', ExecuterPath])
    '''
    BatFilePath = os.path.join(TargetDir, 'Booter.bat')
    with open(BatFilePath, 'w') as BatFile:
        CommandList = [
            '@echo off',
            f'ping 127.0.0.1 -n {DelayTime + 1} > nul',
            f'start "Programm Running" "{ExecuterPath}"' if IsFileCompiled else f'python "{ExecuterPath}"',
            'del "%~f0"'
        ]
        Commands = "\n".join(CommandList)
        BatFile.write(Commands)
    subprocess.Popen([BatFilePath], creationflags = subprocess.CREATE_NEW_CONSOLE).communicate() #RunCMD([BatFilePath])

#############################################################################################################

def GetFileInfo():
    '''
    Check whether python file is compiled
    '''
    FileName = Path(sys.argv[0]).name

    if getattr(sys, 'frozen', None):
        IsFileCompiled = True
    else:
        IsFileCompiled = False if FileName.endswith('.py') or sys.executable.endswith('python.exe') else True

    return FileName, IsFileCompiled


def GetBaseDir(
    FilePath: Optional[str] = None,
    ParentLevel: Optional[int] = None,
    SearchMEIPASS: bool = False
):
    '''
    Get the parent directory of file, or get the MEIPASS if file is compiled with pyinstaller
    '''
    if FilePath is not None:
        BaseDir = NormPath(Path(str(FilePath)).absolute().parents[ParentLevel if ParentLevel is not None else 0])
    elif SearchMEIPASS and getattr(sys, 'frozen', None):
        BaseDir = NormPath(sys._MEIPASS)
    else:
        BaseDir = None

    return BaseDir


class ManageConfig:
    '''
    Manage config
    '''
    def __init__(self,
        Config_Path: Optional[str] = None
    ):
        self.Config_Path = NormPath(Path(os.getenv('SystemDrive')).joinpath('Config.ini')) if Config_Path == None else Config_Path
        os.makedirs(Path(self.Config_Path).parent, exist_ok = True)

    def ReadConfig(self):
        ConfigParser = configparser.ConfigParser()
        ConfigParser.read(self.Config_Path)
        return ConfigParser

    def EditConfig(self,
        Section: str = ...,
        Option: str = ...,
        Value: str = ...,
        ConfigParser: Optional[configparser.ConfigParser] = None
    ):
        ConfigParser = self.ReadConfig() if ConfigParser == None else ConfigParser
        try:
            ConfigParser.add_section(Section)
        except:
            pass
        ConfigParser.set(Section, Option, Value)
        with open(self.Config_Path, 'w') as Config:
            ConfigParser.write(Config)

    def GetValue(self,
        Section: str = ...,
        Option: str = ...,
        InitValue: Optional[str] = None,
        ConfigParser: Optional[configparser.ConfigParser] = None
    ):
        ConfigParser = self.ReadConfig() if ConfigParser == None else ConfigParser
        try:
            Value = ConfigParser.get(Section, Option)
        except:
            if InitValue != None:
                self.EditConfig(Section, Option, InitValue, ConfigParser)
                return InitValue
            else:
                raise Exception("Need initial value")
        return Value

#############################################################################################################