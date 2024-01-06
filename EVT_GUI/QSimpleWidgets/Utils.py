import os
import sys
import re
import time
import shutil
import psutil
import signal
import shlex
import subprocess
import collections
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

#############################################################################################################

def ToIterable(
    Items,
    StrictToText: bool = True
):
    '''
    Function to make item iterable
    '''
    if isinstance(Items, collections.Iterable) or hasattr(Items, '__iter__'):
        ItemList = [Items] if StrictToText and isinstance(Items, (str, bytes)) else Items
    else:
        ItemList = [Items]

    return ItemList


def ItemReplacer(
    Dict: dict,
    Items: object
):
    '''
    Function to replace item using dictionary lookup
    '''
    ItemList = ToIterable(Items)

    ItemList_New = [Dict.get(Item, Item) if isinstance(Item, str) else Item for Item in ItemList]

    if isinstance(Items, list):
        return ItemList_New
    if isinstance(Items, tuple):
        return tuple(ItemList_New)
    if isinstance(Items, (int, float, bool)):
        return ItemList_New[0]
    if isinstance(Items, str):
        return str().join(ItemList_New)


def FindKey(
    Dict: dict,
    TargetValue
):
    for Key, Value in Dict.items():
        if Value == TargetValue:
            return Key

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
    Args: Union[list[Union[list, str]], str],
    PathType: str = 'Posix',
    ShowProgress: bool = False,
    CommunicateThroughConsole: bool = False,
    CreationFlags: int = subprocess.CREATE_NO_WINDOW,
    #InterceptError: Optional[bool] = None,
    DecodeResult: Optional[bool] = None,
    TimeOut: Optional[float] = None
):
    '''
    '''
    TimeLimit = time.time() + TimeOut if TimeOut is not None else None

    if not CommunicateThroughConsole:
        TotalOutput, TotalError = (bytes(), bytes())
        for Arg in ToIterable(Args, StrictToText = False):
            Arg = shlex.split(Arg, posix = True if PathType is 'Posix' else False) if isinstance(Arg, str) else Arg
            Subprocess = subprocess.Popen(
                args = Arg,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                env = os.environ,
                creationflags = CreationFlags
            )
            if ShowProgress:
                Output, Error = (bytes(), bytes())
                for Line in Subprocess.stdout:
                    Output += Line
                    sys.stdout.write(Line.decode(errors = 'ignore'))
                    Subprocess.stdout.flush()
                for Line in Subprocess.stderr:
                    Error += Line
                    sys.stderr.write(Line.decode(errors = 'ignore'))
                    Subprocess.stderr.flush()
                    #Subprocess.terminate() if InterceptError and 'error' in Line.decode(errors = 'ignore').lower() else None
            else:
                Output, Error = Subprocess.communicate(timeout = TimeOut)
            TotalOutput, TotalError = TotalOutput + Output, TotalError + Error

    else:
        TotalInput = str()
        for Arg in ToIterable(Args):
            Arg = shlex.join(Arg) if isinstance(Arg, list) else Arg
            TotalInput += f'{RawString(Arg, PathType)}\n'
        if platform.system() == 'Windows':
            TotalInput = TotalInput.encode(encoding = 'gbk')
            ShellArgs = ['cmd']
        if platform.system() == 'Linux':
            TotalInput = TotalInput.encode(encoding = 'utf-8')
            ShellArgs = ['bash', '-c']
        Subprocess = subprocess.Popen(
            args = ShellArgs,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            env = os.environ,
            creationflags = CreationFlags
        )
        if ShowProgress:
            TotalOutput, TotalError = (bytes(), bytes())
            Subprocess.stdin.write(TotalInput)
            Subprocess.stdin.close()
            for Line in Subprocess.stdout:
                TotalOutput += Line
                sys.stdout.write(Line.decode(errors = 'ignore'))
                Subprocess.stdout.flush()
            for Line in Subprocess.stderr:
                TotalError += Line
                sys.stderr.write(Line.decode(errors = 'ignore'))
                Subprocess.stderr.flush()
                #Subprocess.terminate() if InterceptError and 'error' in Line.decode(errors = 'ignore').lower() else None
        else:
            TotalOutput, TotalError = Subprocess.communicate(TotalInput, timeout = TimeOut)

    TotalOutput, TotalError = TotalOutput.strip(), TotalError.strip()
    TotalOutput, TotalError = TotalOutput.decode(errors = 'ignore') if DecodeResult else TotalOutput, TotalError.decode(errors = 'ignore') if DecodeResult else TotalError

    return None if TotalOutput in ('', b'') else TotalOutput, None if TotalError in ('', b'') else TotalError, Subprocess.returncode


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
                    ],
                    CommunicateThroughConsole = True
                )
            else:
                pass
        if Type == 'User':
            if Variable == 'PATH':
                RunCMD(
                    Args = [
                        'for /f "usebackq tokens=2,*" %A in (`reg query HKCU\Environment /v PATH`) do set userPATH=%B',
                        f'setx PATH "{Value}{os.pathsep}%userPATH%"' #f'setx PATH "%userPATH%{os.pathsep}{Value}"'
                    ],
                    CommunicateThroughConsole = True
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
                ],
                CommunicateThroughConsole = True
            )
        if Type == 'User':
            RunCMD(
                Args = [
                    f'setx {Variable} "{Value}"'
                ],
                CommunicateThroughConsole = True
            )
        if Type == 'Temp' or AffectOS:
            EnvValue = Value
            os.environ[Variable] = EnvValue

