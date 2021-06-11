def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return  user_info
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
user_profile_0 = build_profile('Nikita','Chernyavskiy',height=180,weight=85)
print(user_profile_0)