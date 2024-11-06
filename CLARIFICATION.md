## Clarification

I cannot directly access the client’s actual POS system or Raspberry Pi 4B devices, as the client is based in another country. The client’s POS system generates a CSV sales report file at each POS endpoint. This file is intended to be uploaded and synchronized to the cloud whenever network connectivity is available. The client’s accountant, located in a different region within the client’s home country, requires access to these files to aggregate and centralize data across all POS endpoints.

To simulate the client’s environment and functionality, I developed a Python script (`s3_test1.py`) to mimic the creation, updating, and cloud uploads of the client’s POS CSV files. This program uses AWS IoT Greengrass V2 and a Raspberry Pi 4B core device to simulate network connectivity interruptions and to replicate the client’s requirements for seamless data synchronization between local POS devices and the cloud.
