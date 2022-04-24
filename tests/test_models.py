# test aql hanling module
import pytest
from app import create_app
from  modules.models.models import *

app = create_app(config="test")
init_db(app)

def test_User(): 
    db.create_all()
    # make
    user = User(user_token="#thisistoken", user_name="username", mail_address="user@user.com", pass_word="user", done=False)
    assert user
    # delete
    User.query.filter_by(user_token="#thisistoken").delete()
    db.session.commit()
    db.session.close()

def test_UserList():  
    db.create_all()
    user_list = UserList()
    # add
    user_list.add_user(user_token="#thisistoken", display_name="username", mail_address="user@user.com", pass_word="user") 
    assert db.session.query(User).filter_by(user_token="#thisistoken").first(), "Userオブジェクトが作成されていません"
    # delete
    user_list.delete_user(user_token="#thisistoken")
    assert 0 == db.session.query(User).filter_by(user_token="#thisistoken").count(), "Userオブジェクトが適切に削除されていません"
    # display
    user_list.add_user(user_token="#thisistoken01", display_name="username01", mail_address="user01@user.com", pass_word="user01") 
    user_list.add_user(user_token="#thisistoken02", display_name="username02", mail_address="user02@user.com", pass_word="user02")
    user_list.add_user(user_token="#thisistoken03", display_name="username03", mail_address="user03@user.com", pass_word="user03")
    user01 = user_list.get_user_info("#thisistoken01")
    user02 = user_list.get_user_info("#thisistoken02")
    user03 = user_list.get_user_info("#thisistoken03")
    assert user01, "User01の情報を取得できていません"
    assert user02, "User02の情報を取得できていません"
    assert user03, "User03の情報を取得できていません"
    # clear
    user_list.delete_user(user_token="#thisistoken01")
    user_list.delete_user(user_token="#thisistoken02")
    user_list.delete_user(user_token="#thisistoken03")
    db.delete(User)
    db.session.commit()
    db.session.close()

def test_FavArtist():
    db.create_all()
    # make
    artist = FavArtist(user_token="#thisistoken", fav_artist_id="6U3ybJ9UHNKEdsH7ktGBZ7", main_flag=True, done=False)
    assert artist, "FavArtistオブジェクトが作成されていません"
    # delete
    FavArtist.query.filter_by(user_token="#thisistoken").delete()
    db.session.commit()
    db.session.close()

def test_FavArtistList():
    db.create_all()
    fav_artist_list=FavArtistList()
    # add
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ7", main_flag=True)
    assert db.session.query(FavArtist).filter_by(user_token="#thisistoken").first(), "FavArtistオブジェクトが作成されていません"
    # delete
    fav_artist_list.delete_users_fav_artists(user_token="#thisistoken")
    assert 0 == db.session.query(FavArtist).filter_by(user_token="#thisistoken").count(), "FavArtistオブジェクトが適切に削除されていません"
    # display
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ7", main_flag=True)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ8", main_flag=True)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ9", main_flag=True)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ1", main_flag=True)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ2", main_flag=True)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ3", main_flag=False)
    fav_artist_list.add_user_fav_artist(user_token="#thisistoken", artist_id="6U3ybJ9UHNKEdsH7ktGBZ4", main_flag=True)
    main_fav_list = fav_artist_list.get_all_main_fav_artist(user_token="#thisistoken")
    sub_fav_list = fav_artist_list.get_all_sub_fav_aritist(user_token="#thisistoken")
    assert main_fav_list, "main_fav_listを正しく抽出をできていません"
    assert type(main_fav_list) == list, f"main_fav_listの形式が{type(main_fav_list)}になっています"
    assert len(main_fav_list) == 6, "mainでないアーティストも抽出されています"
    assert sub_fav_list, "sub_fav_listを正しく抽出をできていません"
    assert type(sub_fav_list) == list, f"sub_fav_listの形式が{type(sub_fav_list)}になっています"
    assert len(sub_fav_list) == 1, "subでないアーティストも抽出されています"
    
    # clear
    fav_artist_list.delete_users_fav_artists(user_token="#thisistoken")
    db.delete(FavArtist)
    db.session.commit()
    db.session.close()

def test_SimUser():
    db.create_all()
    # make
    sim_user = SimUser(target_user_token="#thisistoken", sim_user="#thisisSimUsertoken",done=False)
    assert sim_user, "SimUserオブジェクトが作成されていません"
    # delete
    SimUser.query.filter_by(target_user_token="#thisistoken").delete()
    db.session.commit()
    db.session.close()

def test_SimUserList():
    db.create_all()
    sim_user_list = SimUserList()
    # add
    sim_user_list.add_sim_user(target_user="#thisistoken", sim_user="#thisisSimUsertoken")
    assert db.session.query(SimUser).filter_by(target_user_token="#thisistokne"), "SimUserオブジェクトが追加されていません"
    # delete
    sim_user_list.delete_users_data(target_user="#thisistoken")
    assert 0 == db.session.query(SimUser).filter_by(target_user_token="#thisistoken").count(), "SimUserオブジェクトが適切に削除されていません"
    # display
    sim_user_list.add_sim_user(target_user="#thisistoken01", sim_user="#thisisSimUsertoken05")
    sim_user_list.add_sim_user(target_user="#thisistoken01", sim_user="#thisisSimUsertoken02")
    sim_user_list.add_sim_user(target_user="#thisistoken01", sim_user="#thisisSimUsertoken03")
    sim_user_list.add_sim_user(target_user="#thisistoken01", sim_user="#thisisSimUsertoken66")
    sim_user_list.add_sim_user(target_user="#thisistoken05", sim_user="#thisisSimUsertoken16")
    sim_user_list.add_sim_user(target_user="#thisistoken05", sim_user="#thisisSimUsertoken27")
    sim_user_list.add_sim_user(target_user="#thisistoken05", sim_user="#thisisSimUsertoken38")
    sim_users01 = sim_user_list.get_sim_user_all("#thisistoken01")
    sim_users05 = sim_user_list.get_sim_user_all("#thisistoken05")
    assert sim_users01, "user01に置けるSimUserオブジェクトが適切に抽出できていません"
    assert sim_users05, "user05におけるSimUserオブジェクトが適切に抽出できていません"
    assert type(sim_users01) == list, f"SimUserオブジェクトが{type(sim_users01)}形式で取得されています"
    assert type(sim_users05) == list, f"SimUserオブジェクトが{type(sim_users05)}形式で取得されています"
    assert len(sim_users01) == 4, "user01におけるSimUserが適切に抽出されていません"
    assert len(sim_users05) == 3, "user05におけるSimUserが適切に抽出されていません"
    # clear
    sim_user_list.delete_users_data(target_user="#thisistoken01")
    sim_user_list.delete_users_data(target_user="#thisistoken05")
    db.delete(SimUser)
    db.session.commit()
    db.session.close()




