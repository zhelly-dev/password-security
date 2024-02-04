import hashlib
import random
import string

def get_random_string():
	letters = string.ascii_letters
	result_str = ''.join(random.choice(letters) for i in range(8))
	return result_str

pswd = input()
pswd_salted = pswd+get_random_string()
pswd_hashed = hashlib.md5(pswd_salted.encode())
print(f"Source: {pswd}")
print(f"Salted: {pswd_salted}")
print(f"MD5: {pswd_hashed.hexdigest()}")
