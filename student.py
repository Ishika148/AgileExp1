def validate_student(name, email):
    return bool(name) and "@" in email

print(validate_student("Ishika", "aroteishika2006@gmail.com"))
