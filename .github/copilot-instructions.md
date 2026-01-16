# GitHub Copilot Instructions for OctoFit Tracker

## Project Overview

**OctoFit Tracker** is a fitness tracking application built with a **Django REST backend** (Python), **React frontend** (Node.js), and **MongoDB database**. The app enables students to log workouts, compete on leaderboards, earn badges, and access personalized fitness suggestions.

## Architecture & Key Components

### Tech Stack
- **Frontend**: React.js with Bootstrap (port 3000)
- **Backend**: Django REST Framework (port 8000)
- **Database**: MongoDB with Djongo ORM (port 27017)
- **Environment**: GitHub Codespaces with Docker support

### Project Structure
```
octofit-tracker/
├── backend/
│   ├── venv/               # Python virtual environment
│   ├── octofit_tracker/    # Django project
│   └── requirements.txt
└── frontend/               # React app (created via create-react-app)
```

### Key Port Configuration
- **3000** (public): React development server
- **8000** (public): Django API server
- **27017** (private): MongoDB local connection

## Critical Development Workflows

### Backend Setup
```bash
# Create virtual environment
python3 -m venv octofit-tracker/backend/venv

# Activate and install dependencies
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

### Frontend Setup
```bash
# Install with Bootstrap and React Router
npm install bootstrap --prefix octofit-tracker/frontend
npm install react-router-dom --prefix octofit-tracker/frontend
# Bootstrap CSS must be imported at top of src/index.js
```

### MongoDB Check
```bash
ps aux | grep mongod  # Always use this to verify MongoDB is running
```

## Important Conventions & Constraints

### Command Execution Rule
**Never change directories when running commands.** Instead, always specify the directory in the command. Example:
```bash
pip install -r octofit-tracker/backend/requirements.txt  # ✓ Correct
source octofit-tracker/backend/venv/bin/activate
```

### Django Backend Specifics
- **ALLOWED_HOSTS**: Include `localhost`, `127.0.0.1`, and Codespace domain when available
- **Serializers**: Convert MongoDB ObjectId fields to strings for API responses
- **API Testing**: Use `curl` to test REST endpoints
- **URL Configuration**: Dynamically detect Codespace environment for base URLs

See [octofit_tracker_django_backend.instructions.md](./instructions/octofit_tracker_django_backend.instructions.md) for detailed backend guidelines.

### React Frontend Specifics
- **Setup**: Use `create-react-app` with `--use-npm` flag
- **Bootstrap CSS**: Import at the very top of `src/index.js`
- **Routing**: Use `react-router-dom` for navigation
- **Branding**: Reference `docs/octofitapp-small.png` for app logo/imagery

See [octofit_tracker_react_frontend.instructions.md](./instructions/octofit_tracker_react_frontend.instructions.md) for detailed frontend guidelines.

## Data Flow & Integration Points

### Backend → Frontend
- Django REST API exposes `/api/` endpoints for React consumption
- Codespace domain auto-detection ensures frontend points to correct API URL
- CORS headers (`django-cors-headers`) enable cross-origin requests

### Database Integration
- Django uses **Djongo** to bridge Django ORM with MongoDB
- `django-allauth` handles user authentication
- `dj-rest-auth` provides REST endpoints for auth flows

## Django Core Dependencies
- `Django==4.1.7` + `djangorestframework==3.14.0`
- `django-allauth==0.51.0` + `dj-rest-auth==2.2.6` for authentication
- `djongo==1.3.6` + `pymongo==3.12` for MongoDB integration
- `django-cors-headers==4.5.0` for frontend communication

## Development Patterns

### When Adding Features
1. Create Django models/serializers in backend first
2. Expose via REST endpoints at `/api/`
3. Build React components in frontend to consume endpoints
4. Always test backend endpoints with `curl` before frontend integration

### When Debugging
- Check MongoDB is running: `ps aux | grep mongod`
- Verify Django server: `http://localhost:8000` or Codespace domain
- React dev server: `http://localhost:3000`
- Use browser DevTools for frontend issues, Django logs for backend

## For Questions About Specific Sections
Refer to the structured instruction files in `.github/instructions/`:
- General setup & architecture → `octofit_tracker_setup_project.instructions.md`
- Backend implementation details → `octofit_tracker_django_backend.instructions.md`
- Frontend implementation details → `octofit_tracker_react_frontend.instructions.md`
