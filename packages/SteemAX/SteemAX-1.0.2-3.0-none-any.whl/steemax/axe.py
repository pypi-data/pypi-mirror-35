#!/usr/bin/python3

from steemax import axdb
from steemax import axverify
from steemax import default

db = axdb.AXdb(default.dbuser, 
                    default.dbpass, 
                    default.dbname)
verify = axverify.AXverify()

def exchange():
    ''' This method actualizes the exchange between Steemians.
    ID          row[0]
    Inviter     row[1]
    Invitee     row[2]
    Percentage  row[3]
    Ratio       row[4]
    Duration    row[5]
    MemoID      row[6]
    Status      row[7]
    Timestamp   row[8]
    '''
    axlist = db.get_axlist(run=True)
    for row in axlist:
        print("Comparing "+str(row[1])+" vs. "+str(row[2]))
        if verify.eligible_posts(row[1], row[2]) is not False:
            print("Posts are eligible.")
            if verify.eligible_votes(row[1], 
                                row[2], 
                                row[3], 
                                row[4], 
                                2) is not False:
                print("Votes are eligible")
                # Inviter votes invitee's post
                vote_on_it(row[1], 
                            row[2], 
                            verify.post_two, 
                            int(row[3]))
                # Invitee votes inviter's post
                vote_on_it(row[2], 
                            row[1], 
                            verify.post_one, 
                            verify.vote_cut)


def vote_on_it(voter, author, post, weight):
    # refresh the token in the database
    # and use voter's token to upvote 
    # author's post 
    verify.steem.connect.steemconnect(
                    renewed_token(voter))
    result = verify.steem.connect.vote(
                    voter, 
                    author, 
                    post, 
                    int(weight))
    try:
        result['error']
    except:
        # The vote was successful
        print(str(row[1])+" has voted on "
                        +str(verify.post_two)+" "
                        +str(row[3])+"%")                    
    else:
        print(result)
        verify.msg.error_message(result)


def renewed_token(invitee):
    refreshtoken = db.get_user_token(invitee)
    if verify.verify_token(refreshtoken):
        db.update_token(verify.steem.username, 
                verify.steem.accesstoken, 
                verify.steem.refreshtoken)
        return verify.steem.accesstoken
    else:
        return False


# EOF
