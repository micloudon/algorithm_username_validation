# user name validation algorithm
# user name must be between 4-25 characters
# first character must be a letter
# last character cannot be an underscore
# letters, numbers and underscore are the only acceptable characters

def UsernameVal(strParam):

  if len(strParam) < 4:
    return False

  if len(strParam) > 25:
    return False
  
  if strParam[0].isalpha() != True:
    return False
  
  if strParam[-1] == "_":
    return False

  for i in strParam:
    if not i.isalnum() and i != "_":
      return False

  return True
      
    
print(UsernameVal("test_case_123"))