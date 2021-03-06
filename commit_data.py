from app.models import *
from app import db

voters = [Voter(national_id="12345678", first_name="John", last_name="Joe"),
          Voter(national_id="23456789",
                first_name="Jane", last_name="Joe"),
          Voter(national_id="45656764",
                first_name="Michael", last_name="Joe"),
          Voter(national_id="34567891", first_name="Andrew", last_name="Does")]


presidents = [President(first_name="Uhuru", last_name="Kenyatta", location="Kenya", votes=0, party_name="Jubilee", profile_pic_path = "../../static/images/presidents/Uhuru_Kenyatta_1.jpg"), President(first_name="Raila", last_name="Odinga", location="Kenya", votes=0, party_name="ODM",  profile_pic_path = "../../static/images/presidents/raila.jpg")
    
]

deputies = [Deputy(first_name="William", last_name="Ruto", location="Kenya",president_id=1, profile_pic_path = "../../static/images/deputies/ruto.jpg"), Deputy(first_name="Kalonzo", last_name="Musyoka", location="Kenya",president_id=2, profile_pic_path = "../../static/images/deputies/kalonzo.jpg")]

governors = [
    Governor(first_name="Lee", last_name="Kinyanjui", location="Nakuru", votes=0, party_name="Jubilee", profile_pic_path = "../../static/images/governors/lee.jpg"), Governor(first_name="Mike", last_name="Mbuvi",location="Nairobi", votes=0, party_name="Jubilee", profile_pic_path = "../../static/images/governors/mike.jpg"),
    Governor(first_name="Josphat", last_name="Nanok", location="Turkana", votes=0, party_name="ODM", profile_pic_path = "../../static/images/governors/josphat.jpg")
   
]

senators = [
    Senator(first_name="Margaret", last_name="Kamar",
            location="Uasin-Gishu", votes=0,party_name="ODM",profile_pic_path = "../../static/images/senators/mkamar.jpg"),
    Senator(first_name="Kipchumba", last_name="Murkomen",
            location="Elgeyo-Marakwet", votes=0,party_name="Jubilee",profile_pic_path = "../../static/images/senators/Kipchumba.jpg"),
    Senator(first_name="Samuel", last_name="Poghisio",
            location="West-Pokot", votes=0,party_name="ODM",profile_pic_path = "../../static/images/senators/samuel.jpg")

]

parties =[
        Party(party_name="ODM",party_logo_path="../../static/images/odm.png"),
        Party(party_name="Jubilee",party_logo_path="../../static/images/jubilee.png")
]


def commit_data():
    data = [parties,voters, governors, presidents,deputies, senators]
    for list in data:
        for person in list:
            db.session.add(person)
    db.session.commit()
