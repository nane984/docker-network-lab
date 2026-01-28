# Koristimo minimalnu Python sliku (manji attack surface)
FROM python:3.11-slim

# -------------------------------
# Python runtime optimizacije
# -------------------------------

# Ne pravi .pyc fajlove (čistiji container)
ENV PYTHONDONTWRITEBYTECODE=1

# Logovi idu direktno na stdout/stderr (bitno za Docker logs)
ENV PYTHONUNBUFFERED=1

# -------------------------------
# Kreiranje non-root usera
# -------------------------------

# Kreiramo sistemsku grupu i usera "django"
# --system = nema login shell, manja prava
RUN addgroup --system django && adduser --system --ingroup django django

# -------------------------------
# Radni direktorijum aplikacije
# -------------------------------

WORKDIR /app

# -------------------------------
# Instalacija Python dependencija (ovo mora kao root)
# -------------------------------

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Kopiranje aplikacionog koda
# -------------------------------

COPY . .

# -------------------------------
# Permissions
# -------------------------------

# Dajemo vlasništvo nad /app direktorijumom django useru
# Ovo je KLJUČNO da bi non-root user mogao da:
# - čita kod
# - piše static fajlove
# - piše logove (ako ih ima)
RUN chown -R django:django /app

# -------------------------------
# Django static files
# -------------------------------

# collectstatic mora da ima prava pisanja → zato ide PRE USER django
RUN python manage.py collectstatic --noinput

# -------------------------------
# Prelazak na non-root user
# -------------------------------

# Od ovog trenutka SVE se izvršava kao "django", ne kao root
USER django

# -------------------------------
# Pokretanje aplikacije
# -------------------------------

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]