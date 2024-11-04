## Clean Up Instructions

This section provides step-by-step instructions for removing and cleaning all project-related components from AWS and Raspberry Pi4B. Following these steps helps avoid unnecessary costs and restores the environment to its pre-project state.

---

### Step 1: Remove Greengrass Components from Raspberry Pi4B

1. **Remove Deployed Components:**
   - Use the following command to remove all components deployed to the Greengrass Core device:
     ```bash
     sudo /greengrass/v2/bin/greengrass-cli deployment create --remove="com.greengrass.ProjectRPi4B"
     ```

2. **Verify Removal:**
   - Wait a minute for the removal process to complete. Then, confirm that all components have been removed by listing the components:
     ```bash
     sudo /greengrass/v2/bin/greengrass-cli component list
     ```
   - The removed component should no longer appear on the list if successful.

3. **Uninstall Greengrass Core Software:**
   - Run this command to uninstall AWS IoT Greengrass Core software from the Raspberry Pi:
     ```bash
     sudo rm -rf /greengrass
     ```

---

### Step 2: Delete S3 Bucket and Contents

1. **Go to S3 Console:**
   - Navigate to **AWS Console > S3 > Buckets**.

2. **Delete Project Bucket:**
   - Select the project bucket (`ggc-project-s3-bucket`) and delete all contents. 
   - **Note:** S3 buckets can only be deleted once empty.

3. **Delete S3 Bucket:**
   - After confirming that the bucket is empty, delete `ggc-project-s3-bucket`.

---

### Step 3: Remove IAM Roles, Policies, and Users

1. **Remove Custom Policies:**
   - Go to **AWS Console > IAM > Policies**.
   - Locate and delete the following custom policies:
     - `customGGCRPi4BPolicy`
     - `customGreengrassProvisionPolicy`
     - `customGreengrassS3Access`
     - `GreengrassV2TokenExchangeRoleAccess`

2. **Detach and Delete IAM Roles:**
   - Go to **IAM > Roles** and locate the following roles:
     - `GreengrassRole`
     - `GreengrassV2TokenExchangeRole`
   - Detach all policies from these roles before deleting them.

3. **Delete IAM User and Group:**
   - Go to **IAM > Users** and delete the `ggc_user`.
   - Go to **IAM > Groups** and delete the `ggc_group`.

---

### Step 4: Delete AWS IoT Core Device and Thing Resources

1. **Go to AWS IoT Console:**
   - Navigate to **AWS Console > IoT Core > Manage > Things**.

2. **Delete Greengrass Core Device (`GGC1`):**
   - Locate `GGC1` and delete it with all associated certificates and policies.

3. **Delete Thing Group (`GGCGroup`):**
   - Go to **Manage > Thing Groups** and delete the `GGCGroup`.

---

### Step 5: Confirm Clean Up

1. **Check Remaining Resources:**
   - Review the AWS Console and Raspberry Pi environment to ensure that all components, resources, and files related to the project have been removed.

2. **Review Billing Dashboard:**
   - Go to **AWS Billing Dashboard** to confirm no unexpected charges are associated with the remaining resources.

**Note:** Some AWS resources may take a few minutes to disappear from the console after being deleted. Verify in the AWS Console if any resources remain active and repeat the deletion steps as necessary.

---

This completes the cleanup process for the AWS Greengrass V2 and Raspberry Pi 4B project.

