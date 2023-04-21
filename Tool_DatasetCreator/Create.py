'''
Edited
'''
#This script will change the encoding of the srt file, and then extract the information as well
#as store it in a csv file. According to the info in this csv file, the audio is splitted
#the splitted audio and transcripts are then merged and cleaned.

#import time, datetime
import os, sys, shutil
from glob import glob

from .utils.Creating_Directories import create_directories
from .utils.Convert_SRT_to_CSV import change_encoding, convert_srt_to_csv
from .utils.Change_Sample_Rate import pre_process_audio
from .utils.Split_Audio import split_files
from .utils.Create_DS_CSV import create_DS_csv
from .utils.Merge_CSV import merge_csv
from .utils.Merge_Transcripts_and_Files import merge_transcripts_and_wav_files
from .utils.Clean import clean_unwanted_characters
from .utils.Create_Dataset_Loading_Script import Transcript_Writer


#start_time = time.time()


class Dataset_Creating:
    '''
    1. Convert SRT to CSV
    2. Reorgnize CSV content
    3. Split and downsample WAV
    '''
    def __init__(self,
        SRT_Dir: str,
        WAV_Dir: str,
        WAV_SampleRate: int = 22050,
        WAV_Subtype: str = 'PCM_16',
        WAV_Dir_Split: str = './WAV_Files_Split',
        #WAV_Time_Limitation: float = 10.00,
        AutoEncoder: str = 'VITS',
        IsSpeakerMultiple: bool = False,
        FileList_Path_Training: str = './FileLists/Train_FileList.txt',
        FileList_Path_Validation: str = './FileLists/Val_FileList.txt'
    ):
        self.SRT_Dir = SRT_Dir
        self.WAV_Dir = WAV_Dir
        self.WAV_SampleRate = WAV_SampleRate
        self.WAV_Subtype = WAV_Subtype
        self.WAV_Dir_Split = WAV_Dir_Split
        #self.WAV_Time_Limitation = WAV_Time_Limitation
        self.AutoEncoder = AutoEncoder
        self.IsSpeakerMultiple = IsSpeakerMultiple
        self.FileList_Path_Training = FileList_Path_Training
        self.FileList_Path_Validation = FileList_Path_Validation

    '''
    def FolderCreator(self):
        # Check if SRT files directory exists and contains srt files
        if os.path.exists(self.SRT_Dir):
            print('Folder %s exists.. continuing processing..' %self.SRT_Dir)
        else:
            print('Trying to create folder for SRT files')
            try:
                os.mkdir(self.SRT_Dir)
            except OSError:
                print('Creation of directory %s failed' %self.SRT_Dir)
            else:
                print('Successfully created the directory %s' %self.SRT_Dir)
            print('--> Please add srt files to folder %s' %self.SRT_Dir)
            sys.exit()

        # Check if WAV files directory exists and contains wmv or wav files
        if os.path.exists(self.WAV_Dir):
            print('Folder %s exists.. continuing processing..' %self.WAV_Dir)
        else:
            print('Trying to create folder for WAV files')
            try:
                os.mkdir(self.WAV_Dir)
            except OSError:
                print('Creation of directory %s failed' %self.WAV_Dir)
            else:
                print('Successfully created the directory %s' %self.WAV_Dir)
            print('--> Please add wav or wmv files to folder %s' %self.WAV_Dir)
            sys.exit()
    '''

    def CallingFunctions(self):
        SRT_Counter = len(glob(os.path.join(self.SRT_Dir, '*.srt')))

        if SRT_Counter == 0:
            print('!!! Please add srt_file(s) to %s-folder' %self.SRT_Dir)
            sys.exit()

        # Create directories
        WAV_Dir_Prepared = './Temp/ready_for_splitting'
        CSV_Dir_Merged = './Temp/merged_csv'
        CSV_Dir_Final = './Temp/final_csv'
        create_directories(WAV_Dir_Prepared, self.WAV_Dir_Split, CSV_Dir_Merged, CSV_Dir_Final)

        # Changing encoding from utf-8 to utf-8-sig
        print('Encoding srt_file(s) to utf-8...')
        for SRT in glob(os.path.join(self.SRT_Dir, '*.srt')):
            change_encoding(SRT)
        print('Encoding of %s-file(s) changed' %SRT_Counter)
        print('---------------------------------------------------------------------')

        # Extracting information from srt-files to csv
        print('Extracting information from srt_file(s) to csv_files')
        for File in glob(os.path.join(self.SRT_Dir, '*.srt')):
            convert_srt_to_csv(File, WAV_Dir_Prepared)
        print('%s-file(s) converted and saved as csv-files to ./csv' %SRT_Counter)
        print('---------------------------------------------------------------------')

        # Pre-process audio for folder in which wav files are stored
        pre_process_audio(self.WAV_Dir, self.WAV_SampleRate, self.WAV_Subtype, WAV_Dir_Prepared)
        print('Pre-processing of audio files is complete.')
        print('---------------------------------------------------------------------')

        # Now slice audio according to start- and end-times in csv
        print('Slicing audio according to start- and end-times of transcript_csvs...')
        split_files(WAV_Dir_Prepared, self.WAV_Dir_Split)
        WAV_Counter = len(glob(os.path.join(self.WAV_Dir_Split, '*.wav')))
        print('Slicing complete. {} files in dir {}'.format(WAV_Counter, self.WAV_Dir_Split))
        print('---------------------------------------------------------------------')

        # Now create list of filepaths and -size of dir ./split_audio
        create_DS_csv(self.WAV_Dir_Split, CSV_Dir_Merged)
        print('DS_csv with Filepaths - and sizes created.')
        print('---------------------------------------------------------------------')

        # Now join all seperate csv files
        merge_csv(WAV_Dir_Prepared, CSV_Dir_Merged)
        print('Merged csv with all transcriptions created.')
        print('---------------------------------------------------------------------')

        # Merge the csv with transcriptions and the file-csv with paths and sizes
        CSV_Name_Final = 'DS_training_final.csv'
        merge_transcripts_and_wav_files(CSV_Dir_Merged, CSV_Dir_Final, CSV_Name_Final)
        print('Final DS csv generated.')
        print('---------------------------------------------------------------------')

        # Clean the data of unwanted characters and translate numbers from int to words
        CSV_Path_Final_Cleaned = clean_unwanted_characters(CSV_Dir_Final, CSV_Name_Final)
        print('Unwanted characters cleaned.')
        print('---------------------------------------------------------------------')

        # Write transcript to text-file for model training
        Transcript_Writer(CSV_Path_Final_Cleaned, self.AutoEncoder, self.IsSpeakerMultiple, self.FileList_Path_Training)
        Transcript_Writer(CSV_Path_Final_Cleaned, self.AutoEncoder, self.IsSpeakerMultiple, self.FileList_Path_Validation)
        print('Transcript written.')
        print('---------------------------------------------------------------------')

        # Now remove the created folders
        for folders in [WAV_Dir_Prepared, CSV_Dir_Merged, CSV_Dir_Final]:
            shutil.rmtree(folders, ignore_errors = True)
        print('Temp files removed.')
        print('********************************************** FINISHED ************************************************')

        print(f'Final processed audio is in {self.WAV_Dir_Split}')

        '''
        print('******************************************* Execution Time *********************************************')
        # Evaluate the scripts execution time
        end_time = time.time()
        exec_time = str(datetime.timedelta(seconds=end_time-start_time))
        print('The script took {} to run'.format(exec_time))
        print('********************************************************************************************************')
        '''


'''
Sources:
 - Downsampling wav-files: https://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file
 - Converting to 16-bit files: https://stackoverflow.com/questions/44812553/how-to-convert-a-24-bit-wav-file-to-16-or-32-bit-files-in-python3
 - Extract audio (wav) from wmv or mp4: https://zulko.github.io/moviepy/
 - Extract audio (wav) from wmv or mp4: https://medium.com/@steadylearner/how-to-extract-audio-from-the-video-with-python-aea325f434b6
 - Dataset-split: https://stackoverflow.com/questions/38250710/how-to-split-data-into-3-sets-train-validation-and-test
Further information:
 - README.md (https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
'''