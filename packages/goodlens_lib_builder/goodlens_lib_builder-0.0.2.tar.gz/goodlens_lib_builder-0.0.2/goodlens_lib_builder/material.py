import re

class Material():
  def __init__(self):
    super().__init__()

  def validateText(self, text):
    s = text.replace(" ", "")
    s = re.sub('[\[{]', '(', s)
    s = re.sub('[\]}]', ')', s)

    l = (s.count('('))
    r = (s.count(')'))

    print(s)

    if (l != r):
      return False

    return True

