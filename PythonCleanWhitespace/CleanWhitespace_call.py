from CleanWhitespace import CleanWhitespace


input_dict = {' E123      yuyu': ' QWEerer', ' Qwerty   22': ' 89RThhjj ',
              'DDf     ': {' AnIlReDdY      fdf ': 'asdfgFG2 '}}
obj = CleanWhitespace()
ret = obj.clean_whitespace(input_dict, key_strip='lower_case', value_strip='lead_and_trail')
print("Return output from calling file: {}".format(ret))