\# 💱 Currency Converter API



A Django REST Framework API for real-time currency conversion with multiple free API fallbacks and database storage.



\## 🌟 Features



\- \*\*Real-time Exchange Rates\*\* from multiple free APIs

\- \*\*Multiple API Fallbacks\*\* (Frankfurter, ExchangeRate-API, FastForex)

\- \*\*Database Storage\*\* for conversion history

\- \*\*REST API Endpoints\*\* for conversion and history retrieval

\- \*\*Django Admin Interface\*\* for managing conversions

\- \*\*Mock Data Fallback\*\* when external APIs are unavailable



\## 🚀 Quick Start



\### Prerequisites

\- Python 3.8+

\- Django 5.2

\- Django REST Framework



\### Installation Steps



\#### 1. Clone the Repository

```bash

git clone https://github.com/preetham2203/currency-converter-api.git

cd currency-converter-api

2\. Create Virtual Environment

bash

\# Create virtual environment

python -m venv env



\# Activate virtual environment

\# Windows:

env\\Scripts\\activate

\# Mac/Linux:

source env/bin/activate

3\. Install Dependencies

bash

pip install -r requirements.txt

4\. Database Setup

bash

\# Run migrations

cd calculator\_api

python manage.py makemigrations

python manage.py migrate



\# Create superuser (optional)

python manage.py createsuperuser

5\. Run Development Server

bash

python manage.py runserver

Visit: http://127.0.0.1:8000/



📡 API Endpoints

Convert Currency

POST /api/convert/



json

{

&nbsp;   "from\_currency": "USD",

&nbsp;   "to\_currency": "EUR",

&nbsp;   "amount": 100

}

Get Conversion History

GET /api/history/



Get Specific Conversion

GET /api/history/{conversion\_id}/



🛠️ Project Structure

text

currency-converter-api/

├── calculator\_api/          # Django project

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── api/                     # Django app

│   ├── models.py           # CurrencyConversion model

│   ├── views.py            # API views

│   ├── serializers.py      # DRF serializers

│   ├── urls.py             # App URLs

│   └── admin.py            # Django admin

├── requirements.txt         # Python dependencies

├── .gitignore              # Git ignore rules

└── README.md               # This file

💾 Database Models

CurrencyConversion

from\_currency - Source currency code (3 chars)



to\_currency - Target currency code (3 chars)



amount - Amount to convert



exchange\_rate - Rate used for conversion



result - Converted amount



success - Conversion status



created\_at - Timestamp



🔧 API Providers Used

Frankfurter - Primary API



ExchangeRate-API - Fallback 1



FastForex - Fallback 2 (Demo)



Mock Data - Final fallback



🎯 Usage Examples

Convert USD to EUR

bash

curl -X POST http://127.0.0.1:8000/api/convert/ \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{"from\_currency": "USD", "to\_currency": "EUR", "amount": 100}'

Get Conversion History

bash

curl http://127.0.0.1:8000/api/history/

👨‍💻 Development

Running Tests

bash

python manage.py test

Access Admin Panel

Run server: python manage.py runserver



Visit: http://127.0.0.1:8000/admin/



Login with superuser credentials



Adding New API Providers

Edit api/views.py and add new API configurations to the free\_apis list.



📝 Git Commands Used

Initial Setup

bash

\# Initialize git

git init



\# Create .gitignore and requirements.txt

\# (See files in repository)



\# Add files to git

git add .



\# Initial commit

git commit -m "feat: Add Django Currency Conversion API"



\# Connect to GitHub

git remote add origin https://github.com/preetham2203/currency-converter-api.git

git branch -M main

git push -u origin main

Subsequent Updates

bash

\# Add changes

git add .



\# Commit changes

git commit -m "Description of changes"



\# Push to GitHub

git push origin main

🤝 Contributing

Fork the repository



Create a feature branch



Make your changes



Submit a pull request



📄 License

This project is open source and available under the MIT License.



Developer: Preetham

