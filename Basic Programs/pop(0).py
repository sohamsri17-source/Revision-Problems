guest = ['rohan', 'ridam', 'priyam', 'shrea', 'harsh', 'pranjal', 'rishu', 'twinkle' ]
print(f"Hey, I am  hosting a dinner  party at my house you both are most welcomed Mr.{guest[0].title()} and Mr.{guest[1].title()} .")
print(f"Hey, I am  hosting a dinner  party at my house you both are most welcomed Mr.{guest[2].title()} and Mrs.{guest[3].title()}. ")
print(f"Hey, I am  hosting a dinner  party at my house you three are most welcomed Mr.{guest[4].title()}, Mr.{guest[5].title()} and Mrs. {guest[7].title()}. ")
print(f"Hey, I am  hosting a dinner  party at my house you are most welcomed Mr.{guest[6].title()}.")


guest = ['rohan', 'ridam', 'priyam', 'shrea', 'harsh', 'pranjal', 'rishu', 'twinkle' ]
popped_guest = guest.pop(6)
print(f"I am sorry  to hear that you  can't make it because of  your load of work  Mr.{popped_guest.title()}. ")
guest.insert(6, 'navya')
print(f"Hey, I am  hosting a dinner  party at my house you are most welcomed Mrs.{guest[6].title()}./n ")
print(f" Number of  people in the dinner party is : {len(guest)}.")