#############################################################################################################

def SetRichText(
    Title: Optional[str] = None,
    TitleAlign: str = "left",
    TitleSize: float = 12.3,
    TitleWeight: float = 630.,
    TitleColor: str = "#ffffff",
    TitleSpacing: float = 0.9,
    TitleLineHeight: float = 24.6,
    Body: Optional[str] = None,
    BodyAlign: str = "left",
    BodySize: float = 9.9,
    BodyWeight: float = 420.,
    BodySpacing: float = 0.6,
    BodyLineHeight: float = 22.2,
    BodyColor: str = "#ffffff",
):
    '''
    Function to set text for widget
    '''
    def ToHtml(Content, Align, Size, Weight, Color, LetterSpacing, LineHeight):
        Style = f"'text-align:{Align}; font-size:{Size}pt; font-weight:{Weight}; color:{Color}; letter-spacing: {LetterSpacing}px; line-height: {LineHeight}px'"
        Content = re.sub(
            pattern = "[\n]",
            repl = "<br>",
            string = Content
        ) if Content is not None else None
        return f"<p style={Style}>{Content}</p>" if Content is not None else ''

    RichText = (
        "<html>"
            "<head>"
                f"<title>{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleSpacing, TitleLineHeight)}</title>" # Not working with QWidgets
            "</head>"
            "<body>"
                f"{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleSpacing, TitleLineHeight)}"
                f"{ToHtml(Body, BodyAlign, BodySize, BodyWeight, BodyColor, BodySpacing, BodyLineHeight)}"
            "</body>"
        "</html>"
    )

    return RichText

#############################################################################################################

def FindURL(
    String: str
):
    '''
    '''
    URLList = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+').findall(RawString(String))
    URL = URLList[0]

    return URL

#############################################################################################################

def RunEvent(
    EventList: Optional[list] = None,
    ParamList: Optional[list[tuple]] = None
):
    '''
    '''
    EventList = ToIterable(EventList) if EventList is not None else []
    ParamList = ToIterable(ParamList) if ParamList is not None else [()]
    for Index, Event in enumerate(EventList):
        Event(*ToIterable(ParamList[Index]))

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


def ProcessTerminator(
    Program: str,
    SelfIgnored: bool = True,
    SearchKeyword: bool = False
):
    '''
    '''
    ProgramPath = NormPath(Program)
    for Process in psutil.process_iter():
        if Process.pid == os.getpid() and SelfIgnored:
            continue
        try:
            for CMDLine in Process.cmdline():
                if ProgramPath == CMDLine or (ProgramPath in CMDLine and SearchKeyword):
                    ProgramName = Path(ProgramPath).name if ProgramPath.endswith('.exe') else 'python.exe'
                    if Process.name() == ProgramName:
                        Process.send_signal(signal.SIGTERM) #Process.kill()
                    else:
                        print(f'Failed to terminate {ProgramName}')
        except:
            pass

