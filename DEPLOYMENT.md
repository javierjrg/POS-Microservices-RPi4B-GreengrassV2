## Component Build, Test, Deployment, and Troubleshooting

### Build

1. **Create S3 Bucket**
   - Go to **AWS Console > S3 > Create bucket**.
   - Name the bucket: `ggc-project-s3-bucket`, keep default settings, and create it.
   - Note the S3 bucket ARN to update the S3 policy created earlier.

   **AWS Documentation Reference:** [Step 5: Create your AWS IoT Greengrass service component](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-create.html). Replace `"com.example.HelloWorld"` with the project component name, `"ComponentName": "com.greengrass.ProjectRPi4B"`.

   **Note:** Ensure correct syntax, including commas, to avoid deployment errors indicating "Broken" status in the console and Greengrass CLI.

2. **Create S3 Directories**
   - Follow the project’s folder structure:
     - **AWS Console > S3 > Select `ggc-project-s3-bucket` > Objects tab > Create folder**
     - Folder name: `greengrass_rpi4Project` (leave defaults as is).
   - Continue creating the following structure:

     ```
     ~ Amazon S3 ──
     ├── Buckets
         ├── ggc-project-s3-bucket
             ├── greengrass_rpi4Project/
                 ├── 1.0.0/
     ```

3. **Upload Scripts to S3**
   - Ensure that `s3_uploader.py` and `s3_test1.py` are copied to the `1.0.0` folder.

   **Note:** Missing the `s3_uploader.py` file will cause deployment failures with non-specific error messages like “Exit with Error Code 1.” Always verify the code and steps carefully.

4. **Write Artifact and Recipe Components**
   - **Write the Python Artifact Code:**
     ```bash
     cd greengrassv2/artifacts/com.greengrass.ProjectRPi4B/1.0.0/
     nano s3_test1.py
     ```
     - Paste the `s3_test1.py` script from the project’s GitHub Script folder [here](Scripts).
     - **Save and exit:** `Ctrl + X`

   - **Ensure Configuration Matches:** Verify `BUCKET_NAME` and `S3_FILE_NAME` in `s3_test1.py` match your S3 folder structure.

   - **Make the File Executable:**
     ```bash
     sudo chmod +x s3_test1.py
     ```

   - **Write the Recipe:**
     ```bash
     cd ~/greengrassv2/recipes/
     nano com.greengrass.ProjectRPi4B-1.0.0.json
     ```
     - Copy the recipe script, ensuring the S3 bucket information matches the `"Artifacts URI"` line:
       ```json
       "Artifacts": [
           {
             "URI": "s3://ggc-project-s3-bucket/greengrass_rpi4Project/1.0.0/s3_test1.py"
           }
         ]
       ```

   - **Create the `s3_bucket_content.py` Script:**
     ```bash
     cd ~/greengrassv2/scripts/
     nano s3_bucket_content.py
     ```
     - Copy the script content, save it, and make it executable as described above.

---

### Test

1. **Test S3 Communication**
   - Run `s3_bucket_content.py` to test communication between the Raspberry Pi 4B and AWS services:
     ```bash
     python3 -u greengrassv2/scripts/s3_bucket_content.py
     ```
   - Expected output:
     ```
     ggc@ggc:~$ python3 -u greengrassv2/scripts/s3_bucket_content.py
     File: greengrass_rpi4Project/1.0.0/, Last Modified: 2024-10-26 17:01:27+00:00
     File: greengrass_rpi4Project/1.0.0/s3_uploader.py, Last Modified: 2024-10-26 17:01:56+00:00
     File: greengrass_rpi4Project/1.0.0/s3_test1.py, Last Modified: 2024-10-28 16:54:29+00:00
     ```

