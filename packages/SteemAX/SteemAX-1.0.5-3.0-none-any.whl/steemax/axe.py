#!/usr/bin/python3

from simplesteem.simplesteem import SimpleSteem
from steemax import axdb
from steemax import axverify
from steemax import default

db = axdb.AXdb(default.dbuser, 
                    default.dbpass, 
                    default.dbname)
verify = axverify.AXverify()
steem = SimpleSteem(client_id=default.client_id,
                    client_secret=default.client_secret,
                    callback_url=default.callback_url,
                    screenmode=default.msgmode)

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
    newtoken = renewed_token(voter)
    steem.connect.steemconnect(
                    newtoken)
    result = steem.connect.vote(
                    voter, 
                    author, 
                    post, 
                    int(weight))
    try:
        result['error']
    except:
        # The vote was successful
        print(str(voter)+" has voted on "
                        +str(post)+" "
                        +str(weight)+"%")                    
    else:
        verify.msg.error_message(str(result))   
        

def renewed_token(accountname):
    db.get_user_token(accountname)
    refreshtoken = db.dbresults[0][2]
    if steem.verify_key(
                    acctname="", tokenkey=refreshtoken):
        db.update_token(steem.username,
                steem.accesstoken, 
                steem.refreshtoken)
        return steem.accesstoken
    else:
        return False


# EOF
