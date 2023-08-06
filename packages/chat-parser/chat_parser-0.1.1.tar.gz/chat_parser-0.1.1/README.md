# chat-parser
Tools for chat data analytic

## Install
```bash
pip3 install chat-parser
```

## Usages
```python
from chat_parser.data_extractor import Operator

o = Operator()

o.whatsapp_create_frame("path/to/exported_chat.txt")

```

## GeneralOperator methods
GeneralOperator methods accept no arguments, it operates whole dataframe
| Methods |Description |
| --- | --- |
|count_owner  |count owners occurrences |
|count_year  | count years occurrences |
|count_month  |count months occurrences|
|count_day  | count day name occurences|
|count_hour  | count hour occurences from 0 to 24|
|count_word  | count words occurences|
|count_emojis  | count emojis occurences|


## OwnerOperator methods
OwnerOperator methods accept the owner name as argument, raise KeyError if the owner is not presents
 Methods |Description |
| --- | --- |
|count_owner_days  |count days name occurrences of targeted owner|
|count_owner_emojis|count emojis of targeted owner|
|count_owner_hours|count owner hourly activities| 
|count_owner_words|count owner words|
|is_owner_exist| return True if owner exist|
|owner_activities|get the date when the owner is active|


## TextOperator methods
TextOperator methods accepts word as argument
Methods |Description |
| --- | --- |
|count_text_dayname |count the occurences of word according to the day name it occurs|
|count_text_owners|count the owners who said the word|
|get_text_conversations|get the conversations which contain the word|
|get_text_activities|get the date when the word is occurs| 


## DateOperator methods
DateOperator methods accepts date string YYYY-MM-DD as argument, raise KeyError if date doesn't exist
Methods |Description |
| --- | --- |
|count_time_owners |count the owners occurences at the date|
|count_time_words | count the words occurences at the date|
|count_time_emojis | count the emojis occurences at the date|
|get_conversation_at | get the conversations at the date|