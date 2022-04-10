# fav_artist_database
from operator import index
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# resolve flask shell bellow
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

# 初期化関数
def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///..\\..\\data\\user_database.db"
    # autoincrement
    app.config['SQLALCHEMY_ECHO'] = True
    db = SQLAlchemy(app)
    db.init_app(app)

class User(db.Model):
    """
    Table_name : users
    Member_value
    user_token : primary_key, user_name : str, mail_address : str, pass_word : str, done : bool
    """
    __tablename__ = "users"
    user_token = db.Column(db.String(32), primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    mail_address = db.Column(db.String(50), nullable=False)
    pass_word = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class FavArtist(db.Model):
    """
    Table_name : fav_artist
    Member_value
    index : primary_key, user_token : int, fav_artst_id : str, main_flag : bool, done : bool
    """
    __tablename__ = "fav_artists"
    index = db.Column(db.Integer, primary_key=True)
    user_token = db.Column(db.String(32), nullable=False)
    fav_artist_id = db.Column(db.String(50), nullable=False)
    main_flag = db.Column(db.Boolean, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class SimUser(db.Model):
    """
    Table_name : sim_users
    Member_value
    index : primary_key, target_user_token : int, sim_user : user_token, done : bool
    """
    __tablename__ = "sim_users"
    index = db.Column(db.Integer, primary_key=True)
    target_user_token = db.Column(db.String(32), nullable=False)
    sim_user = db.Column(db.String(32), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class UserList:
    def add_user(self,user_token, display_name, mail_address, pass_word):
        user = User(user_token=user_token, user_name=display_name, mail_address=mail_address, pass_word=pass_word, done=False)
        db.session.add(user)
        db.session.commit()
   
    def delete_user(self, user_token):
        user = User.query.filter_by(user_name=user_token).first()
        db.session.delete(user)
        db.session.commit()
    
    def get_user_all(self, user_token):
        users = User.query.filter_by(user_token=user_token).all()
        return users
    
    def _get_all(self):
        users = User.query.all()
        return users

    def delete_doneuser(self):
        User.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, users):
        for user in self._get_all():
            if user.user_id in users:
                user.done = True
            else:
                user.done = False
        db.session.commit()
    
class FavArtistList:
    def add_user_fav_artist(self, user_token, artist_id, main_flag):
        fav_artist = FavArtist(user_token=user_token, fav_artist_id=artist_id, main_flag=main_flag, done=False)
        db.session.add(fav_artist)
        db.session.commit()
    
    def delete_users_fav_artists(self, user_token):
        FavArtist.query.filter_by(user_token=user_token).delete()
        db.session.commit()
    
    def get_all_main_fav_artist(self, user_token):
        main_artists = FavArtist.query.filter_by(user_token=user_token,main_flag=True).all()
        return main_artists
    
    def get_all_sub_fav_aritist(self, user_token):
        sub_artists = FavArtist.query.filter_by(user_token=user_token, main_flag = False).all()
        return sub_artists

    def get_user_fav_all(self, user_token):
        artists = FavArtist.query.filter_by(user_token=user_token).all()
        return  artists
    
    def _get_all(self):
        artists = FavArtist.query.all()
        return  artists
    
    def delete_doneuser(self):
        FavArtist.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, table_ids):
        for artist in self._get_all():
            if artist.table_id in table_ids:
                artist.done = True
            else:
                artist.done = False
        db.session.commit()

class SimUserList:
    def add_sim_user(self, target_user, sim_user):
        sim_user = SimUser(target_user_token = target_user, sim_user=sim_user)
        db.session.add(sim_user)
        db.session.commit()

    def delete_users_data(self, target_user):
        SimUser.query.filter_by(user_token=target_user).delete()
        db.session.commit()

    def get_sim_user_all(self, user_token):
        artists = SimUser.query.filter_by(user_token=user_token).all()
        return  artists

    def _get_all(self):
        sim_users = SimUser.query.all()
        return sim_users

    def delete_doneuser(self):
        FavArtist.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, table_ids):
        for sim_user in self._get_all():
            if sim_user.table_id in table_ids:
                sim_user.done = True
            else:
                sim_user.done = False
        db.session.commit()   



