import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    
    with open(sentiment_file,'r',encoding='utf-8') as fr:
        text_all_demo=fr.readlines()
    for per_line in text_all_demo:
        str_word_score_list=per_line.split("\t")
        if len(str_word_score_list)==1:
            str_word_score_list.append("0")
        if str_word_score_list[0] not in scores:
            try:
                scores[str_word_score_list[0]]=int(str_word_score_list[1])
            except Exception as e:
                scores[str_word_score_list[0]] = 0
    
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    word_list=tweet.replace('\n',"").split(" ")
    for per_word in word_list:
        if per_word in sent_scores:
            score+=sent_scores[per_word]

    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    new_term_sent_temp = {}

    with open(tweets_file,'r',encoding='utf-8') as fr:
        all_tweets=fr.readlines()
    count={}
    for per_line in all_tweets:
        sentiment = 0
        sentiment=get_tweet_sentiment(per_line,sent_scores)
        all_words=per_line.replace("\n",'').split(' ')
        for per_word in all_words:

            # if per_word not in sent_scores and per_word not in new_term_sent:
            #     new_term_sent[per_word]=get_tweet_sentiment(per_word,sent_scores)
            if per_word in sent_scores:
                # sentiment=sentiment+sent_scores[per_word]
                count[per_word]=count.get(per_word,0)+1
            else:
                count[per_word]=count.get(per_word,0)+1
        for per_word in all_words:
            if sentiment > 0:
                new_term_sent_temp[per_word] = new_term_sent_temp.get(per_word, 0) + 1
            elif sentiment < 0:
                new_term_sent_temp[per_word] = new_term_sent_temp.get(per_word, 0) - 1
            else:
                new_term_sent_temp[per_word] = new_term_sent_temp.get(per_word, 0)
    for per_word,sentiment in new_term_sent_temp.items():
        new_term_sent[per_word]=float(sentiment/count[per_word])

    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()