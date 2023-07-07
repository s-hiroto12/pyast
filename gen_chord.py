import markovify
with open('data/all_progressions') as file:
  text = file.read()
print(text)
text_model = markovify.Text(text)

length = 100
for i in range(10):
  print("generated chord progression", i+1)
  print(text_model.make_short_sentence(length))
  print()
