# Download followers list

This should contain both the code to get a followers list, and a followers list of all verified twitter users from the account verified when I have time to run it over the whole thing.

To get an updated version use the list, if you don't need to be exact you can download mine. It should be as simple as applying for API tokens from twitter (which isn't really simple but I digress) and then entering them into the config.ini file.

This script works by downloading all the usernames from the following section of the [verified](https://twitter.com/verified/following) account, which has user ID 63796828, however you can get the user ID for any twitter account from [this site](https://tweeterid.com/) and replace it in the script.

## Note when building

configparser can't interpret '%' characters, however one way you can fix this if your bearer token has them is to double them up. i.e. '%' => '%%', this technique is [mentioned here](https://stackoverflow.com/questions/71854527/configparser-interpolationsyntaxerror-must-be-followed-by-or-found)
