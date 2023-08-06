# Copyright (c) 2018 UniquID

import click
from uniquid.core.login_manager import LoginManager
from uniquid.core.cli_console import CliConsole
import uniquid.core.constants as constants
import uniquid.cli as cli


@click.command()
@click.argument('org',
                required=False)
@click.option('--access-key',
              envvar='UNIQUID_ACCESS_KEY',
              help=('UniquID Access Key. Provided after account registration.'
                    ' The option can also be set using the environment'
                    ' variable UNIQUID_ACCESS_KEY.'),
              required=True)
@click.option('--user',
              envvar='UNIQUID_USER',
              help=('UniquID Username. Provided during account registration.'
                    ' The option can also be set using the environment'
                    ' variable UNIQUID_USER.'),
              required=True)
@click.option('--login-url',
              envvar='UNIQUID_LOGIN_URL',
              help=('UniquID server URL for the Login. Option is available to'
                    ' allow the user to specify the URL of the login server.'
                    ' This is not normally required. The URL'
                    ' must be in the format <ip address>:<port number>. The'
                    ' inclusion of the port number is optional.'
                    ' The option can also be set using the environment'
                    ' variable UNIQUID_LOGIN_URL.'),
              required=False)
@click.option('--org-url',
              envvar='UNIQUID_ORG_URL',
              help=('UniquID server URL for the user\'s Organization. Option'
                    ' is available to'
                    ' allow the user to specify the URL of their assigned'
                    ' server. This is not normally required. The URL'
                    ' must be in the format <ip address>:<port number>. The'
                    ' inclusion of the port number is optional.'
                    ' The option can also be set using the environment'
                    ' variable UNIQUID_ORG_URL.'),
              required=False)
def login(org, access_key, user, login_url, org_url):
    """Login to the Uniquid system, specifying the Organization Identifier ORG.

    When first logging into the system, the user must specify their
    Organization Identifier, which is assigned to them during registration.
    After this first successful login, they no longer need to pass this
    argument unless they want to change the organization account they
    are using.
    """
    cc = CliConsole(click.echo, cli.print_error,
                    constants.FORMAT_TEXT, click.ClickException)
    lm = LoginManager(cc)
    lm.connect(org, access_key, user, login_url, org_url)


@click.command()
def logout():
    """Logout from the Uniquid system."""
    cc = CliConsole(click.echo, cli.print_error,
                    constants.FORMAT_TEXT, click.ClickException)
    lm = LoginManager(cc)
    lm.disconnect()


@click.command()
@click.option('--verbose',
              is_flag=True,
              default=False,
              help=('Print more detailed status information about'
                    ' the connection to the Uniquid system.'),
              required=False)
@click.option('--output',
              default=constants.FORMAT_TEXT,
              type=click.Choice(constants.FORMAT_ALL),
              help=('Format used to print data to the console. Valid options'
                    ' are: ') + str(constants.FORMAT_ALL),
              required=False)
def status(verbose, output):
    """Print the status of the connection to Uniquid system."""
    cc = CliConsole(click.echo, cli.print_error,
                    output, click.ClickException)
    lm = LoginManager(cc)
    state = lm.get_conn_state()
    cc.begin_list()
    cc.ok(constants.TXT_CONN_STATUS + state)
    if (verbose and
            state == constants.TXT_CONN_LOGGED_IN):
        lm.print_info()
    cc.end_list()
