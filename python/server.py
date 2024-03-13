import serial
from functions.audioControll import increaseVolume, decreaseVolume, mute, unmute, getAllAudioData, getAudioDataForChannel

print('')
print('------------------------')
print('Starting server')
print('------------------------')
print('')

com = 'COM9'
baud = 9600

print('Connecting to', com, 'at', baud, 'baud...')
print('')
ser = serial.Serial(com, baud)

channels = ['game', 'chatRender', 'chatCapture', 'media', 'aux']


try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)
            
            # --------------------------------   
            # Increase volume of channel
            # --------------------------------
            
            if 'increaseVolume' in line:
                
                if 'game' in line:
                    increaseVolume('game')
                elif 'chatRender' in line:
                    increaseVolume('chatRender')
                elif 'chatCapture' in line:
                    increaseVolume('chatCapture')
                elif 'media' in line:
                    increaseVolume('media')
                elif 'aux' in line:
                    increaseVolume('aux')
                else:
                    print('Channel not recognized')
                    
            # --------------------------------   
            # Decrease volume of channel
            # --------------------------------
            
            elif 'decreaseVolume' in line:
                
                if 'game' in line:
                    decreaseVolume('game')
                elif 'chatRender' in line:
                    decreaseVolume('chatRender')
                elif 'chatCapture' in line:
                    decreaseVolume('chatCapture')
                elif 'media' in line:
                    decreaseVolume('media')
                elif 'aux' in line:
                    decreaseVolume('aux')
                else:
                    print('Channel not recognized')
                    
            # --------------------------------   
            # Mute a channel
            # --------------------------------
                
            elif 'mute' in line:
                
                if 'game' in line:
                    mute('game')
                elif 'chatRender' in line:
                    mute('chatRender')
                elif 'chatCapture' in line:
                    mute('chatCapture')
                elif 'media' in line:
                    mute('media')
                elif 'aux' in line:
                    mute('aux')
                else:
                    print('Channel not recognized')
                
            # --------------------------------   
            # Unmute a channel
            # --------------------------------
            
            elif 'unmute' in line:
                
                if 'game' in line:
                    unmute('game')
                elif 'chatRender' in line:
                    unmute('chatRender')
                elif 'chatCapture' in line:
                    unmute('chatCapture')
                elif 'media' in line:
                    unmute('media')
                elif 'aux' in line:
                    unmute('aux')
                else:
                    print('Channel not recognized')
                    
            # --------------------------------   
            # Gets and exit + unrecognized commands
            # --------------------------------
                    
            elif 'getAllAudioData' in line:
                print(getAllAudioData())
            elif 'getAudioDataForChannel' in line:
                print(getAudioDataForChannel('game'))
            elif 'exit' in line:
                break
            elif 'test' in line:
                print('Test command recognized')
            else:
                print('Command not recognized')
finally:
    ser.close()