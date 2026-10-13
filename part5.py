# --------- list ----------(mutable)

"""
marks = [98,99,97,93]
print(marks, type(marks))

# ---------- index ----------
print(marks[0])
print(marks[-1])

# slicing a list
list[start: end]
print(marks)
# print(marks[0:3])
# print(marks[-3 :-1])
marks.append(50)
marks.insert(0,7)

print(marks)

print (100 in marks ) #False

marks.clear()
print (marks)

"""

# -----------Tuple(immutable)-----------
marks = (98,99,97, 95,93, 95,95)
print(marks.count(95))
print(marks.index(95))

# ----------set-------

marks1 = {98, 97, 94,94, 95} # only uniqe value
print(len(marks1), marks1) # 4 {97,98,94,95}

for score in marks:
    print(score)

# Dictionary {key => val}

marks = {'Math': 99, "p": 97}
print(marks['p'])