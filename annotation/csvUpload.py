import psycopg2
from config import config


def csvUpload(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")

    user_id = requestParameters.pop()
    for dictionary in requestParameters:
        cur = conn.cursor()

        headline = dictionary["title"]
        content = dictionary["description"]
        owner = dictionary["author"]
        release_date = dictionary["releaseDate"]
        source = dictionary["source"]
        url = dictionary["url"]
        question = ''
        last_modified_by = user_id
        status = 'todo'

        if content == '':
            content = ' '

        if release_date == '':
            cur.execute("""INSERT INTO master_table (user_id, headline, content, owner, release_date, source, url, question,last_modified_by, status) 
            VALUES ( %(user_id)s, %(headline)s, %(content)s, %(owner)s, now(), %(source)s, %(url)s, %(question)s,%(last_modified_by)s, %(status)s );""",
                        {'user_id': user_id, 'headline': headline, 'content': content, 'owner': owner,
                         'source': source, 'url': url, 'question': question, 'last_modified_by': last_modified_by,
                         'status': status})
        else:
            cur.execute("""INSERT INTO master_table (user_id, headline, content, owner, release_date, source, url, question,last_modified_by, status) 
            VALUES ( %(user_id)s, %(headline)s, %(content)s, %(owner)s, %(release_date)s, %(source)s, %(url)s, %(question)s,%(last_modified_by)s, %(status)s );""",
                        {'user_id': user_id, 'headline': headline, 'content': content, 'owner': owner,
                         'release_date': release_date, 'source': source, 'url': url, 'question': question,
                         'last_modified_by': last_modified_by, 'status': status})

        cur.close()
        conn.commit()

    conn.close()
    return {"message": "success"}
