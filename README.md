### codicefiscale-python

******

**Uso:**

```python
import codicefiscale

cf = codicefiscale.GeneraCodiceFiscale(cognome, nome, data, sesso, citta)
```

**Esempio:**

```python
import codicefiscale

cf = codicefiscale.GeneraCodiceFiscale("Rossi", "Mario", "15/06/1998", "M", "Roma")
```

*******

**Funzioni:**

- **GeneraCodiceFiscale**(cognome, nome, data, sesso, citta) ---> Ritorna un codice fiscale completo
- **GetSurname**(cognome) ---> Ritorna le tre lettere del cognome che compongono il codice fiscale
- **GetName**(nome) ---> Ritorna le tre lettere del nome che compongono il codice fiscale
- **GetBirthday**(data, sesso) ---> Ritorna una tupla contenente i caratteri dell'anno di nascita, del mese di nascita, e della composizione *giorno di nascita + sesso*
- **GetCityCode**(citta) ---> Ritorna il codice appartenente alla città
- **GetControlCode**(codicefiscale_incompleto) ---> Ritorna il codice di controllo calcolato con il preciso calcolo sul codice fiscale non completo(15 caratteri)

****

**Note:**

- La data di nascita deve essere passata tramite il formato **dd/mm/YYYY**