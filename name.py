inputString = '3702130'
MagicNumber = inputString[0]
Payload = inputString[1:]
Payload = Payload[::-1]
alphabet = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
OutputString = ''
while len(Payload)>0:
  CurrentSum = ''
  if (len(Payload)==1):
    CurrentSum = Payload[0]
  else:
    CurrentSum = Payload[0:2]
  ElementIndex = int(CurrentSum) - int(MagicNumber)
  ElementChar = alphabet[ElementIndex]
  OutputString += ElementChar
  Payload = Payload.replace(CurrentSum,'')
print OutputString.capitalize()
