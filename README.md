# BTCLatestBlockExtract

Reads block data from the Bitcoin API https://chain.api.btc.com/v3/block/latest/tx 
and parses relevant fields and returns a json structure as follows:
    
    {
       "block_height":702457,
       "block_time":"2021-09-27 17:55:03",
       "fee":75317,
       "inputs_value":8648968,
       "outputs_value":8573651,
       "addresses":[
          "bc1q9hetmwa4n904gsz3wqfzc383cvv6umd9vl5e78",
          "bc1qfunj9a3ewecu496lx23rnfwvs3y99v0ywtglsh35uz3v72ksp49sldzxgp"
       ]
    }



The application checks at regular intervals if there is a new block info and if so it processes the data avoiding duplicate records. 

The print statement is for demonstration purposes to show when the retrieved block is already fetched, this can be moved to a log in case of a production pipeline.
    
### Further Enhancements:    
Currently the resulting extract is just printed for demonstration. 
A Data sink can be created as a downstream system, for example as:
* Insert the record into a Database/DWH
* Send the record to a queue or messaging service for downstream applications
* Append the records to a file

Logging and error management
* extra error management and network issues management.
* General logging 
    
