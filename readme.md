# Verified Twitter User List

This contains two things:

 - A list of all verified twitter users, their account ID's, and the account names
 - A python script to get a list of all people any particular twitter account follows (in this case the [verified](https://twitter.com/verified/following) account, which follows all verified twitter users).

The list was compiled on 08/02/2022 and will continue to become more out of date with time. If you want to redownload the verified twitter list you will need to get API keys from twitter and run the script (which may take 15 minutes per 15k users you pull due to twitter rate limiting).

The verified\_users.csv file is split with quotation marks and commas and is structured something like this:

| Account ID | Username | Chosen name |
|------------|----------|-------------|
|   ...      |   ...    |    ...      |
|   ...      |   ...    |    ...      |



## Note when building

configparser can't interpret '%' characters, however one way you can fix this if your bearer token has them is to double them up. i.e. '%' => '%%', this technique is [mentioned here](https://stackoverflow.com/questions/71854527/configparser-interpolationsyntaxerror-must-be-followed-by-or-found)

## Build Notes

I used tweepy=4.10.0 when building, although I don't expect the API to change a ton so I'm not including a requirements file.
