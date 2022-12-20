with open(os.path.join(new_path_name,'training_text_score.json'),'rb') as f:
    score=json.load(f)
import json
with open('/home/chenboc1/localscratch2/chenboc1/Adver_Conv/data/reddit_comment_setence.json', 'w') as f:
    # indent=2 is not needed but makes the file human-readable 
    # if the data is nested
    json.dump(reddit_setence_list, f, indent=2)        