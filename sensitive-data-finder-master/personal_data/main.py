from personal_data import PersonalData


if __name__ == '__main__':
    text_list = []
    text_list.append("My name is John Doe and my email is")

    for text in text_list:
        personal_data = PersonalData(text)
        print(personal_data)

        if not personal_data.is_empty():
            print("text contains personal data")
