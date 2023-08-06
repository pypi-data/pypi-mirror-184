> SECURITY NOTICE\
> THIS MODULE MAY NOT BE SUITABLE FOR FULL PRODUCTION USE\
> IT MAY OR MAY NOT BE SECURE - NO SEURITY EXPERT HAS CHECKED.\
> IF YOU ARE GOING TO USE THIS MODULE, PLEASE REVIEW THE CODE FIRST,\
> OR ASK A SECURITY EXPERT TO DO SO.

## Introduction

The hashfish python module allows you to easily use salted HMACs for data hashing. It acts as a simple "wrapper" for some of the functions in the hmac module from the standard library. Hashfish allows you to hash data and check the hashes using a quick and easy implementation; one function is for hashing, one for generating secure salt, and one function is for checking (+ one for testing).

## Usage

The usage for hashfish is simple; an example script is shown below: \
\
`import hashfish`\
`       `\
`msg = 'Hello, world!' # Message` \
`key = 'Some key...' # Key/Password ` \
`slt = hashfish.new_salt() # Length of choice may be used by changing the length keyword argument. Default is 16 characters long.` \
`dmd = 'sha256' # Algorithm to use. See hmac.new(...). ` \
`mac = hashfish.new_salty_hmac(msg, key, slt, dmd) # Actually create the HMAC.` \
`print(verify_salty_hmac(mac, msg, key, dmd)) # Test if verified. Should return [bool] True.` 

## Technical ⚙️

Nothing to technical...

## Credits

Credits go to: \
Pigeon Nation :]