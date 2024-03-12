from steelseries_sonar_py import Sonar
from steelseries_sonar_py.exceptions import EnginePathNotFoundError

try:
    sonar = Sonar(streamer_mode=False, app_data_path="C:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json")
except EnginePathNotFoundError:
    print("Engine not found!")
    quit()
    
    
channels = ['game', 'chatRender', 'chatCapture', 'media', 'aux']


def increaseVolume(channel):
    print('Increasing volume of channel', channel)
    # Increase volume of channel
    audioData = getAudioDataForChannel(channel)['classic']
    
    if audioData['volume'] >= 1:
        print('Volume is already at maximum')
        return
    
    sonar.set_volume(channel, audioData['volume'] + 0.01)

    
    
def decreaseVolume(channel):
    print('Decreasing volume of channel', channel)
    # Decreasing volume of channel
    
    audioData = getAudioDataForChannel(channel)['classic']
    
    if audioData['volume'] <= 0:
        print('Volume is already at minimum')
        return
    
    sonar.set_volume(channel, audioData['volume'] - 0.01)
    
def mute(channel):
    print('Muting channel', channel)
    # Mute channel
    
    audioData = getAudioDataForChannel(channel)['classic']
    
    if audioData['muted'] == True:
        print('Channel is already muted')
        return
    
    sonar.mute_channel(channel, True)
    
def unmute(channel):
    print('Unmuting channel', channel)
    # Unmute channel
    
    audioData = getAudioDataForChannel(channel)['classic']
    
    if audioData['muted'] == False:
        print('Channel is already unmuted')
        return
    
    sonar.mute_channel(channel, False)
    
def getAllAudioData():
    print('Checking volume of all channels')
    # Check volume of channel
    volumeData = sonar.get_volume_data()
    
    return volumeData
    
def getAudioDataForChannel(channel):
    print('Checking volume of channel', channel)
    # Check volume of channel
    volumeData = sonar.get_volume_data()
    
    return volumeData['devices'][channel]

# increaseVolume('game')

print(getAllAudioData())