# import base64
# import github
# import os
# import requests

# username = 'Ageeeko'
# token = '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'

# login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))
# if not os.path.exists("folder1"):
#     os.mkdir("folder1")


# def print_repo(repo):

#     print("Contents:")
#     try:
#         for content in repo.get_contents(''):
#             # check if it's a Python file
#             filename = os.path.join("folder1",
#                 f"{repo.full_name.replace('/', '-')}-{content.path}")
#             print(filename)
#             with open(filename, "wb") as f:
#                 f.write(content.decoded_content)
#             print(content)
#     except Exception as e:
#         print("Error:", e)


# # Github username from the command line
# username = "Ageeeko"
# # pygithub object
# g = github.Github()
# # get that user by username
# user = g.get_user(username)
# # iterate over all public repositories
# for repo in user.get_repos():
#     print_repo(repo)
#     print("="*100)

def correct_lines(string):
    record = False
    corrected_string = ""
    for i in string:
        if record:
            if i not in [")", "(", "'", '"', " "]:
                corrected_string += i
            else:
                return corrected_string
        else:
            if (string[string.index(i)+1] ,string[string.index(i)+2], string[string.index(i)+3]) == ("h","t", "t"):
                record = True


def func1(string):
    if len(string) > 2:
        if string[0] == "<":
            return correct_lines(string)
        else:
            return string


with open("folder1/Ageeeko-Ageeeko-README.md", "r", encoding="UTF-8") as f:
    read_list = f.read().split("\n")
    update_read_list = map(func1, read_list)
    print(list(update_read_list))
