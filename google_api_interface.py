import os
from googleapiclient.discovery import build


def get_youtube_comments(video_id):
    service = build("youtube", "v3")
    comment_count = int(os.environ["GET_COMMENT_COUNT"])

    comments = []

    collection = service.commentThreads().list(
        part="snippet", videoId=video_id, maxResults=comment_count, textFormat="plainText"
    )

    try:
        response = collection.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

    except Exception as e:
        print(e)

    service.close()

    return comments
