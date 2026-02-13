def decode(func):
   def wrapper(message):
      cleaned_str = func(message)
      sorted_str = sorted(cleaned_str, key=lambda x: x)
      return ''.join([str(9-int(x)) for x in sorted_str])
   return wrapper

@decode
def clean_message(message):
   return ''.join([x for x in message if x.isdigit()])

if __name__ == "__main__":
    print(clean_message("'`-hjefh83 njdf83 232'"))
