favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
new_favorite_languages = ['nikita','sveta','phil','sarah']
for name in new_favorite_languages:

        if name in favorite_languages.keys():
            print(f'{name.title()} You was vote in this interview,sorry ')
        else:
            print(f'{name.title()} Do you want to run interview now?')