def generate_text(seed_text, next_words, model, max_sequence_len):
  for _ in range(next_words):
  token_list = tokenizer.texts_to_sequences([seed_text])[0]
  token_list = pad_sequences([token_list], maxlen=max_sequence_len-1,  padding=’pre’)
  predicted = model.predict_classes(token_list, verbose=0)
 
  output_word = “”
  for word,index in tokenizer.word_index.items():
  if index == predicted:
  output_word = word
  break
  seed_text += “ “+output_word
  return seed_text.title()
  