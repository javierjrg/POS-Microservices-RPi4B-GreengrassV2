# SETUP.md

## Setup Instructions

1. **Prepare Raspberry Pi 4B**
   - Follow the official [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/) to set up your Raspberry Pi 4B, including configuring network and SSH access and fully updating the operating system.
   - **Note:** This project does not use the latest 64-bit OS due to compatibility issues with Python 3. As of 10/30/2024, AWS Greengrass V2 has limitations with Python 3 running in a virtual environment.

2. **Create IAM User and User Group in AWS**
   In AWS Identity and Access Management (IAM), create a user and user group to configure the AWS CLI with the necessary credentials and security policies.
   - **User and User Group Details:**
     - **Username:** `ggc_user`
     - **User Group:** `ggc_group`
   - **Access Keys:**
     - When creating `ggc_user`, generate two access keys:
       1. **Access Key 1** (named `ggc_user_ak_cli`): Used to configure the AWS CLI.
       2. **Access Key 2** (named `ggc_user_ak_lambda`): Reserved for security best practices.
     - **Download and secure the access keys.** You will use the first key to configure the AWS CLI on the Raspberry Pi.
   - **Account Setup:** To set up the AWS root account and user accounts, Follow the [Getting Started with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html) guide.

3. **Configure the Raspberry Pi for AWS IoT Greengrass V2**
   - **Set Up Environment:** Follow [AWS IoT Greengrass Setup Instructions](https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-start.html) for environment preparation on the Raspberry Pi.
   - **Install and Configure AWS CLI:** Before proceeding, install the AWS CLI and configure it with the `ggc_user_ak_cli` access key. Use [AWS CLI Installation Guide for Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html).
   - **Install AWS IoT Greengrass Core Software:**
     - Follow [Console Instructions](https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-cli-install.html) to begin the installation.
     - On the Raspberry Pi, complete the installation using the [Greengrass CLI instructions](https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-start.html).
   - **Verify Greengrass CLI Installation:** Run verification commands on the Raspberry Pi to confirm a successful installation.
   - **Run AWS Hello World Component Example:**
     - Set up the [AWS Hello World component](https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-start.html) to test and understand Greengrass functionality before starting the project.
     - **Important:** After testing, remove the Hello World component to prevent interference with project components. Use this command to remove it:
       ```bash
       sudo /greengrass/v2/bin/greengrass-cli deployment create --remove="com.example.HelloWorld"
       ```

4. **Project Folder Structure**
   - Organize the project files on the Raspberry Pi as follows:
     ```
     ~/greengrassv2/
     ├── artifacts
     │   └── com.greengrass.ProjectRPi4B
     │       └── 1.0.0
     │           └── s3_test1.py
     ├── data
     │   └── test.csv
     ├── logs
     │   └── com.greengrass.ProjectRPi4B.log
     ├── recipes
     │   └── com.greengrass.ProjectRPi4B-1.0.0.json
     └── scripts
         ├── counter.py
         └── s3_bucket_content.py
     ```

5. **Avoid Permission Errors for Component Deployment**
   - Configure permissions on the Raspberry Pi to prevent errors during component deployment.
   - **User and Group Configuration:**
     - **Raspberry Pi User:** `gcc`
     - **Greengrass User and Group:** `ggc_user` and `ggc_group` (created automatically by Greengrass)
   - **Add `gcc` User to `ggc_group`:**
     - This step resolves many permission-related issues unrelated to AWS policies. Run the following command:
       ```bash
       sudo usermod -aG ggc_group gcc
       ```
