tokenizer = Tokenizer()
def get_sequence_of_tokens(corpus):
  #get tokens
  tokenizer.fit_on_texts(corpus)
  total_words = len(tokenizer.word_index) + 1
 
  #convert to sequence of tokens
  input_sequences = []
  for line in corpus:
  token_list = tokenizer.texts_to_sequences([line])[0]
  for i in range(1, len(token_list)):
  n_gram_sequence = token_list[:i+1]
  input_sequences.append(n_gram_sequence)
 
  return input_sequences, total_words
inp_sequences, total_words = get_sequence_of_tokens(corpus)