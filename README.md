# CMSC447-Proj: Interactive 4-Year Plan Project


**Note that once everything is created/installed, you only need to do steps 3 and 5 to start the server**

# Frontend Setup

Before you start ensure you have Node.js and npm (Node Package Manager installed on your machine. You can check by running:

```bash
node -v
npm -v
```

If you don't have them you can download them here: https://nodejs.org/en

Then install vite

```bash
npm install vite --save-dev
```


Navigate to the react folder

```bash
cd frontend
cd my-react-app
```


# To run the whole website (assuming the Flask server is running)

```bash
npm run dev
```


npm install react-beautiful-dnd


use the link provded to run. it will look something like:
http://localhost:5173/ 







# Backend Setup

Navigate to the backend folder

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





This project is an early-stage implementation of an interactive 4-year planner for students, allowing them to drag and drop classes into a scheduler. The static webpage consists of an index.html file and a style.css file. The interface includes a search bar, blocks holding the names of classes on one side, and a scheduler on the other side.

## Prerequisites

A modern web browser (e.g., Chrome, Firefox, or Edge)

## Running the Webpage

- First clone the git repository by running this command
```sh
git clone https://github.com/avidonaty1/CMSC447-Proj.git
```

- Navigate to the project directory:

```sh
cd CMSC447-Proj
cd frontend
```

- Open the HTML file: Double-click on index.html or right-click and select Open with to choose your browser.


## Customization

To modify the styling, edit style.css.

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





