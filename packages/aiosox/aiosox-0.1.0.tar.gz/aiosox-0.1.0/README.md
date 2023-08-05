
hypercorn main:app --worker-class trio --reload

poetry config repositories.aiosox https://pypi.example.org/legacy/
