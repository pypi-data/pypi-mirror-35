import pymysql
from datetime import datetime
import dateparser


class MySql:
    db=None
    cursor=None
    def __init__(self,host,user,password,db):

     self.db = pymysql.connect(host=host, user=user, passwd=password,db=db)

    def add_kwd(self, keyword, result, required_keyword=None, optional_keyword=None, excluded_keyword=None):
        self.cursor = self.db.cursor()
        self.cursor.execute("""INSERT INTO Periodic_keyword(Text, Optional, Required, Excluded) VALUES(%s,%s,%s,%s)""", (keyword, optional_keyword, required_keyword, excluded_keyword))
        self.cursor.execute("SELECT LAST_INSERT_ID(); ")
        keywordID=self.cursor.fetchone()
        for items in result:
            display_name = items.get_user().get_display_name()
            display_picture = items.get_user().get_display_picture()
            follower_count = items.get_user().get_follower_count()
            following_count = items.get_user().get_following_count()
            created_at = items.get_user().get_time()
            total_likes = items.get_user().get_total_likes()
            total_post = items.get_user().get_total_post()
            PostReshareCount = None
            userID = items.get_user().get_user_id()
            self.cursor.execute(
                """INSERT INTO Periodic_postuser (DisplayImage, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                 total_likes, userID))
            self.db.commit()
            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            postUserID = self.cursor.fetchone()
            post_content=items.get_text()
            time= items.get_user().get_time()
            user_id=items.get_user().get_user_id()
            source=items.get_source()
            resharer_count=items.get_reshare_count()
            post_id=items.get_status_id()


            self.cursor.execute("""Insert into Periodic_post(Keyword_id, PostUser_id, statusID,Content,CreatedAt, Source, ResharerCount) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(keywordID,postUserID,post_id,post_content,time,source,resharer_count))
            self.db.commit()

            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            self.postID = self.cursor.fetchone()
            if resharer_count!='0':
              for user in items.get_resharer():
                  display_name = user.get_display_name()
                  display_picture = user.get_display_picture()
                  follower_count = user.get_follower_count()
                  following_count = user.get_following_count()
                  created_at = user.get_time()
                  total_likes = user.get_total_likes()
                  total_post = user.get_total_post()
                  PostReshareCount = None
                  userID = user.get_user_id()
                  self.cursor.execute(
                      """INSERT INTO Periodic_postuser (DisplayImage, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                      (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                       total_likes, userID))
                  self.db.commit()
                  self.cursor.execute("SELECT LAST_INSERT_ID(); ")
                  postUserID = self.cursor.fetchone()
                  PostID=self.postID
                  self.cursor.execute(
                      """INSERT INTO Periodic_resharer (Post_id, PostUser_id) VALUES (%s,%s)""",
                      (PostID, postUserID))
                  self.db.commit()

        self.db.commit()
        #self.db.close()


    def add_to_Keyword(self, keyword, result, required_keyword=None, optional_keyword=None, excluded_keyword=None):
        self.cursor = self.db.cursor()
        self.cursor.execute("""INSERT INTO Keyword(Text, Optional, Required, Excluded) VALUES(%s,%s,%s,%s)""",
                            (keyword, optional_keyword, required_keyword, excluded_keyword))
        self.cursor.execute("SELECT LAST_INSERT_ID(); ")
        keywordID = self.cursor.fetchone()
