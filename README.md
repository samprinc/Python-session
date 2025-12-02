# 🏛️ Church Platform - Full Stack Project

> A complete church management system with Django REST API backend and React frontend for managing sermons, events, ministries, livestreams, and more.

---

## 🌟 Project Overview

This is a **real-world full-stack application** designed for church administration. It demonstrates the complete flow from backend API development to frontend integration, perfect for learning modern web development practices.

**What makes this special:**
- ✅ Production-ready Django REST API
- ✅ Modern React frontend with hooks
- ✅ Real CRUD operations (Create, Read, Update, Delete)
- ✅ File upload support (audio files, images)
- ✅ Clean architecture with separation of concerns
- ✅ Perfect for portfolio projects!

---

## 🚀 Features

### Backend (Django REST Framework)
* **Sermons Management** - Upload sermons with audio files, videos, and notes
* **Events Calendar** - Manage church events with dates, times, and locations
* **Ministries Directory** - Track ministry leaders and descriptions
* **Homepage Content** - Dynamic welcome messages and about sections
* **Livestream Integration** - Manage YouTube/Facebook livestream URLs

### Frontend (React)
* **Interactive Dashboard** - User-friendly interface for all operations
* **Real-time Updates** - Instant feedback on all actions
* **Form Validation** - Client-side validation for better UX
* **Responsive Design** - Works on desktop, tablet, and mobile
* **Component-Based Architecture** - Reusable, maintainable code

---

## 📂 Project Structure

```
church-project/
│
├── backend/                    # Django REST API
│   ├── api/
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # DRF serializers
│   │   ├── views.py           # API viewsets
│   │   └── urls.py            # API routes
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/                   # React Application
    ├── public/
    ├── src/
    │   ├── components/        # React components
    │   │   ├── SermonList.js
    │   │   ├── SermonForm.js
    │   │   ├── EventList.js
    │   │   ├── EventForm.js
    │   │   ├── MinistryList.js
    │   │   └── Navbar.js
    │   ├── services/
    │   │   └── api.js         # Axios API calls
    │   ├── App.js
    │   └── App.css
    └── package.json
```

---

## 🔌 API Endpoints

### Base URL: `http://localhost:8000/api/`

| Resource         | Endpoint                  | Methods           | Description                    |
|------------------|---------------------------|-------------------|--------------------------------|
| Sermons          | `/sermons/`               | GET, POST         | List all / Create new sermon   |
| Sermon Detail    | `/sermons/<id>/`          | GET, PUT, DELETE  | View / Update / Delete sermon  |
| Sermon Categories| `/sermoncategories/`      | GET, POST         | Manage sermon categories       |
| Events           | `/events/`                | GET, POST         | List all / Create new event    |
| Event Detail     | `/events/<id>/`           | GET, PUT, DELETE  | View / Update / Delete event   |
| Ministries       | `/ministries/`            | GET, POST         | List all / Create new ministry |
| Ministry Detail  | `/ministries/<id>/`       | GET, PUT, DELETE  | View / Update / Delete ministry|
| Homepage Content | `/homepage/`              | GET, PUT          | Manage homepage content        |
| Livestreams      | `/livestreams/`           | GET, POST         | Manage livestream URLs         |

### Example API Response (Sermon)
```json
{
  "id": 1,
  "title": "Faith and Hope",
  "preacher": "Pastor John",
  "category": "Sunday Service",
  "date": "2025-12-21",
  "video_url": "https://youtube.com/...",
  "audio_file": "/media/sermons/audio.mp3",
  "notes": "Sermon notes here..."
}
```

---

## ⚙️ Backend Setup (Django)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/samprinc/Python-session.git
cd Python-session/Test
```

### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run Development Server
```bash
python manage.py runserver
```

✅ Backend now running at: `http://localhost:8000`

### 7️⃣ Test API with Postman
- Open Postman
- Test GET: `http://localhost:8000/api/sermons/`
- Test POST with JSON body:
```json
{
  "title": "Test Sermon",
  "preacher": "Pastor Jane",
  "date": "2025-12-25"
}
```

---

## 🎨 Frontend Setup (React)

### 1️⃣ Create React App
```bash
npx create-react-app church-frontend
cd church-frontend
```

### 2️⃣ Install Axios
```bash
npm install axios
```

### 3️⃣ Create API Service Layer

**File: `src/services/api.js`**
```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

// Sermons
export const getSermons = () => axios.get(`${API_URL}sermons/`);
export const createSermon = (data) => axios.post(`${API_URL}sermons/`, data);
export const updateSermon = (id, data) => axios.put(`${API_URL}sermons/${id}/`, data);
export const deleteSermon = (id) => axios.delete(`${API_URL}sermons/${id}/`);

// Events
export const getEvents = () => axios.get(`${API_URL}events/`);
export const createEvent = (data) => axios.post(`${API_URL}events/`, data);
export const deleteEvent = (id) => axios.delete(`${API_URL}events/${id}/`);

// Ministries
export const getMinistries = () => axios.get(`${API_URL}ministries/`);
export const createMinistry = (data) => axios.post(`${API_URL}ministries/`, data);
export const deleteMinistry = (id) => axios.delete(`${API_URL}ministries/${id}/`);

// Livestreams
export const getLivestreams = () => axios.get(`${API_URL}livestreams/`);
export const createLivestream = (data) => axios.post(`${API_URL}livestreams/`, data);
```

