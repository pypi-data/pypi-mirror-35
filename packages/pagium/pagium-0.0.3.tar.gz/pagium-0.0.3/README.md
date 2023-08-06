About this
==========

This is page object implementation for selenium library.

How to use
==========

1. Basic usage

```python
from pagium import Page, PageElement, By, Remote


class GooglePage(Page):

    search = PageElement(by=By.NAME, value='q')


wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
)

with GooglePage(wd, 'https://google.com') as page:
    page.search.send_keys(*'python selenium')
```

2. Controls usage

```python
from pagium import Page, PageElement, WebElement, By, Remote, Keys


class SearchInput(WebElement):

    def fill(self, text):
        self.send_keys(*text + Keys.ENTER)


class GooglePage(Page):

    search = PageElement(SearchInput, by=By.NAME, value='q')


wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
)

with GooglePage(wd, 'https://google.com') as page:
    page.search.fill('python selenium')
```

3. Container usage

```python
from pagium import Page, PageElement, WebElement, By, Remote, Keys


class SearchInput(WebElement):

    def fill(self, text):
        self.send_keys(*text + Keys.ENTER)


class SearchForm(WebElement):

    input = PageElement(SearchInput, by=By.NAME, value='q')


class GooglePage(Page):

    search_form = PageElement(SearchForm)


wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
)

with GooglePage(wd, 'https://google.com') as page:
    page.search_form.input('python selenium')
```

4. Web driver polling

Pagium has feature polling for web drivers

```python
wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
    polling_timeout=20,
    polling_delay=0.5,
)
```

Polling timeout is retry time for a while execute command raise error and delay is sleep time between reties.

It make using like

```python
wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
)

with wd.enable_polling(20, delay=0.1):
    ...
```

or

```python
wd = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
    polling_timeout=20,
    polling_delay=0.5,
)

with wd.disable_polling():
    ...
```
