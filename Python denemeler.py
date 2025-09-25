# # ad = input("Adınızı giriniz: ")
# # yas = int(input("Yaşınızı giriniz: "))
# # dogum_yili = 2025 - yas
# # print(f"Merhaba {ad}, doğum yılınız {dogum_yili}.")
# from itertools import count
# from os import remove
# from urllib.response import addbase
# from dis import name
# from tkinter.font import names
from locale import windows_locale
# import password

# isim = "Agus"
# print(isim)

# sayi1 = 8
# sayi2 = 3
# toplam = sayi1 + sayi2
# print("toplam:", toplam)
# fark = sayi1 - sayi2
# print("fark:", fark)
# carpim = sayi1 * sayi2
# print("carpim:", carpim)
# bolum = sayi1 / sayi2
# print("bolum:", bolum)
# mod = sayi1 % sayi2
# print("mod:", mod)

# #first_number = input(Enter first number: ")
# #second_number = input("Enter second number: ")
# #product = int(first_number) * int(second_number)
# #print("Product: " + str(product))


# mini_task = "1D"
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# country = input("Enter your country: ")
# print(firstname + " " + lastname + " is from " + country)

# mini_task = "1E"
# language = input("Enter your favorite programming language: ")
# print(language + " is a great programming language!")

# mini_task = "1F"
# age = input("Enter your age: ")
# age = int(age)
# print(type(age))

# mini_task = "2A"
# a = 10
# b = 5
# print(int(a) - int(b))
# print(int(a) / int(b))


# mini_task = "2B"
# a = 10
# b = 5
# print(int(a) // int(b))
# print(int(a) % int(b))

# mini_task = "2C"
# x = 16
# print(x ** 2)
# print(x ** 0.5)

# mini_task = "2D"
# x = 10
# y = 3
# z = 5
# print(x + y * z)
# print((x + y) * z)
# print(x + (y * z))

# mini_task = "2E"
# n = -5
# print(abs(n))

# mini_task = "4A"
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(input("This is an even number."))
# else:
#     print(input("This is an odd number."))

# mini_task = "4B"
# number = int(input("Enter a number: "))
# if number > 0:
#     print("This is a positive number.")
# elif number < 0:
#     print("This is a negative number.")
# else:
#     print("You entered zero.")

# mini_task = "4C"
# score = int(input("Enter your score between 0 and 100: "))
# if 90 <= score <= 100:
#     print("Your grade is Excellent.")
# elif 75 <= score < 90:
#     print("Your grade is Good.")
# elif 50 <= score < 75:
#     print("Your grade is Pass.")
# elif 0 <= score < 50:
#     print("Your grade is Fail.")


# mini_task = "5A"
# for number in range(1, 10):
#     print(number)

# mini_task = "5B"
# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

# mini_task = "5C"
# numbers = range (1, 100)
# for number in numbers:
#     print(sum(numbers))

# mini_task = "6A"
# fruits = ["apple", "banana", "cherry", "date", "strawberry"]
# for fruit in fruits:
#     print(fruit)

# mini_task = "6B"
# fruits = ["apple", "banana", "cherry", "date", "strawberry"]
# for fruit in fruits:
#     print(fruit[0])
#     print(fruit[-1])


# mini_task = "6C"
# fruits = ["apple", "banana", "cherry", "date", "strawberry"]
# fruits.append("fig")
# fruits.remove("banana")
# print(fruits)

# mini_task = "7A"
# def greet():
#     print("Hello Agus!")
#     print("Welcome to the program Agus.")
#     print("Enjoy your stay!")
# greet()


# mini_task = "7B"
# def greet_person(name):
#     print(f"Hello, {name}!")
#     print("Welcome to the program.")
#     print("Enjoy your stay!")
# greet_person("Alice")


# mini_task = "7C"
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5,3)
# print(result)


# mini_task = "7D"
# def describe_person(name, age, country):
#     name = input("Enter your name: ")
#     age = int(input("Enter age: "))
#     country = input("Enter country: ")
#     print(f"{name} is {age} years old and lives in {country}.")

