# Recap of Files and New Features in `monetization_features` Branch

## urls.py
This file defines the URL patterns for the Movie Ranker application. It includes:
- The main movie list view (`movie_list`).
- The home view (`home`).
- The user profile view (`user_profile`).
- The subscription view (`subscribe`).
- The movie details view (`movie_details`).

New Features:
- Added URL patterns for the new views related to monetization features.

## movie_list.html
This HTML file represents the main page for viewing movies filtered by genre. It includes:
- A form for selecting the genre.
- A list of filtered movies.
- A section for sponsored movies.
- An ad banner that changes based on the selected genre.
- If there are no movies for the selected genre, an appropriate message is displayed.

New Features:
- Added affiliate links for movies.
- Added a section for sponsored movies.
- Added dynamic ad banners based on the selected genre.

## user_profile.html
This HTML file represents the user profile page for the Movie Ranker application. It includes:
- A welcome message displaying the username of the logged-in user.
- A section promoting the premium subscription.
- A form that allows the user to subscribe to the premium service.

New Features:
- Added a section for premium subscription.
- Added a form to handle premium subscription.

## home.html
This HTML file represents the home page for the Movie Ranker application. It includes:
- Navigation links to other pages.
- A form for selecting the genre.
- A list of filtered movies.
- A section for sponsored movies.
- An ad banner that changes based on the selected genre.

New Features:
- Added navigation links to user profile and subscription pages.
- Added affiliate links for movies.
- Added a section for sponsored movies.
- Added dynamic ad banners based on the selected genre.

## subscribe.html
This HTML file represents the subscription page for the Movie Ranker application. It includes:
- A section promoting the premium subscription.
- A form that allows the user to subscribe to the premium service.

New Features:
- Added a form to handle premium subscription.

## views.py
This file contains the view functions for the Movie Ranker application. It includes:
- `movie_list`: Displays a list of movies filtered by genre. Limits results to 5 for unauthenticated users.
- `home_view`: Displays the home page with sponsored movies.
- `user_profile`: Displays the user profile page.
- `subscribe`: Handles the subscription process and redirects to the user profile page upon successful subscription.
- `movie_details`: Displays the details of a specific movie.

New Features:
- Added view functions to handle premium subscription and display sponsored movies.

## api.py
This file is used to define functions that interact with The Movie Database API. It includes:
- Functions to get the genre list.
- Functions to get the list of movies for a specific genre.
- Functions to get the details of a specific movie.

New Features:
- Integrated TMDB API to fetch movie details and affiliate links.

## models.py
This file is used to define the models for the movie app. It includes:
- The `Movie` model to represent a movie in the database.
- Fields for the title, genre, rating, overview, and release date of the movie.

New Features:
- Added `affiliate_link` field to the `Movie` model.
- Added `is_sponsored` field to the `Movie` model to indicate sponsored movies.

## Summary of New Features in `monetization_features` Branch
- **Affiliate Marketing**: Added affiliate links for movies.
- **Premium Subscription**: Added premium subscription functionality.
- **Advertisements**: Added dynamic ad banners based on the selected genre.
- **Sponsorships**: Added a section for sponsored movies.


## ITALIAN 
# Riepilogo dei file e delle nuove funzionalità nel branch `monetization_features`

## urls.py
Questo file definisce i pattern URL per l'applicazione Movie Ranker. Include:
- La vista principale della lista dei film (`movie_list`).
- La vista home (`home`).
- La vista del profilo utente (`user_profile`).
- La vista di sottoscrizione (`subscribe`).
- La vista dei dettagli del film (`movie_details`).

Nuove funzionalità:
- Aggiunti pattern URL per le nuove viste relative alle funzionalità di monetizzazione.

## movie_list.html
Questo file HTML rappresenta la pagina principale per la visualizzazione dei film filtrati per genere. Include:
- Un modulo per selezionare il genere.
- Una lista di film filtrati.
- Una sezione per i film sponsorizzati.
- Un banner pubblicitario che cambia in base al genere selezionato.
- Se non ci sono film per il genere selezionato, viene visualizzato un messaggio appropriato.

Nuove funzionalità:
- Aggiunti link affiliati per i film.
- Aggiunta una sezione per i film sponsorizzati.
- Aggiunti banner pubblicitari dinamici in base al genere selezionato.

## user_profile.html
Questo file HTML rappresenta la pagina del profilo utente per l'applicazione Movie Ranker. Include:
- Un messaggio di benvenuto che visualizza il nome utente dell'utente loggato.
- Una sezione che promuove l'abbonamento premium.
- Un modulo che consente all'utente di sottoscrivere il servizio premium.

Nuove funzionalità:
- Aggiunta una sezione per l'abbonamento premium.
- Aggiunto un modulo per gestire l'abbonamento premium.

## home.html
Questo file HTML rappresenta la pagina home per l'applicazione Movie Ranker. Include:
- Link di navigazione verso altre pagine.
- Un modulo per selezionare il genere.
- Una lista di film filtrati.
- Una sezione per i film sponsorizzati.
- Un banner pubblicitario che cambia in base al genere selezionato.

Nuove funzionalità:
- Aggiunti link di navigazione verso le pagine del profilo utente e della sottoscrizione.
- Aggiunti link affiliati per i film.
- Aggiunta una sezione per i film sponsorizzati.
- Aggiunti banner pubblicitari dinamici in base al genere selezionato.

## subscribe.html
Questo file HTML rappresenta la pagina di sottoscrizione per l'applicazione Movie Ranker. Include:
- Una sezione che promuove l'abbonamento premium.
- Un modulo che consente all'utente di sottoscrivere il servizio premium.

Nuove funzionalità:
- Aggiunto un modulo per gestire l'abbonamento premium.

## views.py
Questo file contiene le funzioni di vista per l'applicazione Movie Ranker. Include:
- `movie_list`: Visualizza una lista di film filtrati per genere. Limita i risultati a 5 per gli utenti non autenticati.
- `home_view`: Visualizza la pagina home con i film sponsorizzati.
- `user_profile`: Visualizza la pagina del profilo utente.
- `subscribe`: Gestisce il processo di sottoscrizione e reindirizza alla pagina del profilo utente dopo una sottoscrizione avvenuta con successo.
- `movie_details`: Visualizza i dettagli di un film specifico.

Nuove funzionalità:
- Aggiunte funzioni di vista per gestire l'abbonamento premium e visualizzare i film sponsorizzati.

## api.py
Questo file è utilizzato per definire le funzioni che interagiscono con l'API di The Movie Database. Include:
- Funzioni per ottenere la lista dei generi.
- Funzioni per ottenere la lista dei film per un genere specifico.
- Funzioni per ottenere i dettagli di un film specifico.

Nuove funzionalità:
- Integrata l'API TMDB per ottenere i dettagli dei film e i link affiliati.

## models.py
Questo file è utilizzato per definire i modelli per l'applicazione dei film. Include:
- Il modello `Movie` per rappresentare un film nel database.
- Campi per il titolo, il genere, la valutazione, la descrizione e la data di rilascio del film.

Nuove funzionalità:
- Aggiunto il campo `affiliate_link` al modello `Movie`.
- Aggiunto il campo `is_sponsored` al modello `Movie` per indicare i film sponsorizzati.

## Riepilogo delle nuove funzionalità nel branch `monetization_features`
- **Affiliate Marketing**: Aggiunti link affiliati per i film.
- **Premium Subscription**: Aggiunta funzionalità di abbonamento premium.
- **Advertisements**: Aggiunti banner pubblicitari dinamici in base al genere selezionato.
- **Sponsorships**: Aggiunta una sezione per i film sponsorizzati.