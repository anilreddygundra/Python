from CleanWhitespace import CleanWhitespace

<<<<<<< HEAD

=======
>>>>>>> 78e1c9fea98a1da94c2d2b6a3bb6e67550625a29
input_dict = {' E123      yuyu': ' QWEerer', ' Qwerty   22': ' 89RThhjj ',
              'DDf     ': {' AnIlReDdY      fdf ': 'asdfgFG2 '}}
obj = CleanWhitespace()
ret = obj.clean_whitespace(input_dict, key_strip='lower_case', value_strip='lead_and_trail')
print("Return output from calling file: {}".format(ret))
