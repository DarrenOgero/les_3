def thesaurus(*names):
   l_name = [*names]
   dictionary = {}
   l_name_1 = []
   for name in l_name:
      name.capitalize()
      rob = name[0]
      dict_1 = {rob: name}
      dictionary.update(dict_1)

   return dictionary


print(thesaurus("Петр", "Паша", 'Макс'))
