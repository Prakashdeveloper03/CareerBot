# Firebase Setup and Python Integration

![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![poetry](https://img.shields.io/badge/Firebase-FFA116?logo=firebase&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

In this guide, we'll walk you through setting up a new Firebase project, obtaining the `serviceAccountKey.json`, installing the Firebase Python SDK, and running a Python script to interact with Firebase.

## Firebase Setup

1. **Create a New Firebase Project:**

   - Go to the [Firebase Console](https://console.firebase.google.com/).

   ![Step 1](../markdown/home.png)

   - Click on "Add project" and give a project name, then click on "Continue".

   ![Step 2](../markdown/create-project-1.png)

   - By default, click on "Continue" to enable analytics.

   ![Step 3](../markdown/create-project-2.png)

   - By default, click on "Create Project."

   ![Step 4](../markdown/create-project-3.png)

   - Firebase will allocate resources for our project.

   ![Step 5](../markdown/create-project-4.png)

   - Once it's completed, click on "Continue" to go to the project.

   ![Step 6](../markdown/create-project-5.png)

2. **Add Firebase to Your Web App:**

   - After creating the project, click on "Add app" and select the web platform (</> icon) and follow the instructions.

   ![Step 7](../markdown/project-home.png)

3. **Create Firestore Database:**

   - Create a database by setting the location and click next.

   ![Step 8](../markdown/create-db-1.png)

   - Select "Start in production mode" and click create.

   ![Step 9](../markdown/create-db-2.png)

4. **Get `serviceAccountKey.json`:**

   - Go to Project Settings in the Firebase Console.

   ![Step 10](../markdown/secrets-1.png)

   - Navigate to the "Service accounts" tab.

   ![Step 11](../markdown/secrets-2.png)

   - Scroll down, click on "Generate new private key" to download the `serviceAccountKey.json` file.

   ![Step 12](../markdown/secrets-3.png)

   - Keep this file secure, as it authenticates your application with Firebase services.

## Python Setup

1. **Clone the Repository:**

   ```
   git clone https://github.com/Prakashdeveloper03/CareerBot.git
   ```

2. **Navigate to the Directory:**

   ```
   cd <directory_name>/database
   ```

3. **Install Required Packages:**

   ```
   pip install firebase-admin
   ```

4. **Download `serviceAccountKey.json`:**

   - Follow the steps mentioned in the Firebase Setup section to download `serviceAccountKey.json` and keep it secure.

5. **Update the `serviceAccountKey.json` Path:**

   - Open the `firebase.py` file in the cloned repository.
   - Locate the line `cred = credentials.Certificate("./serviceAccountKey.json")`.
   - Update the path `"./serviceAccountKey.json"` with the path to your downloaded `serviceAccountKey.json` file.
   - Example: `cred = credentials.Certificate("/path/to/your/serviceAccountKey.json")`.

6. **Run the Application:**

   ```
   python firebase.py
   ```

   Once the script is executed, you'll observe progress messages indicating the upload status of CSV files:

   ```bash
   Uploading '../data/courses.csv': 100%|█████████████████████████████████████████████████████████████████████████| 1000/1000 [07:58<00:00,  2.09it/s]
   CSV file '../data/courses.csv' successfully uploaded to the Firestore collection 'courses'!

   Uploading '../data/keywords.csv': 100%|██████████████████████████████████████████████████████████████████████████| 130/130 [00:51<00:00,  2.50it/s]
   CSV file '../data/keywords.csv' successfully uploaded to the Firestore collection 'skills'!
   ```

   After the upload completes, refresh the database page to view the updated collections.

   ![Database Output](../markdown/output.png)
