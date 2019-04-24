 # Pitch

## Built By [John Mwangi](link)

## Description
Pitch is an application that allows users to use that one minute. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

* submit a pitch in any category.
* see the pitches other people have posted.
* view the pitches on the page.
* Ability to comment and give feedback.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitch categories | **On page load** | List of various categories of pitches |
| Display pitches | **On page load** | Pitch displays author, title, pitch, date comment tab |
| To add a pitch  | **Click an add pitch** | Redirected to the pitch collection form|
| Display category | **On Tab link click** | Clickable links to open pitches by category |
| Display profile | **Click profile page** | Redirected to a page with your profile |




## SetUp / Installation Requirements
### Prerequisites

* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:

        * git clone (link)
        * cd peech

## Running the Application
* Creating the virtual environment

       * python3.6 -m venv --without-pip virtual
       * source virtual/bin/env
       * curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

         `Requirements.txt`

* To run the application, in your terminal:

         `chmod +x start.sh`
         `./start.sh`

## Testing the Application
* To run the tests for the class files:

         `python3.6 manage.py test`

## Technologies Used
* `Python3.6`
* `Flask`

## License

Copyright (c) 2019 John Mwangi.