### 4️⃣ Example Component - SermonList

**File: `src/components/SermonList.js`**
```javascript
import React, { useState, useEffect } from 'react';
import { getSermons, deleteSermon } from '../services/api';

const SermonList = () => {
  const [sermons, setSermons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchSermons();
  }, []);

  const fetchSermons = async () => {
    try {
      setLoading(true);
      const response = await getSermons();
      setSermons(response.data);
      setError('');
    } catch (err) {
      setError('Failed to fetch sermons');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Delete this sermon?')) {
      try {
        await deleteSermon(id);
        fetchSermons(); // Refresh list
      } catch (err) {
        alert('Failed to delete sermon');
      }
    }
  };

  if (loading) return <div>Loading sermons...</div>;
  if (error) return <div style={{color: 'red'}}>{error}</div>;

  return (
    <div className="sermon-list">
      <h2>📖 Sermons</h2>
      {sermons.length === 0 ? (
        <p>No sermons yet. Add your first one!</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Title</th>
              <th>Preacher</th>
              <th>Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {sermons.map(sermon => (
              <tr key={sermon.id}>
                <td>{sermon.title}</td>
                <td>{sermon.preacher}</td>
                <td>{new Date(sermon.date).toLocaleDateString()}</td>
                <td>
                  <button onClick={() => handleDelete(sermon.id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default SermonList;
```

### 5️⃣ Run React App
```bash
npm start
```

✅ Frontend now running at: `http://localhost:3000`

---

## 🛠️ Common Issues & Solutions

### CORS Error?
Install django-cors-headers:
```bash
pip install django-cors-headers
```

Add to `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### File Upload Not Working?
Ensure your Django settings include:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📝 Assignment Checklist

### Backend Tasks
- [ ] All models created and migrated
- [ ] Serializers implemented
- [ ] ViewSets configured
- [ ] URLs registered
- [ ] CORS configured
- [ ] Tested all endpoints in Postman

### Frontend Tasks
- [ ] React app created
- [ ] Axios installed
- [ ] API service layer created
- [ ] SermonList component working
- [ ] SermonForm component working
- [ ] EventList component working
- [ ] MinistryList component working
- [ ] LivestreamList component working
- [ ] Basic styling applied
- [ ] Error handling implemented

### Submission Requirements
- [ ] GitHub repository with both backend and frontend
- [ ] README with setup instructions
- [ ] Demo video (3-5 minutes)
- [ ] Code is clean and commented

---

## 🎥 Demo Video Requirements

Your 3-5 minute video should show:
1. **Starting both servers** (Django + React)
2. **Listing data** from at least 3 different resources
3. **Adding a new item** (e.g., new sermon)
4. **Updating an item**
5. **Deleting an item**
6. **Code walkthrough** of your API service layer
7. **Brief explanation** of how React communicates with Django

---

## 💡 Pro Tips

1. **Start Simple** - Get one resource working completely before moving to others
2. **Test Backend First** - Always test your API in Postman before connecting React
3. **Use Console.log** - Debug API responses with `console.log(response.data)`
4. **Handle Errors** - Always use try-catch blocks for API calls
5. **Keep It DRY** - Reuse components and functions where possible
6. **Commit Often** - Make small, meaningful Git commits as you progress

---

## 🎯 Bonus Challenges (Optional)

Want to go above and beyond? Try these:

- [ ] Add search/filter functionality
- [ ] Implement pagination for long lists
- [ ] Add loading spinners and animations
- [ ] Create a dashboard with statistics
- [ ] Add user authentication (JWT)
- [ ] Deploy to Heroku/Vercel
- [ ] Add dark mode toggle
- [ ] Implement drag-and-drop for reordering

---

## 🤝 Getting Help

**Stuck? Here's what to do:**

1. **Check the console** - Most errors show up in browser/terminal console
2. **Read the error message** - Django and React give helpful error messages
3. **Google the error** - Copy-paste the error into Google
4. **Ask for help** - Reach out with specific error messages and what you tried

---

## 📚 Learning Resources

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Axios Documentation](https://axios-http.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## 📜 License

This project is for educational and ministry use. Feel free to modify and extend it for your church or learning purposes.

---

## 🎉 Final Words

**Congratulations on building your first full-stack application!** 

This project demonstrates real-world skills that companies look for:
- RESTful API design
- Frontend-backend integration
- State management
- Error handling
- Clean code architecture

Keep building, keep learning, and remember: **every expert was once a beginner!** 💪

---

**Project Deadline:** Friday, 26th December 2025  
**Questions?** Open an issue on GitHub or reach out directly!

Happy Coding! 🚀⛪