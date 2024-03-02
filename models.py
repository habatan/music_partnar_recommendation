# Legacy Query Interface — Flask-SQLAlchemy Documentation (3.1.x) (palletsprojects.com)
# >> from project import db, create_app, models
# >> db.create_all(app=create_app())
from flask_sqlalchemy import SQLAlchemy
import numpy as np

db = SQLAlchemy()

class User(db.Model):
    """
    Table_name : users
    Member_value
    user_token : primary_key, user_name : str, mail_address : str, pass_word : str, done : bool
    """
    __tablename__ = "users"
    user_token = db.Column(db.String(32), primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    # mail_address = db.Column(db.String(50), nullable=False)
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
    def add_user(self, user_token, display_name, pass_word):
        user = User(user_token=user_token, user_name=display_name, pass_word=pass_word, done=False)
        db.session.add(user)
        db.session.commit()
   
    def delete_user(self, user_token):
        User.query.filter_by(user_token=user_token).delete()
        db.session.commit()
    
    def get_user_info(self, user_token):
        # users = db.session.execute(db.select(User).order_by(User.username)).
        users = User.query.filter_by(user_token=user_token).first_or_404()
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
    
    def get_users_by_artist_id(self, artist_id):
        users = set(FavArtist.query.filter_by(fav_artist_id=artist_id).all())
        return users
        
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
        sim_user = SimUser(target_user_token = target_user, sim_user=sim_user, done=False)
        db.session.add(sim_user)
        db.session.commit()

    def delete_users_data(self, target_user):
        SimUser.query.filter_by(target_user_token=target_user).delete()
        db.session.commit()

    def get_sim_user_all(self, user_token):
        artists = SimUser.query.filter_by(target_user_token=user_token).all()
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

# spotify関連
def get_users_by_aritst_id(artist_ids:list):
    """
    artistを選択しているuserを返す : {"artist" : [users,･･･]} → dict
    """
    assert type(artist_ids) == list, "入力形式をlistにしてください"
    artist_to_users = {}
    for artist_id in artist_ids:
        users = FavArtistList.get_users_by_artist_id(artist_id)
        artist_to_users[artist_id] = users
    return artist_to_users

def get_avarage_of_selected_artists():
    """
    一人あたり選択アーティストの平均を返す : avarage → int
    """
    users = UserList._get_all()
    selected_artist = np.array([])
    for user in users:
        token = user.user_token
        artists = FavArtistList.get_all_main_fav_artist(token)
        selected_artist = np.append(selected_artist,len(artists))
    avarage = np.average(selected_artist)
    return avarage
    