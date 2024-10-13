# Week-5-Encryptie

# Stappenplan

# Stap 1: onderzoek
Symmetrische Encryptie
Symmetrische encryptie is een gegevensversleuteling waarbij dezelfde sleutel wordt gebruikt voor het versleutelen en het ontsleutelen van informatie.
Voordelen van symmetrische encryptie:

Het is snel en goed, vooral voor het versleutelen van grote gegevens.
Nadelen:

Als de sleutel wordt onderschept, kan een aanvaller zowel de versleutelde als de ontsleutelde gegevens verkrijgen.

Asymmetrische Encryptie
asymmetrische encryptie heeft maar een paar sleutels: een openbare sleutel en een privésleutel. De openbare sleutel wordt gebruikt om gegevens te versleutelen, terwijl de privésleutel, die geheim moet blijven, wordt gebruikt om de gegevens te ontsleutelen.

Voordelen van asymmetrische encryptie:
Er is geen noodzaak om een geheime sleutel te delen. De openbare sleutel kan veilig worden verspreid, en alleen de ontvanger met de privésleutel kan de gegevens ontsleutelen.

Nadelen
Asymmetrische encryptie is over het algemeen trager dan symmetrische encryptie en is minder geschikt voor het verwerken van grote hoeveelheden gegevens.

# Stap 2: Implenmentatie

installeren van de python omgeving kun je doen door hetvolgende command uit te voeren: pip install -r requirements.txt
Hierna heb ik in het programma gebruik gemaakt van de fernet module.

# Stap 3: Documentatie

Met deze app is het mogelijk om berichten te versleutelen en ontsleutelen door middel van symmetrische encryptie.
ik heb hiervoor gebruik gemaakt van de cryptography bieb in python.
Je kan in deze app:
Sleutel Genereren
Bericht Versleutelen
Bericht Ontsleutelen

Je kan de app gebruiken door de dec.py file te runnen en hierna het menu te volgen.
Zorg wel dat je van te voren de requirements hebt geinstalleerd.
