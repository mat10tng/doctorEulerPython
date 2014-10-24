def char_position(letter):
	return ord(letter)-96
def pos_to_char(pos):
    return chr(pos) + 97
def word_value(word):
	sm = 0
	for char in word:
		sm+= char_position(char)
	return sm