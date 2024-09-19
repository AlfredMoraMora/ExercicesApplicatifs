Still learning how to push files from school pc

Here`s a tutorial on how to do it 

Here’s a step-by-step guide to upload your project to GitHub while addressing the credentials issue you encounter on your school computer. Since the computer resets after each reboot, you can use **GitHub’s HTTPS method** with a **personal access token** instead of your username/password for authentication. This method is more secure and avoids credential issues.

### Step 1: Create a GitHub Repository
1. Go to [GitHub.com](https://github.com) and log in to your account.
2. Click on the **+** icon (top-right) and select **New repository**.
3. Enter the repository name (e.g., `my-school-project`), and optionally add a description.
4. Choose the repository type (public or private).
5. Click **Create repository**.

### Step 2: Install Git (if not installed)
1. Open the terminal/command line on your school computer.
2. Type `git --version` to check if Git is installed.
   - If not installed, download it from [Git SCM](https://git-scm.com/) and follow the installation instructions.

### Step 3: Clone the Repository to Your Local Machine
1. Go to your repository on GitHub.
2. Click the **Code** button and copy the repository URL (use HTTPS).
3. In the terminal, run the following command to clone the repository:
   ```bash
   git clone https://github.com/your-username/my-school-project.git
   ```
4. This will create a folder named `my-school-project` on your machine.

### Step 4: Add Your Project Files to the Repository
1. Move your project files into the cloned repository folder. You can either drag and drop or use the command line:
   ```bash
   mv /path/to/your/project/* /path/to/my-school-project/
   ```
   
2. Navigate to the folder in the terminal:
   ```bash
   cd my-school-project
   ```

### Step 5: Set Up Git Config (Credentials)
Since your school computer resets, you may have issues with credentials each time. Here’s how to set up Git to use HTTPS with a personal access token (PAT).

1. **Set Git username and email** (only needed once per session):
   ```bash
   git config --global user.name "your-username"
   git config --global user.email "your-email@example.com"
   ```

2. **Generate a Personal Access Token**:
   - Go to [GitHub Tokens](https://github.com/settings/tokens).
   - Click **Generate new token**.
   - Give it a descriptive name, like "School Computer Token".
   - Under "Select scopes", check `repo` and `workflow` (this allows you to push code).
   - Click **Generate token** and **copy** the token (it will not be shown again).

3. **Use the Token to Authenticate**:
   When you push your changes (next step), Git will prompt you for credentials. Instead of entering your password, use the **personal access token** as your password.

### Step 6: Push Your Project to GitHub
1. In the terminal, add the project files to the repository:
   ```bash
   git add .
   ```
2. Commit your changes:
   ```bash
   git commit -m "Initial commit"
   ```
3. Push the changes to GitHub:
   ```bash
   git push origin main
   ```
   - Git will ask for your GitHub username and password:
     - **Username**: Enter your GitHub username.
     - **Password**: Enter the **personal access token** you generated earlier.

### Step 7: (Optional) Save Credentials Temporarily
If you don’t want to enter your username and token every time you push changes (within a single session), you can configure Git to cache your credentials:
```bash
git config --global credential.helper cache
```
This caches your credentials for a few hours.

---

### Summary of Steps:
1. Create a GitHub repository.
2. Clone the repository to your local machine.
3. Move your project files into the cloned repo folder.
4. Configure Git username and email.
5. Generate and use a GitHub personal access token.
6. Add, commit, and push your changes to GitHub.

Each time the computer resets, you'll just need to:
- Clone the repository again.
- Configure Git username/email.
- Use your **personal access token** for authentication during `git push`.

This approach avoids credential issues while uploading your project to GitHub.