# mini_task = "7E"
# def greet_user(name="Guest"):
#     print(f"Hello, {name}!")
#     print("Welcome to the program.")
#     print("Enjoy your stay!")
# greet_user()
# greet_user("Alice")

# mini_task = "7F"
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# mini_task = "8A.1"
# number = int(input("Enter a number: "))
# print(number)
# if number > 0:
#     print("This is a positive number.")
# elif number < 0:
#     print("This is a negative number.")
# else:
#     print("You entered zero.")


# mini_task = "8A.1"
# num = int(input("Enter a number: "))
# def check_sign(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"
# result = check_sign(num)
# print(f"The number is {result}.")



# mini_task = "8A.2"
# num = int(input("Enter a number: "))
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# result = is_even(num)
# if result:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")


# mini_task = "8A.3"
# num = int(input("Enter your score: "))
# def grade(score):
#     if 90 <= score <= 100:
#         return "Excellent"
#     elif 75 <= score < 90:
#         return "Good"
#     elif 50 <= score < 75:
#         return "Pass"
#     elif 0 <= score < 50:
#         return "Fail"
#     else:
#         return "Invalid score"
# result = grade(num)
# print(f"Your grade is {result}.")


# mini_task = "8B.1"
# age = int(input("Enter your age: "))
# def is_teenager(age):
#     if 13 <= age <= 19:
#         return True
#     else:
#         return False
# result = is_teenager(age)
# if result:
#     print("You are a teenager.")
# else:
#     print("You are not a teenager.")


# mini_task = "8B.2"
# age = int(input("Enter your age: "))
# def can_vote_and_drive (age):
#     if age >= 18:
#         return True
#     else:
#         return False
# result = can_vote_and_drive(age)
# if result:
#     print("You are eligible to vote and drive.")
# else:
#     print("You are not eligible to vote and drive.")
# age = int(input("Enter your age: "))
# def can_vote_only(age):
#     if age >= 16 >= 17:
#         return True
#     else:
#         return False
# result = can_vote_only(age)
# if result:
#     print("You are eligible to only vote.")
# else:
#     print("You are not eligible to vote.")
# age = int(input("Enter your age: "))
# def Too_young_to_vote_and_drive(age):
#     if age < 16:
#         return True
#     else:
#         return False
# result = Too_young_to_vote_and_drive(age)
# if result:
#     print("You are too young to vote and drive.")
# else:
#     print("You are eligible to vote and drive.")
#
# # mini_task = "8B.3"
# pass



# mini_task = "8B.2"
# age = int(input("Enter your age: "))
# def can_vote_and_drive(age):
#     if age >= 16:
#         if age >= 18:
#             return "Can vote and drive"
#         else:
#             return "Can vote only"
#     else:
#         return "Too young"
# result = can_vote_and_drive(age)
# print(result)


# input(str("Please enter your password: "))
# password = numbers
# def is_valid_password(password):
#     return len(password) >= 8 and "pass" in password
# result = is_valid_password(password)
# if result:
#     print("Valid password.")
# else:
#     print("Invalid password. Password must be at least 8 characters long and contain the word 'pass'.")


# mini_task = "9A.1"
# def greet_user(name):
#     return f"Hello, {name.capitalize()}!"
#
# user_name = input("Enter your name: ")
# greeting = greet_user(user_name)
# print(greeting)


# mini_task = "9A.2"
# def count_vowels_and_consonants(text):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     consonant_count = 0
#     for char in text:
#         if char.isalpha():
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1
#     return vowel_count, consonant_count
# user_text = input("Enter a string: ")
# vowels, consonants = count_vowels_and_consonants(user_text)
# print(f"Vowels: {vowels}, Consonants: {consonants}")

# mini_task = "9A.3"
# def reverse_string(text):
#     return text[::-1]
# user_text = input("Enter a string: ")
# reversed_text = reverse_string(user_text)
# print(f"Reversed string: {reversed_text}")

