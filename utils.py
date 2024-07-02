# Based on 'Hatsuon' by Duncan Bay (https://github.com/DJTB/hatsuon), written for Python by ccos


#Checks if character is a diagraph

def isDiagraph(kana):
    hira_diagraphs = ['ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'ゃ', 'ゅ', 'ょ', 'ゎ', 'ゕ', 'ゖ']
    kata_diagraphs = ['ァ', 'ィ', 'ゥ', 'ェ', 'ォ', 'ャ', 'ュ', 'ョ', 'ヮ', 'ヵ', 'ヶ']
    if kana in hira_diagraphs:
        return True
    elif kana in kata_diagraphs:
        return True
    else:
        return False
    
#Slices characters into list

def sliceReading(reading):
    sliced_reading = []
    for character in reading:
        sliced_reading.append(character)
    return sliced_reading

#Combines diagraphs into joint string to find accurate morae
# i.e. [か, し, ゅ, う] => [か, しゅ, う]

def getMorae(reading):
    mora_reading = sliceReading(reading)
    i = 0
    while i < len(mora_reading):
        if isDiagraph(mora_reading[i]):
            if i > 0:
                mora_reading[i-1] = mora_reading[i-1] + mora_reading[i]
                del mora_reading[i]
            else:
                i += 1
        else:
            i += 1
    return mora_reading

# Returns mora count of reading

def getMoraCount(mora_reading):
    correct_mora = getMorae(mora_reading)
    mora_count = len(correct_mora)
    return mora_count

# Return of pitch accent pattern

def getPitchPatternName(mora_count, pitch_num, locale='EN'):
    if pitch_num == 0:
        pitch_pattern_name = 'Heiban'
    elif pitch_num == 1:
        pitch_pattern_name = 'Atamadaka'
    elif pitch_num > 1 and pitch_num < mora_count:
        pitch_pattern_name = 'Nakadaka'
    elif pitch_num > 1 and pitch_num == mora_count:
        pitch_pattern_name = 'Odaka'

    return pitch_pattern_name

 # Creates an Heiban pitch pattern
 # initial low -> rest high, particle high
 # [0, 1, 1, 1, 1, 1]

def makeHeibanArray(mora_count):
    pitch_array = [0]
    for i in range(mora_count):
        pitch_array.append(1)
    return pitch_array

# Creates an Atamadaka pitch pattern
# initial high -> rest low, particle low
# [1, 0, 0, 0, 0, 0]

def makeAtamadakaArray(mora_count):
    pitch_array = [1]
    for i in range(mora_count):
        pitch_array.append(0)
    return pitch_array

def makeOdakaArray(mora_count):
    pitch_array = [0]
    for i in range(mora_count-1):
        pitch_array.append(1)
    pitch_array.append(0)
    return pitch_array

def makeNakadakaArray(mora_count, pitch_num):
    pitch_array = [0]
    for i in range(0, pitch_num-1):
        pitch_array.append(1)
    for i in range(pitch_num, mora_count):
        pitch_array.append(0)
    pitch_array.append(0)
    return pitch_array
        
# Create relevant pitch pattern from mora count and number

def makePitchPattern(mora_count, pitch_num):
    pitch_pattern_name = getPitchPatternName(mora_count, pitch_num)
    if pitch_pattern_name == 'Heiban':
        return makeHeibanArray(mora_count)
    elif pitch_pattern_name == 'Atamadaka':
        return makeAtamadakaArray(mora_count)
    elif pitch_pattern_name == 'Odaka':
        return makeOdakaArray(mora_count)
    elif pitch_pattern_name == 'Nakadaka':
        return makeNakadakaArray(mora_count, pitch_num)
    