# prawframe
prawframe is a small framework for running plugin-based reddit bots. prawframe supports scheduling plugins and includes a remote python console for modifying your bot's behavior while it runs.

Documentation coming ~~soon~~ at some point.  Check [`example.py`](https://github.com/Wykleph/prawframe/blob/master/prawframe/example.py) for an
example of the features so far.  Run [`server.py`](https://github.com/Wykleph/prawframe/blob/master/prawframe/server.py) to run 
the remote python console "server".  The bot will connect
to you and you can send it python code.  Everything is
accessible through the [`Bot`](https://github.com/Wykleph/prawframe/blob/master/prawframe/bot.py) object.  Put your plugins in
[`plugins.py`](https://github.com/Wykleph/prawframe/blob/master/prawframe/plugins.py) to add your plugins to the remote python console's
namespace.

Make sure to open up the [`.env`](https://github.com/Wykleph/prawframe/blob/master/prawframe/.env) file to configure your bot.

## Install

`pip install prawframe`
