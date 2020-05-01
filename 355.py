from collections import OrderedDict
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followingdatabase=OrderedDict() # userid : who they are following
        self.tweetdatabase=OrderedDict() #TweetId: (userID) pop off database
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.followingdatabase.keys():
            self.followingdatabase[userId]=[userId]

        
        self.tweetdatabase[tweetId]=userId

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.followingdatabase.keys():
            self.followingdatabase[userId]=[userId]
        
        
        feed=[]
        c=0
        for k,v in list(self.tweetdatabase.items())[::-1]:
            
            if c==10:
                break
            if v in self.followingdatabase[userId]:
                feed.append(k)
                c=c+1
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followingdatabase.keys():
            self.followingdatabase[followerId]=[followerId]
        if followeeId not in self.followingdatabase.keys():
            self.followingdatabase[followeeId]=[followeeId]
        self.followingdatabase[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
        
            if followerId in self.followingdatabase.keys():
                if followeeId in self.followingdatabase[followerId]:
                    ind=self.followingdatabase[followerId].index(followeeId)
                    del ((self.followingdatabase[followerId])[ind])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
