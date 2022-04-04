# fav_artist_database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 初期化関数
def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///..\\..\\data\\user_database.db"
    db = SQLAlchemy(app)
    db.init_app()

class User(db.Model):
    """
    Table_name : users
    Member_value
    user_id : primary_key, user_name : str, mail_address : str, pass_word : str, done : bool
    """
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    mail_address = db.Column(db.String(50), nullable=False)
    pass_word = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class FavArtist(db.Model):
    """
    Table_name : fav_artist
    Member_value
    table_id : primary_key, user_id : int, fav_artst_id : str, main_flag : bool, done : bool
    """
    __tablename__ = "fav_artists"
    table_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    fav_artist_id = db.Column(db.String(50), nullable=False)
    main_flag = db.Column(db.Boolean, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class SimUser(db.Model):
    """
    Table_name : sim_users
    Member_value
    table_id : primary_key, target_user_id : int, sim_user : user_id, done : bool
    """
    __tablename__ = "sim_users"
    table_id = db.Column(db.Integer, primary_key=True)
    target_user_id = db.Column(db.Integer, nullable=False)
    sim_user = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

# モデルの利用モジュールの作成
# データを更新するマーカー(done)いるかな...?

class UserList:
    def add(self, display_name, mail_address, pass_word):
        user = User(user_name=display_name, mail_address=mail_address, pass_word=pass_word, done=False)
        db.session.add(user)
        db.session.commit(user)
    
    def delete(self, display_name):
        user = User.query.filter_by(user_name=display_name).first()
        db.session.delete(user)
        db.session.commit()
    
    def get_all(self):
        users = User.query.all()
        return users

    def delete_doneuser(self):
        User.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, users):
        for user in self.get_all():
            if user.user_id in users:
                user.done = True
            else:
                user.done = False
        db.session.commit()
    
class FavArtistList:
    def add(self, user_id, artist_id, main_flag):
        fav_artist = FavArtist(user_id=user_id, fav_artist=artist_id, main_flag=main_flag, done=False)
        db.session.add(fav_artist)
        db.session.commit()
    
    def delete_users_fav_artists(self, user_id):
        FavArtist.query.filter_by(user_id=user_id).delete()
        db.session.commit()
    
    def get_all_main_fav_artist(self, user_id):
        main_artists = FavArtist.query.filter_by(db.and_(user_id=user_id, main=True)).all()
        return main_artists
    
    def get_all_sub_fav_aritist(self, user_id):
        sub_artists = FavArtist.query.filter_by(db.and_(user_id=user_id, main=False)).all()
        return sub_artists
    
    def get_all(self):
        artists = FavArtist.query.all()
        return  artists
    
    def delete_doneuser(self):
        FavArtist.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, table_ids):
        for artist in self.get_all():
            if artist.table_id in table_ids:
                artist.done = True
            else:
                artist.done = False
        db.session.commit()

class SimUserList:
    def add(self, target_user, sim_user):
        sim_user = SimUser(target_user_id = target_user, sim_user=sim_user)
        db.session.add(sim_user)
        db.session.commit()

    def delete_users_data(self, target_user):
        SimUser.query.filter_by(user_id=target_user).delete()
        db.session.commit()
    
    def get_all(self):
        sim_users = SimUser.query.all()
        return sim_users

    def delete_doneuser(self):
        FavArtist.query.filter_by(done=True).delete()
        db.session.commit()
    
    def update_done(self, table_ids):
        for sim_user in self.get_all():
            if sim_user.table_id in table_ids:
                sim_user.done = True
            else:
                sim_user.done = False
        db.session.commit()   

    
    







