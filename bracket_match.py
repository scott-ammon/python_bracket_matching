class Stack:
  def __init__(self):
    self.store = []
  
  def push(self, element):
    self.store.append(element)
    return self

  def pop(self):
    return self.store.pop()

  def is_empty(self):
    return self.size() == 0
  
  def size(self):
    return len(self.store)

# Determine if character is a bracket
def is_bracket(char):
  is_bracket = False
  brackets = ['(',')','{','}','[',']']
  for bracket in brackets:
    if (char == bracket):
      is_bracket = True
  return is_bracket

# Determine if character is open bracket
def is_open_bracket(char):
  is_open_bracket = False
  open_brackets = ['(','{','[']
  for bracket in open_brackets:
    if (char == bracket):
      is_open_bracket = True
  return is_open_bracket

# Determine if a matching open/close pair of brackets
def is_a_pair(open_bracket, close_bracket):
  brackets = ['()','{}','[]']
  match = False
  for char in brackets:
    if(open_bracket == char[0]):
      if(close_bracket == char[1]):
        match = True
  return match

# Main function that calls bracket functions and stack
def bracket_match(input_string):
  chars = list(input_string)
  char_stack = Stack()

  for char in chars:
    # is the character a bracket?
    if (is_bracket(char)):
      # if so, is it an open bracket?
      if (is_open_bracket(char)):
        # add open bracket to the stack
        char_stack.push(char)
      else:
        # you have a closed bracket but no open...
        if (char_stack.size() == 0):
          return False
        else:
          # get the open bracket off top of stack
          open_bracket = char_stack.pop()
          # compare the closed bracket to open bracket from stack
          if(not is_a_pair(open_bracket, char)):
            return False
  
  return False if(char_stack.size() > 0) else True

# Test cases should return:

# True
print(bracket_match('abc(123)'))

# False
print(bracket_match('abc(123'))

# True
print(bracket_match('a[bc(123)]'))

# False
print(bracket_match('a[bc(12]3)'))

# True
print(bracket_match('a{b}{c(1[2]3)}'))

# False
print(bracket_match('a{b}{c(1}[2]3)'))

# True
print(bracket_match('()'))

# False
print(bracket_match('[]]'))

# True
print(bracket_match('abc123yay'))