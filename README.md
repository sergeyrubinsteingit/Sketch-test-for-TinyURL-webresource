A sketch for testing shortening link functionality in the TinyURL app. The targets of test: a) ensure the shortening option is working properly b) ensure idempotency of shortenings of the two identical links  c) check alias creating function.

Written in Python.

Start file: shorten_link_test.py.

Runs in Chrome only.

Scheme: Opens techjob.co.il site homepage => Creates a list of links present of this page => Opens TinyURL homepage => Inserts links from the list into input field, each link twice  => Inserts a random numbers for alias into alias input field  => Clicks MakeTinyURL button  =>  Clicks Copy button => Checks clipboard input and prints it in PyCharm's console =>  Clicks ShortenAnother button  => Repeats the above process for all the links in the list.
