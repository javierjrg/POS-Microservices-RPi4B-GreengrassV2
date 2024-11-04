# Usage Instructions

### Usage Overview
This section configures the user, user group, and AWS Greengrass V2 policies and roles. Additionally, it contains scripts to assemble all the necessary parts and tips for troubleshooting the project.

---

### Permissions

#### AWS Managed Policy
Attach the following managed policies to the user `ggc_user`:

- `AmazonS3FullAccess`
- `AWSGreengrassFullAccess`
- `AWSGreengrassResourceAccessRolePolicy`
- `AWSIoTFullAccess`
- `IAMFullAccess`

**Note:** The minimum permissions required to run this project and AWS Greengrass V2 include `AmazonS3FullAccess`, `AWSGreengrassFullAccess`, `AWSGreengrassResourceAccessRolePolicy`, and `AWSIoTFullAccess`. Adding `IAMFullAccess` simplifies configuration but is optional.

#### Customer Managed Policy
Create and attach the following custom policies (see the script section for the code):

- `customGGCRPi4BPolicy`
- `customGreengrassProvisionPolicy`
- `customGreengrassS3Access`
- `GreengrassV2TokenExchangeRoleAccess`

Attach these policies to `ggc_group` to enable future updates by adding additional Raspberry Pi devices. Also, attach each policy to all relevant entities (Users, Groups, Roles) within `ggc_group`.

---

### AWS Greengrass Roles

Create the following roles to be attached to the Greengrass Core device to facilitate communication and synchronization with Raspberry Pi 4B. The code is in the script section.

- `GreengrassRole`
- `GreengrassV2TokenExchangeRole`

**Note:** Attach the Greengrass Service Role only after creating the IoT Greengrass Device.

---

### Attach Greengrass Roles

1. Navigate to **AWS IoT > Settings**.
2. Scroll to the “Greengrass service role” section and select **Attach Role**.
3. Attach the previously created `GreengrassRole`.
4. You should now see the Amazon Resource Name (ARN) and the policies attached to the current service role. For example:
   - **Current service role**  
     `arn:aws:iam::012345678901:role/GreengrassRole`
   - **Policies attached to this role**  
     - `customGreengrassProvisionPolicy`
     - `GreengrassV2TokenExchangeRoleAccess`
     - `customGGCRPi4BPolicy`
     - `customGreengrassS3Access`
     - `AWSIoTFullAccess`
     - `AWSGreengrassFullAccess`
     - `IAMFullAccess`
     - `AmazonS3FullAccess`
     - `AWSIoTDeviceTesterForGreengrassFullAccess`

---

### Creating a Thing Resource in AWS IoT

1. Go to **AWS IoT > Connect > Connect one device**.
2. Follow the wizard to create the AWS IoT Greengrass device and connect the Raspberry Pi 4B to the service.

**Resource Names Used:**
- **Thing Name (Core Device):** `GGC1`
- **Thing Group Name:** `GGCGroup`
- **Thing Type:** `RPi4B`

3. After creating the Thing, go to the **Settings** tab and follow the previous instructions on attaching Greengrass service roles.
4. Then, navigate to the **Security > Policies** tab and verify that the following policies are attached to the core device (`GGC1`):
   - `GreengrassV2IoTThingPolicy`
   - `GreengrassTESCertificatePolicyGreengrassV2TokenExchangeRoleAlias` (automatically created by the installation wizard)
   - `GGC-RPi4B-Policy`

5. Upon completing the installation, you should see the following confirmation message:
```bash
    `Successfully configured Nucleus with provisioned resource details!`
    `Configured Nucleus to deploy aws.greengrass.Cli component.`
    `Successfully set up Nucleus as a system service.`
```

---

### Testing Communication

To test communication between the Raspberry Pi 4B device and the AWS Greengrass Core device, run the following command in the Raspberry Pi CLI:

```bash
sudo /greengrass/v2/bin/greengrass-cli component list
```
**Note:** The Greengrass CLI may take up to a minute to deploy. After running the command, you should see a list of the components automatically deployed in the system. If not, please refer to AWS's instructions for [Verifying the Greengrass CLI installation](https://docs.aws.amazon.com/greengrass/v2/developerguide/verify-greengrass-cli.html) on the device.