# Project 1
# def calculator():
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#         return
#     operation = input("Enter operation (+, -, *, /): ")
#     if operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     elif operation == "*":
#         result = num1 * num2
#     elif operation == "/":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             print("Error: Division by zero.")
#             return
#     else:
#         print("Invalid operation. Please enter one of +, -, *, /.")
#         return
#     print(f"The result is: {result}")
# calculator()

# Project 2
# def password_strength_checker(password):
#     if len(password) < 8:
#         return "Weak"
#     elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
#         return "Strong"
#     else:
#         return "Moderate"
# user_password1 = input("Enter your password: ")
# strength = password_strength_checker(user_password1)
# print(f"Password strength: {strength}")


# Project 3
# import random
# def number_guessing_game():
#     number_to_guess = random.randint(1,100)
#     attempts = 0
#     print("Welcome to the Number Guessing Game!")
#     while True:
#         try:
#             user_guess = int(input("Guess a number between 1 and 100: "))
#             attempts += 1
#             if user_guess < 1 or user_guess > 100:
#                 print("Please guess a number within the range.")
#             elif user_guess < number_to_guess:
#                 print("Too low!")
#             elif user_guess > number_to_guess:
#                 print("Too high!")
#             else:
#                 print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")
# number_guessing_game()



# Project 4
# def to_do_list_manager():
#     todo_list = []
#     while True:
#         action = input("Choose an action: add, remove, view, exit: ").lower()
#         if action == "add":
#             task = input("Enter a task to add: ")
#             todo_list.append(task)
#             print(f"Task '{task}' added.")
#         elif action == "remove":
#             task = input("Enter a task to remove: ")
#             if task in todo_list:
#                 todo_list.remove(task)
#                 print(f"Task '{task}' removed.")
#             else:
#                 print(f"Task '{task}' not found in the list.")
#         elif action == "view":
#             if todo_list:
#                 print("Your To-Do List:")
#                 for idx, task in enumerate(todo_list, start=1):
#                     print(f"{idx}. {task}")
#             else:
#                 print("Your To-Do List is empty.")
#         elif action == "exit":
#             print("Exiting To-Do List Manager. Goodbye!")
#             break
#         else:
#             print("Invalid action. Please choose from add, remove, view, exit.")
# to_do_list_manager()


# Project 5
# def temperature_converter():
#     try:
#         temp_celsius = float(input("Enter temperature in Celsius: "))
#         temp_fahrenheit = ((temp_celsius * 9/5) + 32)
#         temp_kelvin = (temp_celsius + 273.15)
#         print(f"Temperature in Fahrenheit: {temp_fahrenheit:.2f} °F")
#         print(f"Temperature in Kelvin: {temp_kelvin:.2f} K")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")
# temperature_converter()

# def life_in_weeks(age):
#     years_left = 90 - age
#     weeks_left = years_left * 52
#     print(f"You have {weeks_left} weeks left.")
#
# # Call the function with a hard-coded age value
# life_in_weeks(25)


# def calculate_love_score(name1, name2):
#     # Combine names and make lowercase
#     combined_names = (name1 + name2).lower()
#
#     # Count for TRUE
#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e = combined_names.count("e")
#     true_score = t + r + u + e
#
#     # Count for LOVE
#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e = combined_names.count("e")  # E appears again here
#     love_score = l + o + v + e
#
#     # Combine into two-digit number
#     final_score = int(str(true_score) + str(love_score))
#
#     print(f"Love Score = {final_score}")
#     return final_score
#
#
# # Test with example
# calculate_love_score("Kanye West", "Kim Kardashian")


# import string
# def word_frequency_counter():
#     text = input("Enter a paragraph: ")
#     for char in string.punctuation:
#         text = text.replace(char, "")
#         text = text.lower()
#         words = text.split()
#         freq = {}
#         for word in words:
#             freq[word] = freq.get(word, 0) + 1
#             sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#             print("Top 5 most frequent words:")
#             for word, count in sorted_words[:5]:
#                 print(f"{word}: {count}")
# word_frequency_counter()


