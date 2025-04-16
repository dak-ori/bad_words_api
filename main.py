import re

ban_words = ["바보", "멍청이", "죽어"]

def filter_text(text, ban_words):
    pattern = "|".join(ban_words)  
    return re.sub(pattern, "***", text)

user_input = "이 바보 멍청이 죽어"
filtered_text = filter_text(user_input, ban_words)

print(filtered_text) 
# "이 *** *** ***"