# Here go your api methods.

@auth.requires_signature()
def add_post():
    post_id = db.post.insert(
        post_title=request.vars.post_title,
        post_description=request.vars.post_description,
        post_price= request.vars.post_price,
        post_city=request.vars.post_city,
        post_image=request.vars.post_image,
    )
    # We return the id of the new post, so we can insert it along all the others.
    return response.json(dict(post_id=post_id))


def get_post_list():
    results = []
    #use for limiting what a user who isnt logged in can see
    if auth.user is None:
        # Not logged in.
        rows = db().select(db.post.ALL, orderby=~db.post.post_time)
        for row in rows:
            results.append(dict(
                id=row.id,
                post_title=row.post_title,
                post_description=row.post_description,
                post_author=row.post_author,
                post_price=row.post_price,
                post_time=row.post_time,
                post_username=row.post_username,
                post_category=row.post_category,
                post_image=row.post_image,
                post_city=row.post_city
            ))
    else:
        # Logged in.
        # rows = db().select(db.post.ALL, db.thumb.ALL,
        #                     left=[
        #                         db.thumb.on((db.thumb.post_id == db.post.id) & (db.thumb.user_email == auth.user.email)),
        #                     ],
        #                     orderby=~db.post.post_time)

        rows = db().select(db.post.ALL, orderby=~db.post.post_time)
        for row in rows:
            results.append(dict(
                id=row.id,
                post_title=row.post_title,
                post_description=row.post_description,
                post_author=row.post_author,
                post_price=row.post_price,
                post_time=row.post_time,
                post_username=row.post_username,
                post_category=row.post_category,
                post_image=row.post_image,
                post_city=row.post_city
            ))
    # For homogeneity, we always return a dictionary.
    return response.json(dict(post_list=results))


def get_user_post_list():
    results = []
    #use for limiting what a user who isnt logged in can see
    if auth.user is None:
        # Not logged in.
        rows = db().select(db.post.ALL, orderby=~db.post.post_time)
        for row in rows:
            results.append(dict(
                id=row.id,
                post_title=row.post_title,
                post_description=row.post_description,
                post_author=row.post_author,
                post_price=row.post_price,
                post_time=row.post_time,
                post_username=row.post_username,
                post_category=row.post_category,
                post_image=row.post_image,
                post_city=row.post_city
            ))
    else:
        # Logged in.
        # rows = db().select(db.post.ALL, db.thumb.ALL,
        #                     left=[
        #                         db.thumb.on((db.thumb.post_id == db.post.id) & (db.thumb.user_email == auth.user.email)),
        #                     ],
        #                     orderby=~db.post.post_time)

        rows = db().select(db.post.ALL, orderby=~db.post.post_time)
        for row in rows:
            if auth.user.username == row.post_username:
                results.append(dict(
                    id=row.id,
                    post_title=row.post_title,
                    post_description=row.post_description,
                    post_author=row.post_author,
                    post_price=row.post_price,
                    post_time=row.post_time,
                    post_username=row.post_username,
                    post_category=row.post_category,
                    post_image=row.post_image,
                    post_city=row.post_city
                ))
    # For homogeneity, we always return a dictionary.
    return response.json(dict(user_post_list=results))
    