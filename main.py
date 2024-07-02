# Based on 'Hatsuon' by Duncan Bay (https://github.com/DJTB/hatsuon), written for Python by ccos

from utils import getMoraCount, getPitchPatternName, makePitchPattern

# Main function which returns object containing pitch accent info

def hatsuon(reading, pitch_num):
    morae = getMoraCount(reading)
    try:
        return {
            'Reading': reading,
            'Morae': morae,
            'Pitch Number': pitch_num,
            'Pitch Pattern': getPitchPatternName(morae, pitch_num),
            'Pitch Array': makePitchPattern(morae, pitch_num)
        }
    except Exception as e:
        print(f'An error has occurred: {e}')