# def contact_book():
#     contacts = {}
#     while True:
#         action = input("Choose an action: add, remove, view, exit: ").lower()
#         if action == "add":
#             name = input("Enter contact name: ")
#             phone = input("Enter contact phone number: ")
#             contacts[name] = phone
#             print(f"Contact '{name}' added.")
#         elif action == "remove":
#             name = input("Enter contact name to remove: ")
#             if name in contacts:
#                 del contacts[name]
#                 print(f"Contact '{name}' removed.")
#             else:
#                 print(f"Contact '{name}' not found.")
#         elif action == "view":
#             if contacts:
#                 print("Contacts:")
#                 for name, phone in contacts.items():
#                     print(f"{name}: {phone}")
#             else:
#                 print("No contacts found.")
#         elif action == "exit":
#             print("Exiting Contact Book. Goodbye!")
#             break
#         else:
#             print("Invalid action. Please choose from add, remove, view, exit.")
# contact_book()



# import random
# def generate_random_ip():
#     return f"192.168.1.{random.randint(1, 254)}"
# def check_firewall_rules(ip, rules):
#     for rule_ip, action in rules.items():
#         if ip == rule_ip:
#             return action
#     return "ALLOW"
#
# def main():
#     firewall_rules = {
#         "192.168.100.1": "BLOCK",
#         "192.168.100.4": "BLOCK",
#         "192.168.100.13": "BLOCK",
#         "192.168.100.16": "BLOCK",
#         "192.168.100.19": "BLOCK",
#     }
#     for _ in range(12):
#         ip_address = generate_random_ip()
#         action = check_firewall_rules(ip_address, firewall_rules)
#         random_number = random.randint(0, 9999)
#         print(f"IP: {ip_address} - Action: {action} - Random Number: {random_number}")
# if __name__ == "__main__":
#     main()


# import os
# import sys
# import time
# from collections import defaultdict
# from scapy.all import sniff, IP
#
# THRESHOLD = 40
# print(f"THRESHOLD: {THRESHOLD}")
#
#
# def packet_callback(packet):
#     src_ip = packet[IP].src
#     packet_count[src_ip] += 1
#
#     current_time = time.time()
#     time_interval = current_time - start_time[0]
#
#     if time_interval >= 1:
#         for ip, count in packet_count.items():
#             packet_rate = count / time_interval
#             # print(f"IP: {ip}, Packet rate: {packet_rate}")
#             if packet_rate > THRESHOLD and ip not in blocked_ips:
#                 print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
#                 os.system(f"iptables -A INPUT -s {ip} -j DROP")
#                 blocked_ips.add(ip)
#
#         packet_count.clear()
#         start_time[0] = current_time
#
#
# if __name__ == "__main__":
#     if os.geteuid() != 0:
#         print("This script requires root privileges.")
#         sys.exit(1)
#
#     packet_count = defaultdict(int)
#     start_time = [time.time()]
#     blocked_ips = set()
#
#     print("Monitoring network traffic...")
#     sniff(filter="ip", prn=packet_callback)


# import socket
#
#
# def port_scanner(ip_address, start_port, end_port):
#     """
#     Scans a range of ports on a specified IP address.
#
#     Args:
#         ip_address (str): The IP address to scan.
#         start_port (int): The starting port for the scan.
#         end_port (int): The ending port for the scan.
#     """
#     print(f"Target IP address: {ip_address}")
#
#     # Loop through the port range
#     for port in range(start_port, end_port + 1):
#         # Create a socket object for each port
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#         # Set a timeout of 0.5 seconds for the connection attempt
#         s.settimeout(0.5)
#
#         # Attempt to connect to the port
#         result = s.connect_ex((ip_address, port))
#
#         # If the connection is successful, the port is open
#         if result == 0:
#             print(f"Port {port} is open.")
#
#         s.close()
#
#
# if __name__ == "__main__":
#     target_ip = "192.168.100.79"  # Your own computer (localhost)
#     start_p = 1
#     end_p = 100
#
#     port_scanner(target_ip, start_p, end_p)



