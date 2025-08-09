# 🌍 Travel Journal

**Travel Journal** is a Django-based web app that lets travelers **plan, document, and share their trips**.  
Users can create trips, add journal entries with photos, browse public adventures, and connect through likes.

---

## ✨ Features

- 🗺 **Trips** – Create, edit, and manage your travel itineraries  
- 📓 **Journal Entries** – Record your travel memories with stories & multiple photos  
- 📸 **Photo Uploads** – Add trip covers and gallery images for each journal entry  
- ❤️ **Likes System** – Show appreciation for inspiring trips  
- 🌐 **Public & Private Trips** – Share with everyone or keep them personal  
- 🔍 **Search** – Filter public trips instantly without reloading the page  
- 🎯 **Featured Trips** – See 4 random public trips each session on the landing page  

---

## 🚀 Tech Stack

- **Backend**: Django + Django REST Framework  
- **Frontend**: Django Templates + JavaScript (AJAX)  
- **Database**: PostgreSQL  
- **Media Storage**: Local
- **Authentication**: Custom User Model  

---

## 📸 Screenshots

| Landing Page | Trip Details | Journal Entry |
|--------------|--------------|---------------|
| ![Landing Page](docs/screenshots/landing.jpg) | ![Trip Details](docs/screenshots/trip_details.jpg) | ![Journal Entry](docs/screenshots/journal_entry.jpg) |

---

## 🛠 Installation

```bash
# 1. Clone the repo
git clone https://github.com/AngEvd/TravelJournal.git
cd travel-journal

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```
---

### 🔑 Environment Variables

#### Create a .env file with:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
```
---

### 📡 API Endpoints

| Method | Endpoint              | Description                          |
|--------|-----------------------|------------------------------------|
| GET    | /trips/public-trips/  | List all public trips               |
| GET    | /trips/featured-trips/| Get 4 random public trips for session |

---

### 🎯 Usage

-	📝 Register & Login** – Create an account or log in to start using the app
-	🗺️ Create Trips – Plan your travel itineraries with detailed info
-	📓 Add Journal Entries – Document your experiences with stories and photos
-	🔍 Search Trips – Instantly filter public trips by keywords without page reload
-	❤️ Like Trips – Show appreciation for trips you enjoy
-	🌟 Explore Featured Trips – Get inspired by random highlights on the landing page

___

### 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements or fixes
- Suggest new features or enhancements

Please fork the repo and create your feature branch before submitting a PR.

---

### 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.