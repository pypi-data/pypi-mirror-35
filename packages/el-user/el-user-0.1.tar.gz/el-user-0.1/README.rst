=====
Data Karyawan
=====

Data karyawan adalah aplikasi berbasis web yang menghandle
pembuatan user. Aplikasi ini juga mengirimkan email notifikasi
kepada user baru untuk aktivasi akun serta merubah password.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "datakaryawan" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'datakaryawan',
    ]

2. Include the datakaryawan URLconf in your project urls.py like this::

    path('datakaryawan/', include('datakaryawan.urls')),

3. Run `python manage.py migrate` to create the datakaryawan models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a datakaryawan (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/datakaryawan/ untuk mulai menggunakan aplikasi data karyawan.