# import requests
#
# def sql_injection_scanner(url):
#     """
#     Scans a given URL for basic SQL Injection vulnerabilities.
#
#     Args:
#         url (str): The URL to test.
#     """
#     # List of common SQL Injection payloads
#     payloads = ["' or 1=1--", "' or 1=1#", "' or 'a'='a'", "')", '")']
#
#     found_vulnerability = False
#
#     for payload in payloads:
#         # Append the payload to the URL
#         test_url = f"{url}{payload}"
#         print(f"Attempting with payload: {test_url}")
#
#         try:
#             # Send a GET request
#             response = requests.get(test_url, timeout=5)
#
#             # Search for common error messages in the response
#             if "SQL syntax" in response.text or "error" in response.text or "Warning" in response.text:
#                 print(f"\n[!!!] Potential Vulnerability Found! Test URL: {test_url}")
#                 found_vulnerability = True
#                 break
#         except requests.exceptions.RequestException as e:
#             print(f"Connection error: {e}")
#             break
#
#     if not found_vulnerability:
#         print("\n[OK] No vulnerabilities found.")
#
#
# if __name__ == "__main__":
#     # Use your own test server instead of a real website
#     target_url = "https://zerone.id/"
#     sql_injection_scanner(target_url)





# from cryptography.fernet import Fernet
# import os
#
#
# def generate_key():
#     """Generates a random encryption key and saves it to a file."""
#     key = Fernet.generate_key()
#     with open("secret.key", "wb") as key_file:
#         key_file.write(key)
#
#
# def load_key():
#     """Loads the secret key from the file."""
#     return open("secret.key", "rb").read()
#
#
# def encrypt_file(file_path):
#     """Encrypts the specified file."""
#     key = load_key()
#     f = Fernet(key)
#
#     with open(file_path, "rb") as original_file:
#         original = original_file.read()
#
#     encrypted = f.encrypt(original)
#
#     with open(file_path + ".encrypted", "wb") as encrypted_file:
#         encrypted_file.write(encrypted)
#
#     print(f"File encrypted: {file_path}.encrypted")
#
#
# def decrypt_file(file_path):
#     """Decrypts an encrypted file."""
#     key = load_key()
#     f = Fernet(key)
#
#     with open(file_path, "rb") as encrypted_file:
#         encrypted_data = encrypted_file.read()
#
#     decrypted = f.decrypt(encrypted_data)
#
#     with open(file_path.replace(".encrypted", ""), "wb") as decrypted_file:
#         decrypted_file.write(decrypted)
#
#     print(f"File decrypted: {file_path.replace('.encrypted', '')}")
#
#
# if __name__ == "__main__":
#     # Generate a key first
#     generate_key()
#
#     # Create a test file
#     with open("test.txt", "w") as f:
#         f.write("This is a sensitive text.")
#
#     # Encrypt the file
#     encrypt_file("test.txt")
#
#     # Define the encrypted file's name
#     encrypted_file_path = "test.txt.encrypted"
#
#     # Decrypt the file
#     decrypt_file(encrypted_file_path)
#
#     # Compare the contents of the original and decrypted files
#     with open("test.txt", "r") as original:
#         original_content = original.read()
#
#     with open("test.txt", "r") as decrypted:
#         decrypted_content = decrypted.read()
#
#     print(f"Original content: {original_content}")
#     print(f"Decrypted content: {decrypted_content}")


# This script checks a list of IP addresses against a simulated threat intelligence feed.
# In a real scenario, the feed would be fetched from an external source or API.

# import requests
# import os


# def check_against_threat_intel(ip_list):
#     """
#     Checks a list of IP addresses against a known list of malicious IPs.
#
#     Args:
#         ip_list (list): A list of IP addresses to check.
#     """
#     print("--- Threat Intelligence Check ---")
#
#     # Simulate a threat intelligence feed of known malicious IPs
#     # In a real application, you would fetch this from a public API
#     # like AbuseIPDB or a commercial threat feed service.
#     known_malicious_ips = {
#         '192.168.100.1',  # Example attacker from our log file
#         '192.168.100.79',
#         '198.51.100.11'
#     }
#
#     if not ip_list:
#         print("No IPs provided to check.")
#         return
#
#     for ip in ip_list:
#         if ip in known_malicious_ips:
#             print(f"[!!!] ALERT: IP {ip} is flagged as malicious in our threat feed!")
#         else:
#             print(f"[OK] IP {ip} is not in our known malicious list.")
#
#
# if __name__ == "__main__":
#     # Example list of IPs to check (could be from the log analyzer script)
#     ips_to_check = [
#         '192.168.100.1',
#         '192.168.100.79',  # The IP from the log file that was flagged
#         '198.51.100.11'
#     ]
#
#     check_against_threat_intel(ips_to_check)


