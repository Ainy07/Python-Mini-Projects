#user input
email = input("Please enter your email:").strip()


#definig username and domain parts
username_part = email[:email.index("@")]
domain_name = email[email.index("@")+1:]


output = (f"Your user name is '{username_part}' and your domain is '{domain_name}'")


#genrating the output
print(output)