from .utils.Install_FFmpeg import Execute_FFmpeg_Installation


class Env_Configurator:
    '''
    Confige the user environment
    '''
    def FFmpeg_Installer():
        if Execute_FFmpeg_Installation() == False:
            print("Failed to install Static FFmpeg.")