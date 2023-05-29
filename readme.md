## UPDATE

It looks like the user @verified no long follows who's verified on Twitter. If this changes in the future I'll try to update the code, however this method no longer works as far as I can tell. You can still see the old lists in the git repo history with the 'verified\_users.csv' file if you're ok with older data.

# Verified Twitter User List

This contains two things:

 - A list of all verified twitter users, their account ID's, and the account names
 - A python script to get a list of all people any particular twitter account follows (in this case the [@verified](https://twitter.com/verified/following) account, which follows all verified twitter users).

The list was updated on 11/12/2022 however will continue to become more out of date with time (although hopefully the git history will reflect some interesting changes in verification status after Elon purchased twitter). If you want to redownload the verified twitter list you will need to get API keys from twitter and run the script (which may take 15 minutes per 15k users you pull due to twitter rate limiting).

The verified\_users.csv file is split with quotation marks and commas and is structured something like this:

| Account ID | Username | Chosen name |
|------------|----------|-------------|
|   ...      |   ...    |    ...      |
|   ...      |   ...    |    ...      |



## Note when building

configparser can't interpret '%' characters, however one way you can fix this if your bearer token has them is to double them up. i.e. '%' => '%%', this technique is [mentioned here](https://stackoverflow.com/questions/71854527/configparser-interpolationsyntaxerror-must-be-followed-by-or-found). Once you have your consumer key you can [follow this guide](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) to generate the bearer token from the command line.

## Build Notes

I used tweepy=4.12.1 when building, although I don't expect the API to change a ton moving forward. Regardless though I've recently added a requirements.txt file as well, which you can install using 

```
pip install -r requirements.txt
```

Otherwise you can run this file on your own by filling in the keys and running 

```
python3 followerList.py
```

When you run this script it will generate a verified\_users.txt file structured as strings separated by commas. If you want to convert it to a more standard csv file separated with commas and quotation marks you can run csv-conv.py to get verified\_users.csv.

```
python3 csv-conv.py
```
