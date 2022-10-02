### PROJECT FOLDERS ORGANIZATION

## RA MODULE 

RA/RA_project/: this folder contains all the code developed for the RA module.

It is composed by:

- ra_action/: it contains scripts and packages for the interface with the simulation map (./config/) and the definition of the actions to be launched on the docker container of the project (./launch/).

- ra_pnp/: it contains the script to launch the plan on the docker container (./launch/pnp.launch), the generated file for the PDDL plan (./plans/), the script to run the plan in the docker container (./scripts/runplan.bash) and the C++ scripts to implement the actions/conditions and to interface them with the map and the docker container (./src/).

- Dockerfile
- build.bash to build the docker container
- run-bash to run the docker container
 

### HRI MODULE ###

HRI/HRI_project/: this folder contains all the code developed for the HRI module.

It is composed by:

- actions/: it contains all the txt files for the actions involved during the Menu Selection (./menu/), during the Table Reservation (./tables/) and during the Order Confirmation (./confirmations/). It contains also other txt files for the actions needed for the execution of the module (e.g. welcome, occupied, confirmation, etc.)

- img/: it contains all the images shown during the executions of the modim interaction

- scripts/: it contains three Python files (./generator.py to generate all the combinations of ordered dishes and drinks; ./table_reservation.py to execute the MODIM implementation to book the tables; ./menu_selection.py to execute the MODIM implementation to select the menu)

- index.html is the HTML file for the GUI setup of the pages.
- qaws.js is a JavaScript file to implement interactive actions (e.g. clicking a button) and server related stuff
