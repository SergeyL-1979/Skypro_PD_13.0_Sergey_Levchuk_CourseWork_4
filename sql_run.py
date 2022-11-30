from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)

# Конец подключения и настройки


favorite_genres = db.Table('favorite_genres',
                           db.Column('user_id', db.Integer, db.ForeignKey('user.pk')),
                           db.Column('genre_id', db.Integer, db.ForeignKey('genre.pk'))
                           )
movie_genre = db.Table('movie_genre',
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.pk')),
                       db.Column('genre_id', db.Integer, db.ForeignKey('genre.pk'))
                       )

movie_director = db.Table('movie_director',
                          db.Column('movie_id', db.Integer, db.ForeignKey('movie.pk')),
                          db.Column('director_id', db.Integer, db.ForeignKey('director.pk'))
                          )


class User(db.Model):
    __tablename__ = "user"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    surname = db.Column(db.String(255))
    favorite_genre_id = db.relationship("Genres", secondary=favorite_genres)

    __table_args__ = (
        db.PrimaryKeyConstraint('pk', name='user_pk'),  # Основной ключ
        db.UniqueConstraint('name'),  # Уникальный ключ
        db.UniqueConstraint('email'),  # Уникальный ключ
    )

    def __repr__(self):
        return f"<User {self.name}, {self.favorite_genre_id}>"


class Movies(db.Model):
    __tablename__ = "movie"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    trailer = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.relationship("Genres", secondary=movie_genre)
    director_id = db.relationship("Directors", secondary=movie_director)

    def __repr__(self):
        return f"<Movies: {self.title}, Genre: {self.genre_id}, Director: {self.director_id}>"


class Directors(db.Model):
    __tablename__ = "director"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(150))

    # movies_id = db.Column(db.Integer, db.ForeignKey('director.pk'))

    def __repr__(self):
        return f"<Directors: {self.name}>"


class Genres(db.Model):
    __tablename__ = "genre"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Genre: {self.name}>"


# Здесь мы тестируем
genre_1 = Genres(name="genre=1", pk=1)
genre_2 = Genres(name="genre=2", pk=2)
genre_3 = Genres(name="genre=3", pk=3)
genre_4 = Genres(name="genre=4", pk=4)
director_1 = Directors(name='FooFI', pk=1)
director_2 = Directors(name='Dir_DO', pk=2)
user_1 = User(pk=1, name="User_1", email="foo_1@foo_1.com", password="123456", surname="Foo_User_1", favorite_genre_id=[genre_1, genre_3])
user_2 = User(pk=2, name="User_2", email="foo_2@foo_2.com", password="123456", surname="Foo_User_2", favorite_genre_id=[genre_3])

movie_1 = Movies(pk=1, title='M_1', description='M-1__11', trailer='URL', year=2021, rating=4.5, genre_id=[genre_4, genre_1], director_id=[director_1, director_2])


print(user_1, genre_1, genre_3)
print(user_2, genre_3)

print(movie_1, director_1, director_2)
