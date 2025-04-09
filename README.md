# CMSC447-Proj: Interactive 4-Year Plan Project

This website provides students with a tool to customize their graduation plan for a specific major.

After the student selects a major from the dropdown, courses populate into the planner.

Click on a course to view more information.

Drag and drop courses to move them to another semester or session.

To run the website:

1. Set up and run the Flask server

2. Set up and run the React app

3. Go to http://localhost:5173/ 

## Prerequisites

1. A modern web browser (e.g., Chrome, Firefox, or Edge)

2. Ability to install and use git for the command line steps

# Running the Webpage

- First clone the git repository by running this command
```sh
git clone https://github.com/avidonaty1/CMSC447-Proj.git

```

# Backend Setup

Navigate to the backend folder

**Note that once everything is created/installed, you only need to do steps 3 and 5 to start the server**

1. Run this command to install virtual environment for Python
```bash
pip install virtualenv
```

2. Run this command to create a virtual environment
```bash
virtualenv planner-env
```

3. Activate the virtual environment (Windows)
```bash
planner-env\Scripts\activate
```

OR Activate the virtual environment (mac/Linux)
```bash
source planner-env/bin/activate
```

4. Run this command to install dependencies
```bash
pip install -r requirements.txt
```

5. Run this command to start the Flask server
```bash
python server.py
```

# Frontend Setup

**Note that once everything is created/installed, you only need to do steps 3, 4, and 5 to start the frontend**

1. Before you start, ensure you have Node.js and npm (Node Package Manager) installed on your machine. You can check by running:

```bash
node -v
npm -v
```

If you don't have them you can download them here: https://nodejs.org/en

2. Then install dependencies 

```bash
npm install

```

3. Navigate to the react folder

```bash
cd frontend
cd my-react-app
```


4. Start the frontend

```bash
npm run dev
```


5. Use the link provided to run. It will look something like:
http://localhost:5173/ 


## Troubleshooting

If the page does not load properly, ensure that the file paths are correct.
Clear the browser cache if style updates are not reflecting.

### Additional Information

Refer to initial-setup.txt for further setup instructions or additional configuration details.


## Contact

For questions or contributions, please contact: 
- David Ni: davidn4@umbc.edu
- Julia Ciattei: jcia1@umbc.edu
- Avi Donaty: adonaty1@umbc.edu
- Chris Dollo: cdollo1@umbc.edu