2. **Test `s3_test1.py` Script**
   - Run the following command:
     ```bash
     python3 -u greengrassv2/artifacts/com.greengrass.ProjectRPi4B/1.0.0/s3_test1.py
     ```
   - Expected output:
     ```
     Test 1 successful!
     File /home/ggc/greengrassv2/data/test.csv uploaded to ggc-project-s3-bucket/greengrass_rpi4Project/1.0.0/test.csv
     ```

---

### Deployment

1. **Remove Hello World Component (if it exists):**
   - Run this command to ensure the Hello World component is removed, preventing conflicts:
     ```bash
     sudo /greengrass/v2/bin/greengrass-cli deployment create --remove="com.example.HelloWorld"
     ```

2. **Deploy Project Component:**
   - Use the following command to deploy your project component:
     ```bash
     sudo /greengrass/v2/bin/greengrass-cli deployment create \
     --recipeDir ~/greengrassv2/recipes \
     --artifactDir ~/greengrassv2/artifacts \
     --merge "com.greengrass.ProjectRPi4B=1.0.0"
     ```

3. **Expected Output:**
     ```bash
     Local deployment submitted! Deployment Id: bb1e6070-d6ca-490f-b515-5b5559979b52
     ```

4. **Record the Deployment ID:**
- Save the `Deployment Id` provided in the output for future reference.

5. **Check Deployment Status:**
- Use the deployment ID from the previous step to verify the status of the deployment:
  ```bash
  sudo /greengrass/v2/bin/greengrass-cli deployment status -i bb1e6070-d6ca-490f-b515-5b5559979b52
  ```
- **Expected Output:**
  ```
  bb1e6070-d6ca-490f-b515-5b5559979b52: SUCCEEDED
  Created on: 29-10-2024 16:54:41 UTC
  ```

6. **Verify in AWS Console:**
- Navigate to **AWS IoT > Greengrass > Core devices > GGC1 > Overview > Components**.
- The status of `GGC1` should display as “Healthy,” and in the components tab, you should see:
  ```
  | com.greengrass.ProjectRPi4B | 1.0.0 | Root | Running | 1 minute ago
  ```

7. **Verify S3 Bucket Content:**
- Check that the `test.csv` file uploaded to the S3 bucket as expected:
  - **AWS Console > S3 > Buckets > ggc-project-s3-bucket > greengrass_rpi4Project/ > 1.0.0/**
- Data added to the `test.csv` file indicates successful data synchronization.

8. **Run Offline Test:**
- Run the `s3_test1.py` script with and without network connectivity:
  - **Without Network:** Data should be saved locally.
  - **With Network Reconnected:** Local data should synchronize automatically to the S3 bucket.

---

### Troubleshooting

#### Logs

1. **View Logs for Errors:**
- Use this command to review log files and identify error messages:
  ```bash
  sudo tail -f /greengrass/v2/logs/com.greengrass.ProjectRPi4B.log
  ```

2. **Filter for Errors:**
- Add a grep filter to search specifically for errors in the logs:
  ```bash
  sudo tail -f /greengrass/v2/logs/com.greengrass.ProjectRPi4B.log | sudo grep "ERROR"
  ```

3. **Consult AWS Documentation:**  
- For specific error codes and troubleshooting guidance, refer to [AWS IoT Greengrass V2 Troubleshooting](https://docs.aws.amazon.com/greengrass/v2/developerguide/troubleshooting.html).

#### Redeployment

1. **Remove Previous Deployment:**
- If errors are found and corrected, remove the existing deployment before redeploying:
  ```bash
  sudo /greengrass/v2/bin/greengrass-cli deployment create --remove="com.greengrass.ProjectRPi4B"
  ```

2. **Verify Removal:**
- Wait a minute for the system to update, then confirm the component removal:
  ```bash
  sudo /greengrass/v2/bin/greengrass-cli component list
  ```
- If the component has been successfully removed, it will no longer appear in the list.

3. **Redeploy Corrected Components:**
- Once the previous deployment is removed, use the deployment command from the **Deployment** section to redeploy the corrected components.
