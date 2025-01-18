# MovieRanker

**MovieRanker** is a prototype web application written in Django. Its primary goal is to help users discover movies tailored to their preferences using The Movie Database (TMDB) API.

---

## Features

- **Integration with TMDB API:** Fetch movie genres, ranks, and other details using TMDB API endpoints.
- **Genre Filtering:** Filter movies by selecting genres from a dropdown menu.
- **Dynamic Movie List:** Display a ranked list of movies based on the selected genre.
- **Movie Details Page:** View detailed information about a selected movie.

---

## Key Components

1. **`api.py`**:
   - Interacts with the TMDB API.
   - Fetches genres, movies by genre, and detailed movie information.

2. **`views.py`**:
   - Handles user requests and business logic.
   - Includes views for the movie list and movie details.

3. **`models.py`**:
   - Defines the data structure for movies.

4. **`movie_list.html`**:
   - Frontend template for viewing and filtering movies by genre.

5. **`movie_details.html`**:
   - Frontend template for displaying detailed information about a specific movie.

---

## Installation and Setup

Follow these steps to set up and run **MovieRanker** locally:

### Prerequisites

- Python 3.9 or higher
- Django installed
- TMDB API Key (for API integration)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mike014/MovieRanker.git
   cd MovieRanker
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\\Scripts\\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Set Up TMDB API Key**:
   	•	Create a .env file in the root directory.
	•	Add your TMDB API key:
    ```bash
    TMDB_API_KEY=your_api_key_here
    ```

6.	**Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7.	**Access the Application**:
    ```plaintext
    http://127.0.0.1:8000/
    ```

## Development Workflow

### Linting and Formatting

- This project uses Pylint, Black, and isort for linting and formatting.  Pre-commit hooks are set up to enforce these standards.

	1.	**Install pre-commit**:
        ```bash
        pip install pre-commit
        pre-commit install
        ```
    2.	**Run pre-commit hooks**:
        ```bash
        pre-commit run --all-files
        ```

    ### Running Tests
    To run tests, use:
    ```bash
    pytest
    ```

    **Using Tox**
    Tox is configured to automate testing and linting:
    ```bash
    tox
    ```

    **GitHub Actions**
    The project includes a GitHub Actions workflow for automated testing and linting. The configuration is in .github/workflows/lint-and-test.yml.

    **Running Django Tests**
    To run Django tests for the Movies app and discover any bugs, you can use the following command:
    ```bash
     python manage.py test movies
    ```

## Useful TMDB API Endpoints

1. Fetch Genre List:
    ```bash
    https://api.themoviedb.org/3/genre/movie/list
    ```

2.	Discover Movies by Genre:
    ```bash
    https://api.themoviedb.org/3/discover/movie
    ```

3.	Get Movie Details:
    ```bash
    https://api.themoviedb.org/3/movie/{movie_id}
    ```

4.	Fetch Similar Movies:
    ```bash
    https://api.themoviedb.org/3/movie/{movie_id}/similar
    ```

## Documentation

- The documentation for MovieRanker is available at: [MovieRanker Documentation](https://Mike014.github.io/MovieRanker/)
- Created a new requirements.txt file with command:

```bash
pip install pipreqs
pipreqs .
```
- created docker file, you can buld the image with this command:
```bash
docker build . -t movies:latest && docker run -e PYTHONUNBUFFERED=1 -p 8000:8000 movies
```
- Go to [Link](http://localhost:8000/movies/)
  
## Future Goals

- Implement content-based and collaborative filtering for advanced movie recommendations.
- Enhance user interface and add user authentication.
- Deploy the application on a cloud platform.

## License

This project is licensed under the **MIT License**.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contact

Maintainer: Michele Grimaldi
GitHub: Mike014[Mike014](https://github.com/Mike014)
