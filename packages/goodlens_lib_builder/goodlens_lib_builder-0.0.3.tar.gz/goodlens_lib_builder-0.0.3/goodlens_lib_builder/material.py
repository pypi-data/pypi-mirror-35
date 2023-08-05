import re

class Material():
  def __init__(self):
    super().__init__()

  def validateText(self, text):
    # s = text.replace(" ", "")
    # s = re.sub('[\[{]', '(', s)
    # s = re.sub('[\]}]', ')', s)

    if validateBracketPair(text, '[', ']') == False:
      return False

    if validateBracketPair(text, '{', '}') == False:
      return False

    if validateBracketPair(text, '(', ')') == False:
      return False

    return True

def validateBracketPair(text, open, close):
  o = (text.count(open))
  c = (text.count(close))
  if (o != c):
    return False
  return True

