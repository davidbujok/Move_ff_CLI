#!/usr/bin/python
        # click.echo(f"{ click.style(number, fg='white') } { click.style(file_path[x:-1], fg='green') } ")
import click 
import os
import subprocess

from click.termui import style

home_directory = os.environ.get('HOME')
current_folder = os.getcwd()

@click.command()
@click.option("--name", prompt="File name")
@click.option("--type", default="file")

def cli(name, type):
    list_of_files = subprocess.run(["fd", "--base-directory", f"{ home_directory }", "-I", name],
                                   capture_output=True, text=True)
    split_list_of_files = list_of_files.stdout.split()
    number = 1
    if (type == "dir"):
        click.echo("Directory")
    else:
        click.echo("File")
    while (not len(split_list_of_files)):
        click.echo("File doesn't exist")
        file_name = click.prompt("File name")
        list_of_files_r = subprocess.run(["fd", "--base-directory", f"{ home_directory }", "-I", file_name],
                                   capture_output=True, text=True)
        split_list_of_files = list_of_files_r.stdout.split()

    if (len(split_list_of_files) == 1):
        file_path = split_list_of_files[0]
        x = file_path.rfind("/")
        fileToMove = file_path
    else:
        for path in split_list_of_files:
            x = path.rfind("/")
            click.echo(f"{ click.style(number, fg='white') } { click.style(path[x:-1], fg='green') } ")
            number+=1
        userChoice = click.prompt("File number", type=int)
        fileToMove = split_list_of_files[userChoice - 1]

    click.echo(f"Where to move {fileToMove}?")

    locationToMove = click.prompt("folder name")
    listOfDestinations = subprocess.run(["fd", "--base-directory", f"{ home_directory }", "-td", "-I",
                                         locationToMove], capture_output=True, text=True)
    splitListOfDestinations = listOfDestinations.stdout.split()
    if (locationToMove == "."):
        splitListOfDestinations = []
        splitListOfDestinations.append(current_folder)

    while (not len(splitListOfDestinations)):
        click.echo("Folder doesn't exist")
        new_location_to_move = click.prompt("folder name") 
        listOfDestinations = subprocess.run(["fd", "--base-directory", f"{ home_directory }", "-td", "-I",
                                             new_location_to_move], capture_output=True, text=True)
        splitListOfDestinations = listOfDestinations.stdout.split()

    number = 1
    if (len(splitListOfDestinations) == 1):
        destinationPath = splitListOfDestinations[0]
        y = file_path.rfind("/")
    else:
        for path in splitListOfDestinations:
            click.echo(f"{ click.style(number, fg='white') } { click.style(path, fg='green') } ")
            number += 1
        userDestinationNumber = click.prompt("Which the file should go to?", type=int)
        destinationPath = splitListOfDestinations[userDestinationNumber - 1]
    click.echo(destinationPath)
    if (locationToMove == "."):
        moveFile = subprocess.run(["mv", f"{home_directory}/{ fileToMove }", f"{ destinationPath }"])
    else:
        moveFile = subprocess.run(["mv", f"{home_directory}/{ fileToMove }", f"{home_directory}/{ destinationPath }"])

if __name__ == "__main__":
    cli()
