import os


def create_directories(
    wav_dir_prepared,
    wav_dir_split,
    csv_dir_merged,
    csv_dir_final
):
    '''
    Create csv directory
    '''
    if not os.path.exists(wav_dir_prepared):
        try:
            os.makedirs(wav_dir_prepared, exist_ok = True)
        except OSError:
            print('Creation of directory %s failed' %wav_dir_prepared)

    if not os.path.exists(wav_dir_split):
        try:
            os.makedirs(wav_dir_split, exist_ok = True)
        except OSError:
            print('Creation of directory %s failed' %wav_dir_split)

    if not os.path.exists(csv_dir_merged):
        try:
            os.makedirs(csv_dir_merged, exist_ok = True)
        except OSError:
            print('Creation of directory %s failed' %csv_dir_merged)

    if not os.path.exists(csv_dir_final):
        try:
            os.makedirs(csv_dir_final, exist_ok = True)
        except OSError:
            print('Creation of directory %s failed' %csv_dir_final)
