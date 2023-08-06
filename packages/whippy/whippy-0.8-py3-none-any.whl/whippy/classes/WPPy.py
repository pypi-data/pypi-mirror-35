import fileinput
import mysql.connector
import os
import re
import tarfile
import urllib.request


class WPPy:
    unwanted_characters = re.compile('(\W+)|(_+)')

    def __init__(self, use_defaults):
        if use_defaults:
            self.directory_home = ""
            self.directory_nginx_available = ""
            self.directory_nginx_enabled = ""
            self.directory_nginx_includes = ""
            self.site_url = ""
        else:
            self.directory_home = os.getenv("DIR_DEFAULT")
            self.directory_nginx_available = os.getenv("DIR_NGINX_AVAILABLE")
            self.directory_nginx_enabled = os.getenv("DIR_NGINX_ENABLED")
            self.directory_nginx_includes = os.getenv("DIR_NGINX_INCLUDES")
            self.site_url = os.getenv("URL_DEFAULT_SCHEMA") + "://" + os.getenv("URL_DEFAULT_DOMAIN")

            if not self.directory_nginx_includes.endswith("/"):
                self.directory_nginx_includes + "/"

        self.database_username = ""
        self.database_password = ""
        self.database_name = ""

        self.directory_site = ""
        self.directory_wordpress = ""

        self.is_sub_directory = True    # TODO: make this false and write the NGINX Config generator

        self.site_name = ""

        self.set_database()
        self.set_directories()
        self.set_site_url()

    @staticmethod
    def format_directory(directory_name):
        return WPPy.unwanted_characters.sub('-', directory_name).lower()

    @staticmethod
    def get_salt():
        with urllib.request.urlopen(os.getenv('URL_WP_SALT')) as response:
            return response.read()

    @staticmethod
    def create_password(iterations):
        if iterations < 2:
            iterations = 2

        password = ""

        for x in range(iterations):
            with urllib.request.urlopen("https://www.passwordrandom.com/query?command=password") as response:
                password = password + response.read()

        return password

    # create a database name
    def create_database_name(self):
        db_name = self.site_name
        db_name.replace('-', '_')

        self.database_name = "wp_" + db_name

    # create a database username
    def create_database_username(self):
        temp_username = self.site_name
        temp_username.split('-')
        username = ""

        for tu in temp_username:
            username = username + tu[0]

        self.database_username = "wp_" + username

    # create the WP database
    def create_wp_database(self):
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS')
        )

        db_cursor = db.cursor()

        query = "CREATE DATABASE %s; GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%s' IDENTIFIED BY '%s';"
        parameters = (self.database_name, self.database_name, self.database_username, os.getenv('DB_HOST'),
                      self.database_password)

        db_cursor.execute(query, parameters)
        db.commit()

    # create the WordPress directory with files
    def create_wp_site(self):
        # build the path
        if not os.path.exists(self.directory_home):
            os.makedirs(self.directory_home)

        # extract the WP tarball
        wp_files = tarfile.open(os.getenv('DIR_WP_TARBALL'), 'r:gz')
        wp_files.extractall(self.directory_home)

        # rename the config file
        config_sample_filename = self.directory_wordpress + "/wp-config-sample.php"
        config_filename = self.directory_wordpress + "/wp-config.php"
        os.rename(config_sample_filename, config_filename)

        # edit the WP config file
        self.edit_wp_config(config_filename)

        # edit the NGINX config file
        if self.is_sub_directory:
            self.create_nginx_include()
        else:
            self.create_nginx_config()

        # rename the WP directory
        os.rename(self.directory_wordpress, self.directory_site)

    def create_nginx_config(self):
        if self.is_sub_directory:
            print("Wrong method...")

        print("This option is currently unavailable")

    # create an NGINX include file
    def create_nginx_include(self):
        location_include_text = "\tlocation /{} {\n" \
                                "\t\tindex index.php;\n" \
                                "\t\ttry_files $uri $uri/ /{}/index.php?$args;" \
                                "\n}\n".format(self.site_name, self.site_name)

        location_include_file_name = self.directory_nginx_includes + self.site_name + ".conf"

        if not os.path.exists(location_include_file_name):
            location_include_file = open(location_include_file_name, 'w')
        else:
            location_include_file = open(location_include_file_name, 'a')

        location_include_file.write(location_include_text)
        location_include_file.close()

    # edit the WP config file
    def edit_wp_config(self, config_filename):
        wp_salt = WPPy.get_salt()
        wp_salt.splitlines()

        wp_fs_direct = "\n\n/** Sets up 'direct' method for WordPress, auto-update without FTP **/\n" \
                       "define('FS_METHOD', 'direct');\n\n"

        search_lines = [
            "database_name_here",
            "username_here",
            "password_here",
            "localhost",
            "define('AUTH_KEY', 'put your unique phrase here');",
            "define('SECURE_AUTH_KEY', 'put your unique phrase here');",
            "define('LOGGED_IN_KEY', 'put your unique phrase here');",
            "define('NONCE_KEY', 'put your unique phrase here');",
        ]

        replace_lines = [
            self.database_name,
            self.database_username,
            self.database_password,
            os.getenv("DB_HOST"),
            wp_salt[0],
            wp_salt[1],
            wp_salt[2],
            wp_salt[3],
        ]

        # overwrite the config
        with fileinput.FileInput(config_filename, True) as wp_config_file:
            for line in wp_config_file:
                for key, search_line in enumerate(search_lines):
                    line.replace(search_line, replace_lines[key])

        # add the FS_DIRECT method for FTP-free auto-updates to the config file
        wp_config_file = open(config_filename, 'a')
        wp_config_file.write(wp_fs_direct)
        wp_config_file.close()

    # set properties, but ensure they don't exist first
    def set_database(self):
        if self.database_name == "":
            self.create_database_name()

        if self.database_username == "":
            self.create_database_username()

        if self.database_password == "":
            self.create_password(3)

    # sets directories; requires user interaction
    def set_directories(self):
        # set home directory
        if self.directory_home == "":
            home_directory = input("Please enter the home directory: [%s]".format(os.getenv('DIR_DEFAULT')))

            if home_directory == "":
                self.directory_home = os.getenv("DIR_DEFAULT")
            else:
                self.directory_home = home_directory

        # set site name
        site_name = ""
        while site_name == "":
            site_name = input("Please enter the site name: ")

        self.site_name = self.format_directory(site_name)

        # set site path
        if self.directory_home.endswith('/') or self.site_name.startswith('/'):
            self.directory_site = self.directory_home + self.site_name
        else:
            self.directory_site = self.directory_home + '/' + self.site_name

        # set NGINX config directories
        if self.directory_nginx_available == "":
            self.directory_nginx_available = input(
                "Please enter the NGINX sites-available (or just sites) directory: [%s]".format(
                    os.getenv("DIR_NGINX_AVAILABLE")))

        if self.directory_nginx_enabled == "":
            self.directory_nginx_enabled = input(
                "Please enter the NGINX sites-enabled (or just sites) directory: [%s]".format(
                    os.getenv("DIR_NGINX_ENABLED")))

        if self.directory_nginx_includes == "":
            self.directory_nginx_includes = input(
                "Please enter the NGINX includes directory: [%s]".format(os.getenv("DIR_NGINX_INCLUDES")))

        # set WordPress directory
        if self.directory_home.endswith('/'):
            self.directory_wordpress = self.directory_home + "wordpress"
        else:
            self.directory_wordpress = self.directory_home + "/wordpress"

    # set site URL
    def set_site_url(self):
        site_url = input("Please enter the domain and TLD for the site: [%s] ".format(os.getenv("URL_DEFAULT_DOMAIN")))
        site_schema = input("Please enter the URL schema (ex: http, https): [%s] ").format(
            os.getenv("URL_DEFAULT_SCHEMA"))

        if site_url == "":
            site_url = os.getenv("URL_DEFAULT_DOMAIN")

        if site_schema == "":
            site_schema = os.getenv("URL_DEFAULT_SCHEMA")

        site_schema.replace("://", "")  # make sure we don't duplicate this

        self.site_url = site_schema + "://" + site_url
