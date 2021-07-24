def num_translate(num):
     nums = {
         'one': 'один',
         'two': 'два',
         'three': 'три',
         'four': 'четыре',
         'five': 'пять',
         'six': 'шесть',
         'seven': 'семь',
         'eight': 'восемь',
         'nine': 'девять',
         'ten': 'десять'
    }
     el_num = nums[num]
     return el_num

print(num_translate('two'))
