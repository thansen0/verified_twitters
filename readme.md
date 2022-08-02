# Download followers list

This should contain both the code to get a followers list, and a followers list of all verified twitter users from the account verified when I have time to run it.

To get an updated version use the list, if you don't need to be exact you can download mine. It should be as simple as applying for API tokens from twitter (which isn't really simple but I digress) and then entering them into the config.ini file (including the bearer token, which is necessary).


## Note when building

configparser can't interpret '%' characters, however one way you can fix this if your bearer token has them is to double them up. i.e. '%' => '%%', this technique is [mentioned here](https://stackoverflow.com/questions/71854527/configparser-interpolationsyntaxerror-must-be-followed-by-or-found)
