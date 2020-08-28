str = 'X-DSPAM-Confidence:0.8475'

pos = str.find(':')
floatVal = str[pos+1:]
print(float(floatVal))