# This script analyzes a web server log file to find suspicious activities.
# It uses regular expressions to parse logs and flags suspicious user agents.

# This script analyzes a web server log file to find suspicious activities.
# It uses a single, precise regular expression to parse logs and flags suspicious user agents.

# import re
# import collections
#
#
# def analyze_logs(log_file_path):
#     """
#     Parses a log file, identifies and reports on suspicious activity.
#
#     Args:
#         log_file_path (str): The path to the log file.
#     """
#     # A list of user agents commonly associated with scanners or bots.
#     suspicious_agents = [
#         "Nmap Scripting Engine",
#         "nessus",
#         "nikto",
#         "Wget",
#         "Python-urllib"
#     ]
#
#     # A regular expression pattern to parse common log formats
#     # This single-line pattern is more robust and prevents "greedy" matching issues.
#     log_pattern = re.compile(
#         r'(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<timestamp>.*?)\] '
#         r'"(?P<request_type>GET|POST|PUT|DELETE)\s(?P<url>.*?)\sHTTP/\d\.\d" '
#         r'(?P<status_code>\d{3}) (?P<bytes>\d+) '
#         r'"(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
#     )
#
#     print("--- Log Analysis Report ---")
#
#     # We use a dictionary to keep track of suspicious IPs
#     suspicious_ips = collections.defaultdict(list)
#
#     try:
#         with open(log_file_path, 'r') as f:
#             for line_num, line in enumerate(f, 1):
#                 # Try to match each log line to our pattern
#                 match = log_pattern.match(line)
#                 if not match:
#                     print(f"Warning: Could not parse line {line_num}: {line.strip()}")
#                     continue
#
#                 # Extract data from the matched groups
#                 data = match.groupdict()
#                 user_agent = data['user_agent']
#                 ip_address = data['ip_address']
#
#                 # Check for suspicious user agents
#                 for agent in suspicious_agents:
#                     if agent in user_agent:
#                         print(f"[!] Suspicious User Agent detected from IP: {ip_address} on line {line_num}")
#                         print(f"    User Agent: {user_agent}")
#                         suspicious_ips[ip_address].append(line_num)
#                         break
#
#         print("\n--- Summary of Suspicious IPs ---")
#         if suspicious_ips:
#             for ip, lines in suspicious_ips.items():
#                 print(f"IP: {ip} was flagged on lines: {lines}")
#         else:
#             print("No suspicious activity found based on user agents.")
#
#     except FileNotFoundError:
#         print(f"Error: The file '{log_file_path}' was not found.")
#
#
# # In a real-world scenario, you would have a continuously updated log file.
# if __name__ == "__main__":
#     # The name of our simulated log file
#     analyze_logs('access_log.txt')


