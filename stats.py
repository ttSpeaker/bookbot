def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    for c in text.lower():
        chars[c] = chars.get(c, 0) + 1
    return chars

def sort_on(dict):
    return dict["char"]
    

def char_count_builder(chars_object):
    chars = []
    for c in chars_object:
        chars.append({
            'char': c[0],
            'count': c[1]
        })
    chars.sort(key=sort_on, reverse=False)
    return chars
    
    
