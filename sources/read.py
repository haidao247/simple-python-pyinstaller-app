import os



class Pr:
    @property
    def pr_id(self) -> str | None:
        return os.getenv("CHANGE_ID")



print('this is PR number',Pr().pr_id)
###################


# repo_owner = 'haidao247'
# repo_name = 'simple-python-pyinstaller-app'
# repo = (f"{repo_owner}/{repo_name}")

# # //Iterate through all open pull requests in the repository
# for pull_request in repo.get_pulls(state='open'):
#     print(f"Checking Pull Request #{pull_request.number} - {pull_request.title}")

 
#     files = pull_request.get_files()

#     for file in files:
#         print(f"File: {file.filename}")

     
#         patch_content = file.patch

#         patch_lines = patch_content.split('\n')

   
#         added_lines = [line[2:] for line in patch_lines if line.startswith('+ ') and not line.startswith('+++')]
#         print("Added Lines:")
#         for added_line in added_lines:
#             print(added_line)

#         print("\n" + "=" * 50 + "\n")  # Separating each file's output

#     print("\n" + "=" * 50 + "\n")  # Separating each pull request's output



# path = './file'

# def read_file(path):

#     files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


#     for file_name in files:
#         file_path = os.path.join(path, file_name)
#         with open(file_path, 'r') as file:
#             content = file.read()
#             print(f"Content of {file_name}:")
#             print(content)
#             print("=" * 50)  # Just for separation between file contents

# read_file(path)


