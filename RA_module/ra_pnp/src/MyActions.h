#ifndef _MY_ACTIONS_
#define _MY_ACTIONS_

// robotname as external variable (defined in MyActions.cpp)
extern std::string robotname;

// Action implementation

void ainit(string params, bool *run);
void gotopose(string params, bool *run);
void home(string params, bool *run);

void moverobot(string params, bool *run);
void takeorder(string params, bool *run);
void bringplate(string params, bool *run);
void releaseplate(string params, bool *run);

#endif

