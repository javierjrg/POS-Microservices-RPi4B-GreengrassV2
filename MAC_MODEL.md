# Project MAC Model

---

## Motivation

This project addresses the performance, reliability, and latency issues currently faced by a client’s Point of Sale (POS) system, especially during server outages. Frequent performance slowdowns and data synchronization delays hinder operational efficiency, impacting customer experience. By deploying a cloud-native microservices architecture locally on a Raspberry Pi with AWS Greengrass V2, the project aims to:

1. **Enable Offline Functionality:** Allow POS devices to operate independently of the cloud, ensuring continuous operation during server or network outages.
2. **Enhance Data Synchronization:** Facilitate seamless data transfer from local devices to the cloud when connectivity is available, maintaining data integrity and operational flow.
3. **Reduce Latency and Improve Speed:** Localize critical microservices, minimizing communication delays between POS devices and backend systems, which improves response times and overall system speed.
4. **Boost System Reliability and Security:** Implement secure data processing and ensure POS devices operate without disruption, meeting the growing demands of high-traffic retail environments and providing a better customer experience.

The ultimate goal is to create a robust, scalable, and efficient cloud synchronization solution capable of operating reliably in environments with intermittent internet connectivity, thereby significantly improving performance and customer satisfaction.

---

## Architecture

This project leverages AWS Greengrass V2 to deploy a cloud-native microservices architecture on a Raspberry Pi 4B, enabling seamless offline operations for POS devices. The architecture consists of the following key components:

1. **Raspberry Pi 4B:** Acts as the local processing hub, running AWS Greengrass and hosting microservices that enable POS operations even during network outages.
2. **AWS Greengrass V2:** Facilitates the deployment of microservices locally on the Raspberry Pi, ensuring that data processing can occur independently of cloud connectivity. It also manages secure communication between local devices and the cloud.
3. **Local Microservices:** These services, including the `s3_test1.py` script, handle POS transactions, update the `test.csv` file with transaction data, and synchronize with the cloud once internet connectivity is restored.
4. **Data Synchronization:** When the Raspberry Pi 4B regains internet access, it automatically uploads locally stored data to a specified S3 bucket, ensuring all transactions are recorded for further analysis or reporting.
5. **Cloud Integration:** Although only partially utilized at this stage, the architecture is designed to easily integrate with AWS services (like DynamoDB) for future data storage and analytics capabilities.

This architecture enables improved reliability, reduced latency, and secure local processing, providing a robust solution for POS operations in environments with unstable internet connectivity.

---

## Challenges

### 1. AWS Documentation Gaps and Unclear Instructions
- **Issue:** The AWS documentation for IoT Greengrass V2 contains gaps or unclear instructions. For example, in the section *AWS > Documentation > AWS IoT Greengrass > Developer Guide, Version 2 > Develop a Hello World component*, step 12 mentions updating the component’s configuration parameters, but it does not specify that the JSON file name must include “-config-update” to function correctly. This lack of clarity initially caused deployment errors labeled as “Broken” in the console.
- **Solution:** After troubleshooting various naming conventions, I discovered that adding “-config-update” to the JSON file name resolved the issue. This knowledge was validated by testing with multiple naming conventions to confirm the required keywords for the file to work correctly.

### 2. Local AWS Greengrass Core Permissions Errors
- **Issue:** After removing the “Hello World” component from the Raspberry Pi 4B core device, I encountered permissions errors when deploying project-specific components. The errors included:
  - `[WARN] (Copier) com.example.test: stderr. python3: can’t open file’/greengrass/v2/packages/artifacts/com.example.test/1.0.0/test.py’: [Errno 13] Permission denied.`
  - `ls: cannot access’/greengrass/v2/packages/artifacts/com.example.test/1.0.0/test.py’: No such file or directory`
- **Solution:** Initial troubleshooting verified that all cloud and local permissions were correctly set; however, the error persisted. After researching similar cases and consulting AWS and community sources, I could not find a solution. However, I resolved the issue by adding the Raspberry Pi user (`ggc`) to the `ggc_group` created during the Greengrass installation. Adding the user to this group and restarting the system resolved the permissions errors. Reverting the user-group assignment caused the errors to reappear, confirming that group assignment was the solution.
