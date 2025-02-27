
#Task 1: Power of 5

def Find(n):
    if n<=0:
        return
    while n%5==0:
        n//=5
    return n==1
    
print(Find(15625))
print(Find(526))

#Task 2: Find the K-th Character



def generate_word(word, k):
    if len(word) >= k:
        return word
    new_part = "".join(chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in word)
    return generate_word(word + new_part, k)

def find_kth_character(k):
    word = generate_word("a", k)
    return word[k - 1]

print(find_kth_character(5))  
print(find_kth_character(10)) 
