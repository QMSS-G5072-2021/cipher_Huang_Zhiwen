def cipher(text, shift, encrypt=True):

    """
    The function allows encipher your message. 
    In short, each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text: a string of the word, sentence or paragraph to encipher
    shift: an integer of fixed number of positions down the alphabet  
    encrypt: a boolean that identify whether to encrypt or decrypt 

    Returns
    ----------
    The next text that was ciphered according to the shift of input under the Caesar cipher

    Examples
    ----------
    >>> import cipher_zh2387
    >>> cipher_zh2387.cipher("All about us", 3)
    'Doo derxw xv'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
