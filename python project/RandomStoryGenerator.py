#1
#importing module
import random
#Defining a list of phrases for sentence making
topic = ['DSA', 'Python', 'Java', 'Computer Networks',' Operating Systems','html/css','c/c++','mySQL/postgradSQL']
adj = ['an important', 'an essential', 'very important', 'an interesting']
to = ['Developers', 'Student',' Professionals', 'Freshers','Exprinces']
supportive = ['learn it',' master it', 'read it', 'see it']
where = ['Coding Ninjas.', 'Code Studio.',' Code Studio Library.', 'CN guided paths.']
#generating the output
print(random.choice(topic) + ' is ' + random.choice(adj) + ' topic for ' + random.choice(to) + ', You can ' + random.choice(supportive) + ' from ' + random.choice(where))





#2
# import random
# when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
# who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
# name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
# residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
# went = ['cinema', 'university','seminar', 'school', 'laundry']
# happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
# print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
