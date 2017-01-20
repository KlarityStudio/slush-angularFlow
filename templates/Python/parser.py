#Python scrapper for scrapping webflow content

import os
import zipfile
import fnmatch
from bs4 import BeautifulSoup


def zip_extract():

    webflow_destination = "../Webflow/"

    webflow_zip = "td-phoenix.webflow.zip"
    print("Extracting zip file")
    webflow_zip = zipfile.ZipFile(webflow_destination+webflow_zip, "r")
    webflow_zip.extractall(webflow_destination)
    webflow_zip.close()
    print("Finished extracting zip file")

zip_extract()

def parse():

    parsed_html = "./parsed_html/"
    for root, dirnames, filenames in os.walk('../Webflow'):

        if not os.path.exists(parsed_html):
            os.system("mkdir parsed_html")

        for filename in fnmatch.filter(filenames, '*.html'):
            new_file = parsed_html+filename
            original_file = os.path.join(root, filename)

            os.system("cd parsed_html")
            with open(original_file) as File:
                read_file = File.read()

                files = open(new_file, 'w')
                files.write(read_file)
            os.system("cd ..")



parse()

def component_builder():

    html_files = "./parsed_html"
    all_files = os.listdir(html_files)

    for files in all_files:

        with open(html_files+"/"+files, "r") as html:

            html_page = BeautifulSoup(html, 'lxml')
            component_tag = html_page.find_all("", {"component": True})

            for component in component_tag:
                component_name = component["component"]

                if os.path.exists("../Angular/app/Components/"+component_name):
                    print("Directory exists")

                else:
                    os.system("mkdir ../Angular/app/Components/"+component_name)

                if os.path.exists("../Angular/app/Components/"+component_name+"/"+component_name+".component.html"):
                    print("File exists")

                else:
                    new_file = open("../Angular/app/Components/"+component_name+"/"+component_name+".component.html", "w")
                    component = component.prettify()
                    new_file.write(str(component))


component_builder()

def static_files():

    css_directory = "../Webflow/css/"
    js_directory = "../Webflow/js/"
    angular_directory = "../Angular/"

    list_css = os.listdir(css_directory)
    list_js = os.listdir(js_directory)

    for css_files in list_css:

        new_css = angular_directory+css_files
        with open(css_directory+css_files, "r") as files:

            files = files.read()
            new_css = open(new_css, 'w')
            new_css.write(files)



    for js_files in list_js:

        new_js = angular_directory+js_files
        with open(js_directory+js_files, "r") as files:

            files = files.read()
            new_js = open(new_js, 'w')
            new_js.write(files)


static_files()


def director_cleaner():

    directory = "../Webflow/*"

    print("Cleaning files")
    os.system("rm -rf " +directory)

director_cleaner()