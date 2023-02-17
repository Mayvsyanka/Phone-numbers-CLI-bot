phone_list = {}

command_list = ["hello", "add", "change", "phone",
                "show all", "good bye", "close", "exit"]


def input_error(func):
    def inner(phone_list, name_phone):
        try:
            func(phone_list, name_phone)
        except (IndexError):
            print("Give me name and phone please")
        except (KeyError):
            print("Give user name")
        except (ValueError):
            print("Give phone number")
    return (inner)


def greeting(): return "How can I help you?"


@input_error
def add_num(phone_list, name_phone): return phone_list.update(
    {name_phone[1]: int(name_phone[2])})


@input_error
def change_num(
    phone_list, name_phone): phone_list[name_phone[1]] = int(name_phone[2])


@input_error
def phone_print(phone_list, name_phone):
    print(phone_list[name_phone[1]])


def show_all(): return (phone_list)


def bye(): return ("Good bye!")


def main():
    while True:
        command = input("your command:")
        name_phone = command.split(" ")

        if "hello" in command.lower():
            print(greeting())

        if "add" in command.lower():
            add_num(phone_list, name_phone)

        if "change" in command.lower():
            change_num(phone_list, name_phone)

        if "phone" in command.lower():
            phone_print(phone_list, name_phone)

        if "show all" in command.lower():
            print(show_all())

        if "good bye" in command.lower() or "close" in command.lower() or "exit" in command.lower():
            print(bye())
            break


main()
