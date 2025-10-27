import csv
movies =[]



class Movie:
    count=0

    def __init__(self, title, duration, age):
        self.title = title
        self.duration = duration
        self.age = age
        Movie.count += 1
    def display_info(self):
        print(f"제목:{self.title}, 러닝타임:{self.duration}, 제한 연령:{self.age}")


    @claddmethos
    def show_count(cls):
       print(f"현재 상영 중인 영화는 {cls.count}개 입니다.")

def load_movies(filename):
    f=open(filename,"r", encoding= "utf-8-sig")
    reader=csv.reader(f)
     
    header = next(reader)
    print(header)
 
    for line in reader:
        title, duration, age =line
        movie_obj = Movie(title, duration , age) 
        movies.append(movie_obj)


    for m in movies:
        m.display_info()

    Movie.show_count()

    f.close()
load_movies("movie.csv")

