import csv
import collections
from unicodedata import normalize

def cargar_datos():
    with open('data/movie.csv', encoding='utf-8') as fichero:
        movies_csv = csv.DictReader(fichero)
        movies = collections.defaultdict(list)
        Movie = collections.namedtuple('Movie', 'title year score')
        for line in movies_csv:
            try:
                movie_title = normalize(
                    'NFKC',
                    line['movie_title']).rstrip()
                director = line['director_name']
            except ValueError:
            m = Movie(title = movie_title, year = 2002, score = 3.2)
            movies[director].append(m)
    return(movies)

def main():
    movies_data = cargar_datos()
    contador = collections.Counter(movies_data)
    print(contador.most_common(5))

 
if __name__ == "__main__":
    main()