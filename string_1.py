#CodingBat Python practice problems
# String-1

#String-1 > hello_name
def hello_name(name):
    return "Hello " + name + "!"
#alternative
def hello_name(name):
    return "Hello %n!"%(name)

#String-1 > make_abba
def make_abba(a, b):
    return (a + 2 * b + a)

#String-1 > make_tags
def make_tags(tag, word):
    return '<%s>%s</%s>'%(tag, word, tag)
#more simple alternative
def make_tags(tag, word):
    return ("<" + tag + ">") + word + ("</" + tag + ">")

#String-1 > make_out_word
def make_out_word(out, word):
    return '%s%s%s'%(out[:2], word, out[2:])
#or
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#String-1 > extra_end
def extra_end(str):
    return 3 * str[-2:]

#String-1 > first_two
def first_two(str):
    return str[:2]

#String-1 > first_half
def first_half(str):
    return str[:len(str) // 2]

#String-1 > without_end
def without_end(str):
    n = len(str)
    if n >= 2:
        return str[1:-1]
    else: return str
#or
def without_end(str):
    return str[1:-1]
#or
def without_end(str):
  return str[1:len(str)-1]

#String-1 > combo_string
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else: return a + b + a

#String-1 > non_start
def non_start(a, b):
    return a[1:] + b [1:]

#String-1 > left2
def left2(str):
    return str[2:] + str [:2]
