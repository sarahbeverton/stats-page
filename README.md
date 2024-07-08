# OSoMe Stats Page

The OSoMe Stats Page uses [Django](https://www.djangoproject.com/) for the backend and [Vue 3](https://v3.vuejs.org/) with [Vite](https://vitejs.dev/) for the frontend.

## Prerequisites

- [Node.js](https://nodejs.org/en/download/)
- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Installation

### Clone the Repository

```
git clone https://github.com/sarahbeverton/stats-page.git
cd stats-page
```

### Frontend Setup (Vue3/Vite)

1. Navigate to the frontend directory:
```
cd frontend
```
2. Install the dependencies:
```
npm install
```
3. To serve the frontend locally using Vite, run:
```
npm run dev
```
This will start the development server and you can access the application at http://localhost:5173.

4. To build the project for production, run:
```
npm run build
```
The build output will be in the 'dist/' directory.

### Backend Setup (Django)

1. Navigate to the backend directory:
```
cd backend
```
2. Create and activate the Conda environment:
```
conda env create -p ./<myvenv> -f environment.yml
conda activate ./<myenv>
```
This creates and activates a venv at /path/to/project/<myvenv>

3. Apply the database migrations -
in the same directory where manage.py is located, run:
```
python manage.py migrate
```
4. Create a superuser:
```
python manage.py createsuperuser
```
This will create a superuser and can be used to log in to the application.

5. Run the development server:
```
python manage.py runserver
```
The backend will be available at http://localhost:8000.