# def run_quiz():
#
#     # Initialize score
#     score = 0
#
#     # Define questions, options, and correct answers
#     questions = [
#         {
#             "question": "What is the capital of France?",
#             "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
#             "correct": "B"
#         },
#         {
#             "question": "Which planet is known as the Red Planet?",
#             "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
#             "correct": "B"
#         },
#         {
#             "question": "What is 5 + 7?",
#             "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
#             "correct": "C"
#         }
#     ]
#     import random
#     random.shuffle(questions)
#     print("Welcome to the Simple Quiz Game!")
#     print("Answer the following questions by typing A, B, C, or D.\n")
#
#     # Ask each question
#     for i, q in enumerate(questions, 1):
#         print(f"Question {i}: {q['question']}")
#         for option in q['options']:
#             print(option)
#
#         # Get user input with validation
#         while True:
#             answer = input("\nYour answer: ").strip().upper()
#             if answer in ['A', 'B', 'C', 'D']:
#                 break
#             else:
#                 print("Please enter A, B, C, or D.")
#
#         # Check if answer is correct
#         if answer == q['correct']:
#             print("Correct! ✓")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {q['correct']}.")
#
#         print()  # Add a blank line between questions
#
#     # Display final score
#     print(f"Quiz completed! Your final score is {score}/{len(questions)}")
#
#     # Provide feedback based on score
#     if score == len(questions):
#         print("Perfect! You're a quiz master!")
#     elif score >= len(questions) / 2:
#         print("Good job! You know your stuff.")
#     else:
#         print("Keep learning! You'll do better next time.")
#
#
# # Run the quiz
# if __name__ == "__main__":
#     run_quiz()



# def expense_tracker():
#     """
#     A simple expense tracker that allows users to add, view, and delete expenses.
#     """
#     expenses = []
#
#     def add_expense():
#         try:
#             amount = float(input("Enter expense amount: "))
#             category = input("Enter expense category (e.g., Food, Transport): ")
#             description = input("Enter expense description: ")
#             expenses.append({
#                 "amount": amount,
#                 "category": category,
#                 "description": description
#             })
#             print("Expense added successfully.")
#         except ValueError:
#             print("Invalid amount. Please enter a numeric value.")
#
#     def view_expenses():
#         if not expenses:
#             print("No expenses recorded.")
#             return
#         print("\n--- Expense List ---")
#         for i, expense in enumerate(expenses, 1):
#             print(f"{i}. Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")
#         total = sum(expense['amount'] for expense in expenses)
#         print(f"Total Expenses: ${total:.2f}\n")
#
#     def delete_expense():
#         view_expenses()
#         if not expenses:
#             return
#         try:
#             index = int(input("Enter the number of the expense to delete: ")) - 1
#             if 0 <= index < len(expenses):
#                 removed = expenses.pop(index)
#                 print(f"Removed expense: Amount: ${removed['amount']:.2f}, Category: {removed['category']}, Description: {removed['description']}")
#             else:
#                 print("Invalid index.")
#         except ValueError:
#             print("Please enter a valid number.")
#
#     while True:
#         action = input("Choose an action: add, view, delete, exit: ").lower()
#         if action == "add":
#             add_expense()
#         elif action == "view":
#             view_expenses()
#         elif action == "delete":
#             delete_expense()
#         elif action == "exit":
#             print("Exiting Expense Tracker. Goodbye!")
#             break
#         else:
#             print("Invalid action. Please choose from add, view, delete, exit.")
# expense_tracker()


# from tkinter import *
# windows = Tk()
# windows.mainloop()

# def expense_tracker():
#     expenses = []
#
#     while True:
#         print("\nChoose an action: add, view, total, exit")
#         action = input("Action: ").lower()
#
#         if action == "add":
#             try:
#                 amount = float(input("Enter amount: "))
#                 category = input("Enter category (e.g., food, transport): ")
#                 description = input("Enter description: ")
#                 expenses.append({
#                     "amount": amount,
#                     "category": category,
#                     "description": description
#                 })
#                 print("Expense added successfully.")
#             except ValueError:
#                 print("Invalid amount. Please enter a number.")
#
#         elif action == "view":
#             if expenses:
#                 print("\nYour Expenses:")
#                 for i, exp in enumerate(expenses, 1):
#                     print(f"{i}. {exp['amount']} HUF - {exp['category']} - {exp['description']}")
#             else:
#                 print("No expenses recorded yet.")
#
#         elif action == "total":
#             total = sum(exp["amount"] for exp in expenses)
#             print(f"\nTotal spent: {total:.2f} HUF")
#
#         elif action == "exit":
#             print("Exiting Expense Tracker. Goodbye!")
#             break
#
#         else:
#             print("Invalid action. Please choose from add, view, total, exit.")
# HUF_TO_EUR_RATE = 0.0026  # Update this as needed
# expense_tracker()



































