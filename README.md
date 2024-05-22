# retake

# Create a virtual environment named 'myvenv'
python -m venv myvenv

# Activate the virtual environment (Windows)
myvenv\Scripts\activate

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Backend activation: Start the Django development server
python manage.py runserver

# Frontend activation: Start the frontend development server
npm run dev
