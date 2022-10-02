#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <actionlib/client/simple_action_client.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <sensor_msgs/LaserScan.h>
//for mapping key of location to coordinates
// #include <map>
#include <iostream>

#include <boost/thread/thread.hpp>

#define radians(a) ((a)/180.0*M_PI)

#define RESET   	"\033[0m"
#define RED     	"\033[31m"      	/* Red */
#define GREEN   	"\033[32m"      	/* Green */
#define CYAN    	"\033[36m"      	/* Cyan */
#define BOLDRED		"\033[1m\033[31m"      	/* Bold Red */
#define BOLDGREEN   	"\033[1m\033[32m"      	/* Bold Green */


std::string robotname="";

// defined in robotpose.cpp
bool getRobotPose(std::string robotname, double &x, double &y, double &th_rad);

// defined in gotopose.cpp
void exec_gotopose(std::string robotname, float GX, float GY, float GTh, bool *run);

using namespace std;

std::string turn_topic = "turn";
std::string movebase_topic = "move_base";

//actionlib::SimpleActionClient<rp_action_msgs::TurnAction> *ac_turn = NULL;
//actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> *ac_movebase = NULL;


/*** ACTIONS ***/

void start_gotopose(float GX, float GY, float GTh, bool *run) {

  exec_gotopose(robotname, GX, GY, GTh, run);

}


// Action implementation

void ainit(string params, bool *run) {
  cout << "\n### Executing Init ... " << params << endl;
  // Set turn topic

  float GX=10.58;
  float GY=25.60;
  float GTh=0;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
      cout << "### Finished Init " << endl;
  else
      cout << "### Aborted Init  " << endl;
}

void gotopose(string params, bool *run) {
  cout << "\n### Executing Gotopose ... " << params << endl;

  int i=params.find("_");
  float GX=atof(params.substr(0,i).c_str());
  int j=params.find("_",i+1);
  float GY=atof(params.substr(i+1,j).c_str());
  float GTh=atof(params.substr(j+1).c_str());

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished Gotopose " << endl;
  else
    cout << "### Aborted Gotopose  " << endl;
}

void home(string params, bool *run)
{
  cout << "\n### Executing Home ... " << params << endl;

  float GX=10.58;
  float GY=25.60;
  float GTh=0;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished Home " << endl;
  else
    cout << "### Aborted Home  " << endl;
}


// key mapping from location name to map coordinate
std::map<string, string> initMap() {
    static std::pair<string, string> data[] = {
        std::pair<string, string>("entrance", "10.58_25.60_0_0"),
      	std::pair<string, string>("corridor1", "16.50_22.89_0_0"),
      	std::pair<string, string>("corridor2", "16.50_18.39_0_0"),
      	std::pair<string, string>("corridor3", "16.50_13.89_0_0"),
      	std::pair<string, string>("corridor4", "16.50_9.39_0_0"),
      	std::pair<string, string>("corridor5", "16.50_4.89_0_0"),
      	std::pair<string, string>("table1", "24.77_22.89_0_0"),
      	std::pair<string, string>("table2", "24.77_18.39_0_0"),
      	std::pair<string, string>("table3", "24.77_13.89_0_00"),
      	std::pair<string, string>("table4", "24.77_9.39_0_0"),
      	std::pair<string, string>("table5", "24.77_4.89_0_0"),
      	std::pair<string, string>("kitchen", "4.54_14.0_0_0")
    };

    return map<string, string>(data, data + sizeof(data) / sizeof(*data));
}

// To initiate the map, use:
// std::map<string, string> map_loc2coord = initMap();


void moverobot(string params, bool *run) {
  cout << "\n### Executing moveRobot ..." << endl;
  
  // detect parameters
  int i = params.find("_");
  int j = params.find("_", i+1);
  string from = params.substr(i+1,j-i-1).c_str();
  string to = params.substr(j+1).c_str();
    
  // initiate mapping between map location name and coordinate
  std::map<string, string> map_loc2coord = initMap();
  
  cout << BOLDGREEN << "\t~ Moving the robot from " << from << " to " << to << " ~\n" << RESET << endl;
  // get location coordinate
  string nextcoord = map_loc2coord[to];

  i=nextcoord.find("_");
  float GX=atof(nextcoord.substr(0,i).c_str());
  j=nextcoord.find("_",i+1);
  float GY=atof(nextcoord.substr(i+1,j).c_str());
  float GTh=atof(nextcoord.substr(j+1).c_str());
  //cout << GREEN << "\t~ Moving the robot to " << GX << ", " << GY << ", " << GTh << RESET << endl;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished moveRobot " << endl;
  else
    cout << "### Aborted moveRobot  " << endl;
}

// ADDED FUNCTION FOR HRI_PROJECT
// TAKE ORDER
void takeorder(string params, bool *run) {
  cout << "\n### Executing takeOrder ..." << endl;
  
  // detect parameters
  int i = params.find_last_of("_");
  string table = params.substr(i+1).c_str();
  
  cout << BOLDGREEN << "\t~ Pepper is taking the order at " << table << " ~\n" << endl;
  ros::Duration(2).sleep();
  cout << RED << "\t~ Pepper says: Hi, you can order what you want with my tablet! ~\n";
  ros::Duration(2).sleep();
  cout << CYAN << "\t~ Humans are placing the order for plate" << table[5] << " ~\n" << RESET << endl; 
  ros::Duration(10).sleep();
  if (*run)
    cout << "### Finished takeOrder " << endl;
  else
    cout << "### Aborted takeOrder " << endl;
}


// BRING PLATE
void bringplate(string params, bool *run) {
  cout << "\n### Executing bringPlate ... " << endl;
  
  // detect parameters
  int i = params.find("_");
  int j = params.find("_", i+1);
  int k = params.find("_", j+1);
  string loc = params.substr(i+1,j-i-1).c_str();
  string plate = params.substr(j+1, k-j-1).c_str();
  string table = params.substr(k+1).c_str();
  
  cout << BOLDGREEN << "\t~ Pepper is bringing the " << plate << " at " << loc << " for " << table << " ~\n" << RESET << endl;
  ros::Duration(2).sleep();
  
  if (*run)
    cout << "### Finished bringPlate " << endl;
  else
    cout << "### Aborted bringPlate " << endl;
}


// RELEASE PLATE
void releaseplate(string params, bool *run) {
  cout << "\n### Executing releasePlate ... " << endl;
  
  // detect parameters
  int i = params.find("_");
  int j = params.find("_", i+1);
  string table = params.substr(i+1, j-i-1).c_str();
  string plate = params.substr(j+1).c_str();
  
  cout << BOLDGREEN << "\t~ Pepper is releasing the " << plate << " at " << table << " ~\n" << RESET << endl;
  ros::Duration(2).sleep();
  
  if (*run)
    cout << "### Finished releasePlate " << endl;
  else
    cout << "### Aborted releasePlate " << endl;
}
