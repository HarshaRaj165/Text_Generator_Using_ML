def create_model(max_sequence_len, total_words):
  input_len = max_sequence_len — 1
  model = Sequential()
 
  # Add Input Embedding Layer
  model.add(Embedding(total_words, 10, input_length=input_len))
 
  # Add Hidden Layer 1 — LSTM Layer
  model.add(LSTM(100))
  model.add(Dropout(0.1))
 
  # Add Output Layer
  model.add(Dense(total_words, activation=’softmax’))
  model.compile(loss=’categorical_crossentropy’, optimizer=’adam’)
 
  return model
model = create_model(max_sequence_len, total_words)
model.fit(predictors, label, epochs=20, verbose=5)
