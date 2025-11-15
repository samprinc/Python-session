# Church API – Django REST Framework

This project provides a clean and structured REST API for managing church-related content such as sermons, events, ministries, homepage content, and livestreams. Built with Django and Django REST Framework (DRF), it exposes reliable endpoints suitable for any frontend, including React.

---

## 🚀 Features

* CRUD operations for:

  * Sermons
  * Events
  * Ministries
  * Homepage Content
  * Livestreams
* Uses DRF `ModelViewSet` for clean, RESTful endpoints
* Backend ready for integration with web/mobile frontends
* Organized models, serializers, and viewsets

---

## 📂 API Viewsets

The main API viewsets are defined as follows:

```python
from rest_framework import viewsets
from .models import Sermon, Event, Ministry, HomepageContent, Livestream
from .serializers import (
    SermonSerializer, EventSerializer, MinistrySerializer,
    HomepageContentSerializer, LivestreamSerializer
)

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer

class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

class HomepageContentViewSet(viewsets.ModelViewSet):
    queryset = HomepageContent.objects.all()
    serializer_class = HomepageContentSerializer

class LivestreamViewSet(viewsets.ModelViewSet):
    queryset = Livestream.objects.all()
    serializer_class = LivestreamSerializer
```

---

## 🔌 API Endpoints

| Resource         | Endpoint             | Description                |
| ---------------- | -------------------- | -------------------------- |
| Sermons          | `/api/sermons/`      | List / Create              |
| Sermon Detail    | `/api/sermons/<id>/` | Retrieve / Update / Delete |
| Events           | `/api/events/`       | List / Create              |
| Ministries       | `/api/ministries/`   | List / Create              |
| Homepage Content | `/api/homepage/`     | Manage homepage content    |
| Livestream       | `/api/livestream/`   | Manage livestream data     |

---

## ⚙️ Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/samprinc/Python-session.git
cd Test
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Start development server

```bash
python manage.py runserver
```

---

## 🧪 Testing the API

Example: Fetch sermons

```http
GET http://localhost:8000/api/sermons/
```

Example: Create an event

```http
POST http://localhost:8000/api/events/
```

---

## 🤝 Contributing

Pull requests are welcome! If you need help connecting this API to a React frontend, feel free to ask.

---

## 📜 License

This project is for educational and ministry use. Modify and extend freely.