#############################################################################################################

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


def MoveFiles(
    Dir: str,
    Dst: str
):
    '''
    '''
    for DirPath, FolderNames, FileNames in os.walk(Dir):
        for FolderName in FolderNames:
            if Dir != Dst:
                shutil.move(os.path.join(DirPath, FolderName), Dst)
        for FileName in FileNames:
            if Dir != Dst:
                shutil.move(os.path.join(DirPath, FileName), Dst)


def GetPaths(
    Dir: str,
    Name: str,
    SearchKeyword: bool = True
):
    '''
    '''
    Result = []

    for DirPath, FolderNames, FileNames in os.walk(Dir):
        for FolderName in FolderNames:
            if Name == FolderName or (Name in FolderName and SearchKeyword is True):
                Result.append(os.path.join(DirPath, FolderName))
            else:
                pass
        for FileName in FileNames:
            if Name == FileName or (Name in FileName and SearchKeyword is True):
                Result.append(os.path.join(DirPath, FileName))
            else:
                pass

    return Result if len(Result) > 0 else None

#############################################################################################################

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


def GetFileInfo(
    File: Optional[str] = None
):
    '''
    Check whether python file is compiled
    '''
    if File is None:
        FileName = Path(sys.argv[0]).name
        if getattr(sys, 'frozen', None):
            IsFileCompiled = True
        else:
            IsFileCompiled = False if FileName.endswith('.py') or sys.executable.endswith('python.exe') else True
    else:
        FileName = Path(NormPath(File)).name
        IsFileCompiled = False if FileName.endswith('.py') else True

    return FileName, IsFileCompiled

#############################################################################################################

def RunBat(
    CommandList: list[str],
    BatFilePath: Optional[str]
):
    '''
    '''
    BatFilePath = Path.cwd().joinpath('Bat.bat') if BatFilePath is None else NormPath(BatFilePath)
    with open(BatFilePath, 'w') as BatFile:
        Commands = "\n".join(CommandList)
        BatFile.write(Commands)
    subprocess.Popen([BatFilePath], creationflags = subprocess.CREATE_NEW_CONSOLE).communicate()


def BootWithBat(
    ProgramPath: str = ...,
    DelayTime: int = 3,
    BatFilePath: Optional[str] = None
):
    '''
    subprocess.call([ProgramPath] if GetFileInfo(ProgramPath)[1] else ['python.exe', ProgramPath])
    '''
    _, IsFileCompiled = GetFileInfo(ProgramPath)
    RunBat(
        CommandList = [
            '@echo off',
            f'ping 127.0.0.1 -n {DelayTime + 1} > nul',
            f'start "Programm Running" "{ProgramPath}"' if IsFileCompiled else f'python "{ProgramPath}"',
            'del "%~f0"'
        ],
        BatFilePath = BatFilePath
    )

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
        LatestRelease = Repo.get_latest_release() #LatestRelease = Repo.get_release(Version_Latest)
        for Index, Asset in enumerate(LatestRelease.assets):
            if Asset.name == f"{FileName}.{FileFormat}":
                IsUpdateNeeded = True if Version_Current != Version_Latest else False
                DownloadURL = Asset.browser_download_url #DownloadURL = f"https://github.com/{RepoOwner}/{RepoName}/releases/download/{Version_Latest}/{FileName}.{FileFormat}"
                return IsUpdateNeeded, DownloadURL
            elif Index + 1 == len(LatestRelease.assets):
                raise Exception(f"No file found with name {FileName}.{FileFormat} in the latest release")

    except Exception as e:
        print(f"Error occurred while checking for updates: \n{e}")


def DownloadFile(
    DownloadURL: str,
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
        with urllib.request.urlopen(DownloadURL) as source, open(DownloadPath, "wb") as output:
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

#############################################################################################################

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