# global listStd
# listStd = ["John Smith", "Claire Temple", "Steve Roger"]

User_Data = "user_data.txt"
import re


def read_user_data():
    user_data = []
    with open("user_data.txt", "r") as file:
        for line in file:
            info = line.split(",")
            user_data.append(info)
    return user_data


# You can define a function to write user data to the file.
def write_user_data(user_data):
    with open("user_data.txt", "a") as file:
        username = user_data[0]
        password = user_data[1]
        email = user_data[2]
        url = user_data[3]
        number = user_data[4]
        gitlink = user_data[5]
        likedinlink = user_data[6]
        address = user_data[7]

        file.write(
            "{}, {}, {}, {}, {}, {}, {}, {}\n".format(
                username, password, email, url, number, gitlink, likedinlink, address
            )
        )
        # file.write("{}\n".format(user_data))

        # for i in user_data:
        #     file.write(f"{i},\n")
    print("\n=> New Member {} Successfully Add \n".format(user_data))


def get_existing_users():
    with open("user_data.txt", "r") as fp:
        for line in fp:
            # This expects each line of a file to be (name, pass) seperated by whitespace
            username = line.strip().split()


def user_exists(username):
    db = open("user_data.txt", "r")
    x = []
    for line in db:
        x = line.strip().split(",")
    if username in x:
        return True
    else:
        return False


def username_validation():
    while True:
        print("Please Provide Username")
        name = str(input("Name: "))
        username = name
        if user_exists(username):
            print("Try Again with different username")
            print("\nThis Member {} Already In The Database".format(name))
            continue
        elif name[0].isalpha() is False:
            print("Your username should startswith alphabate. Please try again: ")
            continue
        elif len(name) < 5:
            print("Your username is too short. Please try again: ")
            continue
        elif name.count(" ") > 0:
            print("Your username contains spaces. Please try again: ")
            continue
        elif name.isalnum() is False:
            print("Your username contains a special character. " "Please try again: ")
            continue
        else:
            print("Username is created")
        return username


# Function to validate the password
def password_check():
    while True:
        print("Please Provide password")
        passwd = str(input("Password: "))
        SpecialSym = ["$", "@", "#", "%"]
        val = True
        if len(passwd) < 6:
            print("length should be at least 6")
            val = False
            continue

        if len(passwd) > 20:
            print("length should be not be greater than 8")
            val = False
            continue

        if not any(char.isdigit() for char in passwd):
            print("Password should have at least one numeral")
            val = False
            continue
        if not any(char.isupper() for char in passwd):
            print("Password should have at least one uppercase letter")
            val = False
            continue

        if not any(char.islower() for char in passwd):
            print("Password should have at least one lowercase letter")
            val = False
            continue
        if not any(char in SpecialSym for char in passwd):
            print("Password should have at least one of the symbols $@#")
            val = False
            continue
        if val:
            c = input("Confirm Password: ")
        while c != passwd:
            print("Password not match, Try Again")
            c = input("Try Again Confirm Password: ")
        return passwd


# email validation
def email_validate():
    while True:
        print("Please Provide Valid Email Address")
        email = str(input("Email: "))
        email = email.strip().lower()
        if not "@" in email:
            print("Invalid email,Try Again")
            continue
        elif not (".com" or ".org" or ".edu" or ".gov" or ".net") in email[-4:]:
            print("Invalid email,Try Again")
            continue
        elif not email[-4:] in ".com.org.edu.gov.net":
            print("Invalid email,Try Again")
            continue
        return email


def is_valid_url():
    print("Please Provide Valid portfolio link")
    url = str(input("website: "))
    pattern = r"^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$"
    if not bool(re.match(pattern, url)):
        print("Invalid Url")
        is_valid_url()
    else:
        print("its valid url")
        return url


