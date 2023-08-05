
def quandl_apikey_set(apikey):
    """Store the Quandl Token in $HOME/.updoon_quandl 

    Parameters:
    -----------
    apikey : str
        The API Key from the Quandl Website. 
        See https://www.quandl.com/account/api
    
    """
    import pathlib 
    filename = str(pathlib.Path.home()) + "/.updoon_quandl";
    fileptr = open(filename, 'w');
    fileptr.write(apikey);
    fileptr.close();
    return None;

def quandl_apikey():
    """ Returns the locally store QUandl API key from $HOME/.updoon_quandl 

    Returns
    -------
    apikey : str
        The API Key from the Quandl Website. 
        See https://www.quandl.com/account/api

    The function will throw an exception if the 
    file $HOME/.updoon_quandl does not exist.
    Use `quandl_apikey_set("mysupersecrettoken")`
    to store your Quandl API Key first.

    The function will also throw an exception if
    the file $HOME/.updoon_quandl returns an empty
    string.
        
    """
    import pathlib 
    filename = str(pathlib.Path.home()) + "/.updoon_quandl";
    errmsg2 = 'Please add your Quandl API Key with quandl_apikey_set("mysupersecrettoken")';
    try:
        fileptr = open(filename, 'r');
        apikey = fileptr.read();
        fileptr.close();
        if apikey:
            if len(apikey)>0:
               return apikey;
        raise Exception('File "$HOME/.updoon_quandl" seems empty. ' + errmsg2);
    except: 
        raise Exception('No "$HOME/.updoon_quandl" file found. ' + errmsg2);
