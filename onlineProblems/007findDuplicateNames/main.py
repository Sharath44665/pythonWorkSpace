def find_duplicates(names):
  DuplicateNames = {}
  duplicateList = []
  for name in names:
    if name not in DuplicateNames:
      DuplicateNames[name] = 1
    else:
      DuplicateNames[name] += 1

  for key,val in DuplicateNames.items():
    if val > 1:
      duplicateList.append(key)

  # duplicate_names = []
  # unique_names = set()

  # for name in names:
  #     if name in unique_names:
  #         duplicate_names.append(name)
  #     else:
  #         unique_names.add(name)
        
  return duplicateList

names = ["Aman", "Akanksha", "Divyansha", "Devyansh", 
         "Aman", "Diksha", "Akanksha"]
print(find_duplicates(names))
