# CMD Challenge - Command Line for the win!

I completed the [CMD CHALLENGE](https://cmdchallenge.com/) and uploaded screenshots (using SFTP) showing that I completed all the required levels.

## Project Overview

This project involves taking screenshots of completed levels from the CMD Challenge and transferring them to a specified directory on a remote sandbox environment. Additionally, you will upload these screenshots to your GitHub repository.

## Steps to Complete the Project

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:
   ```sh
   git clone <repository_url>
   ```

2. **Complete the CMD Challenge:**
   Go through the CMD Challenge tasks and take screenshots of your completed levels. Store these screenshots in a local folder.

3. **SFTP File Transfer:**
   Open a terminal or command prompt on your local machine. Use the following commands to transfer screenshots to the sandbox environment:
   ```sh
   sftp username@hostname
   cd /root/alx-system_engineering-devops/command_line_for_the_win/
   put path/to/local/screenshot.png
   ```
   Repeat the `put` command for each screenshot.

4. **Confirm File Transfer:**
   Verify that the screenshots have been successfully transferred by listing the files in the sandbox directory using `ls` command.

5. **Update README:**
   Update the `README.md` file in your local repository with the steps you followed to use SFTP for transferring files.

6. **Push to GitHub:**
   Commit your changes and push them to your GitHub repository:
   ```sh
   git add .
   git commit -m "Add screenshots and update README"
   git push origin main
   ```

7. **Submission:**
   Submit the link to your GitHub repository through the required platform or method.

## Additional Resources

- [SFTP Guide](https://man.openbsd.org/sftp)
- [SFTP File Transfer Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
