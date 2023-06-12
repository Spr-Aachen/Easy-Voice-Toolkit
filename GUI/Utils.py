import os
import configparser
#import time
import hashlib
import shutil
import urllib
from github import Github
from tqdm import tqdm
from typing import Tuple, Union, Optional
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread


class ManageConfig:
    '''
    Manage config
    '''
    def __init__(self,
        Config_Path: Optional[str] = None
    ):
        self.Config_Path = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'Config.ini') if Config_Path == None or not os.path.exists(Config_Path) else Config_Path
    
    def ReadConfig(self):
        ConfigParser = configparser.ConfigParser()
        ConfigParser.read(self.Config_Path, encoding = 'utf-8')
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


def CheckUpdate(AccessToken: str, RepoOwner: str, RepoName: str, FileName: str, Version_Current: str):
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
            if File["filename"] == FileName:
                SHA = File["sha"]
    except:
        raise Exception("Failed to get commit")

    return IsUpdateNeeded, URL, SHA


def FileDownload(URL: str, DownloadDir: str, FileName: str, FileFormat: str, SHA_Expected: str) -> Tuple[Union[bytes, str], str]:
    
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
        else:
            with open(DownloadPath, "rb") as f:
                FileBytes = f.read()
            if len(SHA_Expected) == 40:
                SHA_Current = hashlib.sha1(FileBytes).hexdigest()
            if len(SHA_Expected) == 64:
                SHA_Current = hashlib.sha256(FileBytes).hexdigest()
            Download() if SHA_Current != SHA_Expected else None
    else:
        FileBytes = Download()

    return FileBytes, DownloadPath


def Updater(
    CurrentVersion: str = ...,
    DownloadDir: str = ...,
    Name: str = ...,
    #Format: str = 'zip',
    ExtractDir: str = ...
):
    Format = 'zip'

    try:
        IsUpdateNeeded, URL, SHA = CheckUpdate(
            AccessToken = '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',
            RepoOwner = 'Spr-Aachen',
            RepoName = 'Easy-Voice-Toolkit',
            FileName = f'EVT.{Format}',
            Version_Current = CurrentVersion
        )
        
    except:
        print("Failed to check for update")

    else:
        if IsUpdateNeeded:
            if os.path.exists(ExtractDir):
                FoldersToKeep = ['__pycache__', '.git']
                for Root, Dirs, Files in os.walk(ExtractDir, topdown = False):
                    for File in Files:
                        FilePath = os.path.join(Root, File)
                        try:
                            if not any(Folder in FilePath for Folder in FoldersToKeep):
                                os.remove(FilePath)
                        except:
                            pass
                    for Dir in Dirs:
                        DirPath = os.path.join(Root, Dir)
                        try:
                            if not any(Folder in DirPath for Folder in FoldersToKeep):
                                shutil.rmtree(DirPath)
                        except:
                            pass
            print("Start updating!")
            try:
                shutil.unpack_archive(
                    filename = FileDownload(
                        URL = URL,
                        DownloadDir = DownloadDir,
                        FileName = Name,
                        FileFormat = Format,
                        SHA_Expected = SHA
                    )[1],
                    extract_dir = ExtractDir,
                    format = Format
                )
            except:
                shutil.unpack_archive(
                    filename = FileDownload(
                        URL = 'https://ghproxy.com/' + URL,
                        DownloadDir = DownloadDir,
                        FileName = Name,
                        FileFormat = Format,
                        SHA_Expected = SHA
                    )[1],
                    extract_dir = ExtractDir,
                    format = Format
                )
            print("Successfully updated!")

        else:
            print("Already up to date!")


def ItemReplacer(
    Dict: dict,
    Item: object
):
    '''
    Function to replace items using dictionary lookup
    '''
    if isinstance(Item, str):
        return Dict.get(Item)
    else:
        try:
            iter(Item)
            ItemList = Item
        except:
            ItemList = []
            ItemList.append(Item)

    ItemList_New = [Dict.get(Item, Item) if isinstance(Item, str) else Item for Item in ItemList]

    if isinstance(Item, list):
        return ItemList_New
    if isinstance(Item, tuple):
        return tuple(ItemList_New)
    if isinstance(Item, (int, float, bool)):
        return ItemList_New[0]


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