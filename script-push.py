import git

studentName = "Valerie Eve Taniputra"
teacherName = "Mr. Ahmad Yazid"


local_repo_path = "C:/Github Koding Next/Python-First"

def git_pull_push(repo_path, student, teacher):
    try:
        repo = git.Repo(repo_path)

        repo.git.execute("git pull")
        repo.git.execute("git add .")
        repo.git.execute(f'''git commit -m "Uploading the Projects Made by {student} from {teacher}'s Class"''')
        repo.git.execute("git push")

        print(f"File project {student} pada folder {repo_path} berhasil di upload")
    except Exception as e:
        print(f"Terjadi kesalahan {str(e)}")

git_pull_push(local_repo_path, studentName, teacherName)