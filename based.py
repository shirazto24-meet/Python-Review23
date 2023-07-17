def create_youtube_video(title,description):
	youtube = {"Title":title, "Description":description,"Likes":0, "Dislikes":0,"Comments":{}}
	return youtube

def like(youtube):
	if "Likes" in youtube:
		youtube["Likes"]+= 1
	return youtube

def dislike(youtube):
	if "Dislikes" in youtube:
		youtube["Dislikes"]+= 1
	return youtube

def add_comment(youtube, username, comment_text):
	youtube["Comments"][username] = comment_text
	return youtube

new=create_youtube_video("what???", "no way!!!!!")
like(new)
dislike(new)
add_comment(new,"cherrybear2233","ur mom")
print(new)