
from github import Github
import os

# GitHub access token
token = "Your-Git-Token"
g = Github(token)

# Connect to GitHub and get user
user = g.get_user()

# Create a new repository
def create_repo(repo_name):
    try:
        repo = user.create_repo(repo_name)
        print(f"Repository '{repo_name}' created successfully!")
        return repo
    except Exception as e:
        print(f"Error: {e}")

# Delete a repository
def delete_repo(repo_name):
    try:
        repo = user.get_repo(repo_name)
        repo.delete()
        print(f"Repository '{repo_name}' deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Add a file to the repository from local system
def add_file_from_local(repo_name, file_path):
    try:
        # Open the local file and read its content
        with open(file_path, 'r') as file:
            content = file.read()

        # Get the file name from the file path
        file_name = os.path.basename(file_path)

        # Upload file to GitHub repository
        repo = user.get_repo(repo_name)
        repo.create_file(file_name, "Adding file from local system", content)
        print(f"File '{file_name}' from local system added to repo '{repo_name}'")

    except Exception as e:
        print(f"Error: {e}")

# Update a file in the repository
def update_file(repo_name, file_name, content, sha):
    try:
        repo = user.get_repo(repo_name)
        repo.update_file(file_name, "Updating file", content, sha)
        print(f"File '{file_name}' updated in repo '{repo_name}'")
    except Exception as e:
        print(f"Error: {e}")

# Delete a file in the repository
def delete_file(repo_name, file_name, sha):
    try:
        repo = user.get_repo(repo_name)
        repo.delete_file(file_name, "Deleting file", sha)
        print(f"File '{file_name}' deleted from repo '{repo_name}'")
    except Exception as e:
        print(f"Error: {e}")

# Generate README file automatically
def generate_readme(content):
    readme_content = f"# Project Title\n\n{content}"
    return readme_content

# Menu function for user options
def menu():
    print("Select an action:")
    print("1. Create Repository")
    print("2. Delete Repository")
    print("3. Add File from Local System to Repository")
    print("4. Update File in Repository")
    print("5. Delete File from Repository")
    print("6. Generate README File")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        repo_name = input("Enter repository name: ")
        create_repo(repo_name)
    elif choice == '2':
        repo_name = input("Enter repository name to delete: ")
        delete_repo(repo_name)
    elif choice == '3':
        repo_name = input("Enter repository name: ")
        file_path = input("Enter the full local file path: ")
        add_file_from_local(repo_name, file_path)
    elif choice == '4':
        repo_name = input("Enter repository name: ")
        file_name = input("Enter file name: ")
        content = input("Enter updated file content: ")
        sha = input("Enter SHA of the file to update: ")
        update_file(repo_name, file_name, content, sha)
    elif choice == '5':
        repo_name = input("Enter repository name: ")
        file_name = input("Enter file name: ")
        sha = input("Enter SHA of the file to delete: ")
        delete_file(repo_name, file_name, sha)
    elif choice == '6':
        content = input("Enter content for README: ")
        readme = generate_readme(content)
        print("\nGenerated README file:\n")
        print(readme)
    elif choice == '7':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    while True:
        menu()
