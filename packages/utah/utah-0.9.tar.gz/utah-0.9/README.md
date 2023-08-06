# utah

This module is used as an example package for the Sept 2018 meetup,
and also used as an example on slcpy.com.

# Standard Installation

- `pip install utah`
- Set your `MEETUP_API_KEY` value: `$export MEETUP_API_KEY=api_key_value`, located at [meetup.com](https://secure.meetup.com/meetup_api/key/).
- Test with `from utah import slcpython; slcpython.howdy()` in a python interpreter. You should see details of the next meetup.

# Dev Installation

- Install `pipenv`: `python3 -m pip install pipenv`.
- Install the pipenv requirements: `pipenv sync --dev'
- After hacking, use `pipenv install -e .` 
- For testing use: `python -m pytest`


## TODO

- [x] Add tests
- [x] Integrate `meetup api` to find latest meetups.
  - [ ] Research if public api exists.
  - [ ] Figure out friendly auth flow for API key.
- [ ] Use rst for README