def valid_num():
    print("Please Provide Valid Phone Numper")
    num = str(input("Phone Number: "))
    # Check if number length is greater or less then 10
    if len(num) > 11 or len(num) < 10:
        print("Number is not valid (Enter a 11 digit number)")
        valid_num()
    else:
        # Check if first number is 1 and secnd is  9 -1
        if (
            num[0] == "0"
            or num[1] == "1"
            and num[:2] == [5, 6, 7, 8, 9]
            and len(num[3:] == 9)
        ):
            try:
                num = int(num)
                print("Your number is valid")
            except:
                print(
                    "Number is not valid (A number should not contain any characters)"
                )
                valid_num()
            return num

        else:
            print("Number is not valid (A number should start with 0 )")
            valid_num()


def url_github():
    print("Please Provide GitHub Url")
    link1 = str(input("GitHub link: "))
    if not link1.startswith("https://github.com/"):
        # raise ValueError(f"URL {link1} is not valid github link")
        print(f"URL {link1} is not valid github link, Please Try Again")
        url_github()
    else:
        print("its valid url")
        return link1


def url_linkedin():
    print("Please Provide LinkedIn Profile")
    link2 = str(input("LinkedIn link: "))
    if not link2.startswith("https://www.linkedin.com/in/"):
        print(f"URL {link2} is not valid github link, Please Try Again")
        url_linkedin()
    else:
        print("its valid url")
        return link2


def address_line():
    while True:
        print("Please Provide Adddress Line")
        address_line = str(input("address: "))
        if len(address_line) < 0:
            print("Your address_line should not be blank. Please try again: ")
            continue
        elif address_line.isalnum() is False:
            print("Invalid address_line. Please try again: ")
            continue
        else:
            print("its valid Addressl")
            return address_line


def ask_user_credentials():
    username = username_validation()
    password = password_check()
    email = email_validate()
    url = is_valid_url()
    number = valid_num()
    gitlink = url_github()
    likedinlink = url_linkedin()
    address = address_line()
    return (username, password, email, url, number, gitlink, likedinlink, address)


def register_user():
    (
        username,
        password,
        email,
        url,
        number,
        gitlink,
        likedinlink,
        address,
    ) = ask_user_credentials()
    user_data = read_user_data()
    user_data = [username, password, email, url, number, gitlink, likedinlink, address]
    write_user_data(user_data)
    print("User created successfully.")
    # print("Your data is:", url, email, number)


def manageMember():
    print(
        """ 

  ---------------------------------------------------------
 |========================================================| 
 |======== Welcome To Resume Building System =========|
 |========================================================|
  ---------------------------------------------------------

Enter 1 : To View Resume List 
Enter 2 : Resume for New Member 
Enter 3 : To Remove Resume 
Enter 4 : Exit
		
		"""
    )

    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")

    if userInput == 1:
        print("List of Members")
        listStd = []
        sl = 0
        db = open("user_data.txt", "r")
        for line in db:
            x = line.strip().split(",")
            # listStd.append(x)
            # for members in listStd:
            #     # print(members)
            sl += 1
            print(" Resume Building System=>sl:{} {}  \n".format(sl, x))

    elif userInput == 2:
        register_user()

    elif userInput == 3:
        rmStd = input("Enter Member Name To Remove: ")
        db = open("user_data.txt", "r")
        for line in db:
            listStd = line.strip().split(",")
            for row in listStd:
                if rmStd in row:
                    listStd.remove(row)
                    print("\n=> Member {} Successfully Deleted \n".format(rmStd))
            print("=> {}".format(listStd))
        else:
            print("\n=> No Record Found of This Member {}".format(rmStd))

    elif userInput == 4:
        print("Exiting the system.")
        quit()

    elif userInput < 1 or userInput > 4:
        print("Please Enter Valid Option")


manageMember()


def runAgain():
    runAgn = input("\nContinue Transaction? y/n: ")
    if runAgn.lower() == "y":
        manageMember()
        runAgain()
    else:
        quit()


runAgain()
