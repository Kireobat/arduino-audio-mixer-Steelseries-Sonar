from steelseries_sonar_py import Sonar
from steelseries_sonar_py.exceptions import EnginePathNotFoundError

try:
    sonar = Sonar(streamer_mode=False, app_data_path="C:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json")
except EnginePathNotFoundError:
    print("Engine not found!")
    quit()
    


def increaseVolume(channel):
    print('Increasing volume of channel', channel)
    # Increase volume of channel
    
    
    
def decreaseVolume(channel):
    print('Decreasing volume of channel', channel)
    # Decreasing volume of channel
    
def mute(channel):
    print('Muting channel', channel)
    # Mute channel
    
def unmute(channel):
    print('Unmuting channel', channel)
    # Unmute channel
    
def getAllAudioData():
    print('Checking volume of all channels')
    # Check volume of channel
    volumeData = sonar.get_volume_data()
    
    volumeData
    
def getAudioDataForChannel(channel):
    print('Checking volume of channel', channel)
    # Check volume of channel
    volumeData = sonar.get_volume_data()
    
    print(volumeData['devices'][channel])
    
getAudioDataForChannel('game')