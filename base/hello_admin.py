current_users = ['admin','user1','user2','user3','user4']
new_users = ['User1','user2','user6','user7','user8']
if new_users:
	for new_user in new_users:
		if new_user in current_users :
			print (f'Hello Master {new_user}. You are log in. ')
		else :
			print (f"Hello, try to change login and try again")
else:
	print (f"We are need user to auth")			


