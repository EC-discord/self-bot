import requests

__author__ = 'Corey Hoard'
__version__ = '1.0.0'
__license__ = 'MIT'

__all__ = ['Imgflip', 'Meme']

class Imgflip(object):
    """
    Access the Imgflip RESTful JSON API.
    A username and password are needed to caption images, but are not needed to get
    the current list of memes.

    Examples:

    # List all memes available by name
    import pyimgflip
    api = pyimgflip.Imgflip()
    memes = api.get_memes()
    for meme in memes:
        print(meme.name)


    # Post a random meme and print its url
    import pyimgflip
    import random
    api = pyimgflip.Imgflip(username='your_username', password='******')
    memes = api.get_memes()
    meme = random.choice(memes)
    print("Generating a meme from template: " + meme.name)
    result = api.caption_image(meme, "Top Text", "Bottom Text")
    print("Meme available at URL: " + result['url'])


    See Imgflip's documentation at https://api.imgflip.com for more information.
    Most function descriptions taken from the above URL.
    """

    def __init__(self, username = None, password = None):
        """
        Create a new Imgflip instance.

        Args:
            username (str) [optional]: Username of any valid imgflip account. 
            password (str) [optional]: Corresponding account password
        """

        super(Imgflip, self).__init__()
        self.username = username
        self.password = password

    def get_memes(self):
        """ 
        Get list of available memes.

        Gets an array of popular memes that may be captioned with this API. 
        The size of this array and the order of memes may change at any time. 
        When this description was written, it returned 100 memes ordered by 
        how many times they were captioned in the last 30 days.

        Returns:
            A list of pyimgflip.Meme objects
        Raises:
            HTTPError: if the API cannot be reached or returns an invalid response.
            RuntimeError: if the API indicates an unsuccessful response or JSON cannot be parsed.
        """
        
        url = 'https://api.imgflip.com/get_memes'
        r = requests.get(url)
        r.raise_for_status()
        response = r.json()
        if response['success']:
            return [Meme.fromJSON(meme) for meme in response['data']['memes']]
        else:
            raise RuntimeError("Imgflip returned error message: " + response['error_message'])


    def caption_image(self, meme, text0, text1, font='impact', max_font_size=50):
        """
        Add a caption to an Imgflip meme template.

        Args:
            meme (pyimgflip.Meme, int): Accepts either a Meme object or a valid Imgflip template ID.
            text0 (str): The top text for the meme.
            text1 (str): The bottom text for the meme.
            font (str): Current options are 'impact' and 'arial'. Defaults to 'impact'.
            max_font_size (int): Maximum font size in pixels. Defaults to 50px.
        Returns:
            A dictionary as with keys "url" and "page_url" as reported by Imgflip.
        Raises:
            HTTPError: if the API cannot be reached or returns an invalid response.
            RuntimeError: if the API indicates an unsuccessful response.
            TypeError: if meme id is an invalid type
            ValueError: if font is passed an incorrect value
        """
        url = 'https://api.imgflip.com/caption_image'
        if self.username is None or self.password is None:
            raise RuntimeError("Username and password required to caption image.")
        try: 
            try:
                template_id = int(meme.id)
            except AttributeError as e:
                template_id = int(meme)
        except ValueError as e:
            raise TypeError("Meme id must be a numeric value.")

        font_clean = font.lower().strip()
        if font_clean != 'impact' and font_clean != 'arial':
            raise ValueError("Font parameter must be either 'impact' or 'arial'.")

        payload = {'username':self.username, 'password':self.password,
                   'template_id':template_id, 
                   'text0':text0, 'text1':text1, 
                   'font':font_clean, 'max_font_size':max_font_size}

        r = requests.post(url, data=payload)
        r.raise_for_status()
        response = r.json()
        if response['success']:
            return response['data']
        else:
            raise RuntimeError("Imgflip returned error message: " + response['error_message'])
        
    def caption_image_boxes(self, meme, boxes, font='impact', max_font_size=50):
        """
        Uses Imgflip's more advanced 'boxes' interface for maximum customization.
        See https://api.imgflip.com for usage details.

        Args:
            meme (pyimgflip.Meme, int): Accepts either a Meme object or a valid Imgflip template ID.
            boxes (dict): Custom text boxes as specified by the API.
            font (str): Current options are 'impact' and 'arial'. Defaults to 'impact'.
            max_font_size (int): Maximum font size in pixels. Defaults to 50px.
        Returns:
            A dictionary as with keys "url" and "page_url" as reported by Imgflip.
        Raises:
            HTTPError: if the API cannot be reached or returns an invalid response.
            RuntimeError: if the API indicates an unsuccessful response.
            TypeError: if meme id is an invalid type
            ValueError: if font is passed an incorrect value
        """
        url = 'https://api.imgflip.com/caption_image'
        if self.username is None or self.password is None:
            raise RuntimeError("Username and password required to caption image.")
        try: 
            try:
                template_id = int(meme.id)
            except AttributeError as e:
                template_id = int(meme)
        except ValueError as e:
            raise TypeError("Meme id must be a numeric value.")

        font_clean = font.lower().strip()
        if font_clean != 'impact' and font_clean != 'arial':
            raise ValueError("Font parameter must be either 'impact' or 'arial'.")

        payload = {'username':self.username, 'password':self.password,
                   'template_id':template_id, 
                   'text0':'', 'text1':'', 
                   'boxes':boxes,
                   'font':font_clean, 'max_font_size':max_font_size}

        r = requests.post(url, data=payload)
        r.raise_for_status()
        response = r.json()
        if response['success']:
            return response['data']
        else:
            raise RuntimeError("Imgflip returned error message: " + response['error_message'])

    def __str__(self):
        return repr(self)

    def __repr__(self):
        if self.username is None or self.password is None:
            return '<pyimgflip.Imgflip>'
        else:
            return '<pyimgflip.Imgflip for user "%s">' % self.username


class Meme(object):
    """
    Represents a meme template as returned by pyimgflip.Imgflip.get_memes().

    Fields:
        id (int): Meme template ID number. Needed to caption images.
        name (str): Human-readable name.
        url (str): URL to an uncaptioned prototype image.
        width (int): Image width in pixels.
        height (int): Image height in pixels.
    """

    def __init__(self, id, name='', url='', width=0, height=0):
        """
        Create a new Meme instance

        Args:
            id (int): Meme template ID number. Needed to caption images.
            name (str): Human-readable name.
            url (str): URL to an uncaptioned prototype image.
            width (int): Image width in pixels.
            height (int): Image height in pixels.
        """

        super(Meme, self).__init__()
        self.id = int(id)
        self.name = name
        self.url = url
        self.width = width
        self.height = height

    @classmethod
    def fromJSON(cls, data):
        """
        Create a Meme instance from a JSON API response.

        Args:
            data (dict): A JSON object as returned by the get_memes endpoint
        Returns:
            The newly-created Meme object
        Raises:
            RuntimeError: if the JSON object cannot be properly parsed
        """

        try:
            return cls(**data)
        except AttributeError:
            raise RuntimeError("JSON cannot be properly parsed into Meme object: " + str(data))

    def __str__(self):
        return '<pyimgflip.Meme with id %i and name "%s">' % (self.id, self.name)

    def __repr__(self):
        return '<pyimgflip.Meme with id %i>' % self.id

