import csv
import collections

def cargar_datos():
    with open('../data/movie.csv', encoding='utf-8') as fichero:
        movies_csv = csv.DictReader(fichero)
        movies = collections.defaultdict(list)
        Movie = collections.namedtuple('Movie', 'title year score')
        for line in movies_csv:
            try:
                movie_title = line['movie_title']
                director = line['director_name']
            except ValueError:
                continue
            m = Movie(title = movie_title, year = 2002, score = 3.2)
            movies[director].append(m)
    return(movies)

def main():
    movies_data = cargar_datos()
    print(type(movies_data))

 
if __name__ == "__main__":
    main()